import ast
import builtins
import io
import json
import re
import tokenize


CODE_OPTIONS_PREFIX = '__CODE_OPTIONS__\n'

_OUTPUT_QUESTION = re.compile(
    r'\bчто\s+(?:выведет|напечатает|получится|произойдёт|произойдет)\b',
    re.IGNORECASE,
)
_CODE_KEYWORDS = re.compile(
    r'\b(?:def|if|elif|else|for|while|return|print|input|match|case|import|from|try|except|raise|with|pass|break|continue)\b',
)
_CODE_ACTION = re.compile(
    r'\b(?:напишите|запишите|исправьте|перепишите|создайте|добавьте|допишите|'
    r'реализуйте|составьте|измените|упростите|введите|вставьте|сделайте|'
    r'вынесите|напечатайте)\b',
    re.IGNORECASE,
)
_CODE_SNIPPET_QUESTION = re.compile(
    r'\b(?:какое\s+(?:выражение|начальное\s+значение)|'
    r'что\s+короче\s+записывает\s+выражение|'
    r'как\s+передать\b.*\bаргументом|'
    r'какой\s+блок\s+отделяет)\b',
    re.IGNORECASE,
)
_CODE_OPERATORS = re.compile(
    r'\+=|-=|\*=|/=|//=|%=|\*\*=|==|!=|<=|>=|(?<![<>=!])=(?!=)|[<>]|[+*/%]|[(){}\[\]]|[A-Za-z_]\w*\.[A-Za-z_]\w*\s*\('
)
_PLAIN_OPERATORS = {'and', 'or', 'not', 'in', 'is', 'if / else'}
_MAIN_GUARD = re.compile(r'^if\s+__name__\s*==\s*([\'"])__main__\1\s*:?\s*$')
_IGNORED_TOKENS = {
    tokenize.ENDMARKER,
    tokenize.NEWLINE,
    tokenize.NL,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.COMMENT,
}


def is_code_task(question, answer, task_type=None):
    """Detect code-writing tasks without treating printed output as source code."""
    if task_type == 'practice':
        return True
    if not isinstance(answer, str) or not answer.strip():
        return False
    if answer.startswith(CODE_OPTIONS_PREFIX):
        return True
    if _OUTPUT_QUESTION.search(question or ''):
        return False
    normalized_answer = answer.strip().casefold()
    if normalized_answer in _PLAIN_OPERATORS:
        return False
    has_code_syntax = bool(_CODE_KEYWORDS.search(answer) or _CODE_OPERATORS.search(answer))
    if _CODE_ACTION.search(question or ''):
        return has_code_syntax
    return bool(
        _CODE_SNIPPET_QUESTION.search(question or '')
        and has_code_syntax
        and re.search(r'\b[A-Za-z_]\w*\b', answer)
    )


def _normalized_code(code):
    """Compare Python syntax while ignoring formatting and local variable names."""
    try:
        tree = ast.parse(code.strip())
    except (SyntaxError, TypeError, ValueError):
        try:
            tokens = tokenize.generate_tokens(io.StringIO(code).readline)
            return tuple(
                (token.type, token.string)
                for token in tokens
                if token.type not in _IGNORED_TOKENS
            )
        except (tokenize.TokenError, IndentationError):
            return None

    builtin_names = set(dir(builtins))

    class NormalizeNames(ast.NodeTransformer):
        def __init__(self):
            self.names = {}

        def normalize(self, name):
            if name in builtin_names:
                return name
            if name not in self.names:
                self.names[name] = f'__name_{len(self.names)}'
            return self.names[name]

        def visit_Name(self, node):
            node.id = self.normalize(node.id)
            return node

        def visit_arg(self, node):
            node.arg = self.normalize(node.arg)
            return self.generic_visit(node)

        def visit_FunctionDef(self, node):
            node.name = self.normalize(node.name)
            return self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):
            node.name = self.normalize(node.name)
            return self.generic_visit(node)

    return ast.dump(NormalizeNames().visit(tree), include_attributes=False)


def _strip_code_fence(answer):
    candidate = answer.strip()
    if candidate.startswith('```') and candidate.endswith('```'):
        candidate = candidate[3:-3].strip()
        if candidate.startswith('python'):
            candidate = candidate[6:].strip()
    return candidate


def _code_input_variants(answer):
    """Return normalized input and a decoded copy for JSON-escaped pasted code."""
    source = _strip_code_fence(answer).replace('\r\n', '\n').replace('\r', '\n')
    candidates = [source]
    try:
        ast.parse(source.strip())
    except (SyntaxError, TypeError, ValueError):
        if r'\n' in source or r'\t' in source or r'\r' in source:
            try:
                decoded = json.loads(f'"{source}"')
            except (TypeError, ValueError):
                decoded = (
                    source.replace(r'\r\n', '\n')
                    .replace(r'\n', '\n')
                    .replace(r'\r', '\n')
                    .replace(r'\t', '\t')
                    .replace(r'\"', '"')
                )
            if decoded != source:
                candidates.append(decoded)

    normalized = []
    for candidate in candidates:
        signature = _normalized_code(candidate)
        if signature is not None and signature not in normalized:
            normalized.append(signature)
    return normalized, candidates


def _main_guard_signature(code):
    first_line = next((line.strip() for line in code.splitlines() if line.strip()), '')
    return bool(_MAIN_GUARD.fullmatch(first_line))


def task_answer_is_correct(task, answer):
    if not is_code_task(task.question, task.correct_answer, task.task_type):
        return answer.strip().lower() == task.correct_answer.strip().lower()

    expected_answers = [task.correct_answer]
    if task.correct_answer.startswith(CODE_OPTIONS_PREFIX):
        try:
            expected_answers = json.loads(task.correct_answer[len(CODE_OPTIONS_PREFIX):])
        except (TypeError, ValueError):
            return False

    normalized_answers, answer_variants = _code_input_variants(answer)
    if any(
        _main_guard_signature(expected)
        and any(_main_guard_signature(candidate) for candidate in answer_variants)
        for expected in expected_answers
    ):
        return True
    expected_signatures = {
        _normalized_code(expected)
        for expected in expected_answers
    }
    return any(signature in expected_signatures for signature in normalized_answers)

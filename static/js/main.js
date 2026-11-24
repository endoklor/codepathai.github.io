// CodePath AI — общий фронтенд-скрипт.
// Здесь позже появится логика live-обновления чата и вызовов AI-помощника (Этапы 4–5).
document.addEventListener('DOMContentLoaded', () => {
  console.log('CodePath AI загружен');
});

function handleCodeEditorTab(event) {
  if (event.key !== 'Tab') return;
  event.preventDefault();
  const editor = event.currentTarget;
  const start = editor.selectionStart;
  const end = editor.selectionEnd;

  if (event.shiftKey) {
    const lineStart = editor.value.lastIndexOf('\n', start - 1) + 1;
    const beforeCursor = editor.value.slice(lineStart, start);
    const spaces = Math.min(4, (beforeCursor.match(/^ */) || [''])[0].length);
    if (spaces) editor.setRangeText('', lineStart, lineStart + spaces, 'preserve');
    return;
  }

  editor.setRangeText('    ', start, end, 'end');
}

function formatPastedCode(text) {
  if (!text) return text;

  const fence = text.match(/^```(?:python)?[ \t]*\r?\n([\s\S]*?)\r?\n```$/i);
  if (fence) return fence[1];
  if (/[\r\n]/.test(text)) return text;

  const hasEncodedLineBreak = /:\s*\\(?:r\\)?n|\\(?:r\\)?n(?:\\t|[ \t]+|(?:def|if|elif|else|for|while|return|try|except|with|print|import|from|class)\b)/.test(text);
  if (!hasEncodedLineBreak) return text;

  const trimmed = text.trim();
  try {
    const decoded = trimmed.startsWith('"') && trimmed.endsWith('"')
      ? JSON.parse(trimmed)
      : JSON.parse(`"${text}"`);
    return typeof decoded === 'string' && /[\r\n]/.test(decoded) ? decoded : text;
  } catch {
    return text
      .replace(/\\r\\n/g, '\n')
      .replace(/\\n/g, '\n')
      .replace(/\\t/g, '\t')
      .replace(/\\"/g, '"');
  }
}

function handleCodeEditorPaste(event) {
  const pastedText = event.clipboardData?.getData('text/plain');
  const formattedText = formatPastedCode(pastedText);
  if (!pastedText || formattedText === pastedText) return;

  event.preventDefault();
  const editor = event.currentTarget;
  editor.setRangeText(formattedText, editor.selectionStart, editor.selectionEnd, 'end');
}

function attachCodeEditorKeys() {
  document.querySelectorAll('textarea.code-editor').forEach((editor) => {
    editor.addEventListener('keydown', handleCodeEditorTab, true);
    editor.addEventListener('paste', handleCodeEditorPaste);
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', attachCodeEditorKeys, { once: true });
} else {
  attachCodeEditorKeys();
}

// Dashboard interactions from the supplied design, connected to real site data.
let sandboxWorker = null;
let sandboxWorkerUrl = null;
const defaultSandboxCode = 'print("Привет, CodePath AI!")\n\nfor number in range(1, 4):\n    print("Урок", number)';

function createSandboxWorker() {
  if (sandboxWorker) return sandboxWorker;
  const source = `
    import { loadPyodide } from 'https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.mjs';
    let runtime;
    self.onmessage = async (event) => {
      try {
        if (!runtime) {
          self.postMessage({ type: 'loading' });
          runtime = await loadPyodide();
        }
        self.postMessage({ type: 'preparing' });
        await runtime.loadPackagesFromImports(event.data);
        self.postMessage({ type: 'running' });
        const output = [];
        runtime.setStdout({ batched: (line) => output.push(line) });
        runtime.setStderr({ batched: (line) => output.push(line) });
        await runtime.runPythonAsync(event.data);
        self.postMessage({ type: 'done', output: output.join('\\n') || 'Код выполнен без вывода.' });
      } catch (error) {
        self.postMessage({ type: 'error', output: error && error.message ? error.message : String(error) });
      }
    };
  `;
  sandboxWorkerUrl = URL.createObjectURL(new Blob([source], { type: 'text/javascript' }));
  sandboxWorker = new Worker(sandboxWorkerUrl, { type: 'module' });
  sandboxWorker.addEventListener('error', () => {
    sandboxWorker?.terminate();
    sandboxWorker = null;
    if (sandboxWorkerUrl) URL.revokeObjectURL(sandboxWorkerUrl);
    sandboxWorkerUrl = null;
  }, { once: true });
  return sandboxWorker;
}

async function runPythonSandbox() {
  const editor = document.getElementById('sandboxEditor');
  const output = document.getElementById('sandboxOutput');
  const status = document.getElementById('sandboxStatus');
  const button = document.getElementById('runSandboxButton');
  if (!editor || !output || !status || !button) return;

  button.disabled = true;
  status.textContent = 'Загружаю Python…';
  output.textContent = '';
  let settled = false;
  let timer;
  let worker;
  try {
    worker = createSandboxWorker();
    await new Promise((resolve, reject) => {
      const finish = (callback, value) => {
        if (settled) return;
        settled = true;
        window.clearTimeout(timer);
        worker.removeEventListener('message', onMessage);
        worker.removeEventListener('error', onError);
        callback(value);
      };
      const onMessage = (event) => {
        if (event.data.type === 'loading') {
          status.textContent = 'Загружаю Python…';
          return;
        }
        if (event.data.type === 'preparing') {
          status.textContent = 'Подготавливаю импорты…';
          window.clearTimeout(timer);
          timer = window.setTimeout(() => finish(reject, new Error('Подготовка Python заняла слишком много времени.')), 30000);
          return;
        }
        if (event.data.type === 'running') {
          status.textContent = 'Выполняю…';
          window.clearTimeout(timer);
          timer = window.setTimeout(() => finish(reject, new Error('Время выполнения превышено (5 секунд).')), 5000);
          return;
        }
        if (event.data.type === 'done') {
          output.textContent = event.data.output;
          status.textContent = 'Готово';
          finish(resolve);
        } else if (event.data.type === 'error') {
          output.textContent = event.data.output;
          status.textContent = 'Ошибка';
          finish(resolve);
        }
      };
      const onError = () => finish(reject, new Error('Не удалось запустить среду Python в браузере.'));
      worker.addEventListener('message', onMessage);
      worker.addEventListener('error', onError);
      timer = window.setTimeout(() => finish(reject, new Error('Не удалось загрузить среду Python. Проверьте подключение к интернету.')), 30000);
      worker.postMessage(editor.value);
    });
  } catch (error) {
    output.textContent = error?.message || String(error);
    status.textContent = 'Ошибка';
    if (worker) {
      worker.terminate();
      if (sandboxWorker === worker) sandboxWorker = null;
      if (sandboxWorkerUrl) URL.revokeObjectURL(sandboxWorkerUrl);
      sandboxWorkerUrl = null;
    }
  } finally {
    button.disabled = false;
  }
}

function resetSandboxCode() {
  const editor = document.getElementById('sandboxEditor');
  const output = document.getElementById('sandboxOutput');
  const status = document.getElementById('sandboxStatus');
  if (!editor || !output || !status) return;
  editor.value = defaultSandboxCode;
  output.textContent = 'Код сброшен к примеру.';
  status.textContent = 'Готово';
  editor.focus();
}

function openLessonPreview() {
  const modal = document.getElementById('lessonPreviewModal');
  const source = document.getElementById('lesson-preview-data');
  if (!modal || !source) return;

  let lesson;
  try {
    lesson = JSON.parse(source.textContent);
  } catch {
    return;
  }
  const title = document.getElementById('previewTitle');
  const subtitle = document.getElementById('previewSubtitle');
  const content = document.getElementById('previewContent');
  const openLink = document.getElementById('previewOpenLesson');
  title.textContent = `Урок ${lesson.number}. ${lesson.title}`;
  subtitle.textContent = `${lesson.language} · ${lesson.level}`;
  openLink.href = lesson.lessonUrl;
  content.replaceChildren();

  if (lesson.theory) {
    const theory = document.createElement('section');
    theory.className = 'preview-block';
    const heading = document.createElement('h3');
    heading.textContent = 'Теория';
    const paragraph = document.createElement('p');
    paragraph.textContent = lesson.theory;
    theory.append(heading, paragraph);
    content.append(theory);
  }
  (lesson.examples || []).forEach((example, index) => {
    const section = document.createElement('section');
    section.className = 'preview-block';
    const heading = document.createElement('h3');
    heading.textContent = example.title || `Пример ${index + 1}`;
    const code = document.createElement('pre');
    code.textContent = example.code;
    section.append(heading, code);
    if (example.explanation) {
      const explanation = document.createElement('p');
      explanation.textContent = example.explanation;
      section.append(explanation);
    }
    content.append(section);
  });
  if ((lesson.tasks || []).length) {
    const tasks = document.createElement('section');
    tasks.className = 'preview-block';
    const heading = document.createElement('h3');
    heading.textContent = `Задания · ${lesson.tasks.length}`;
    tasks.append(heading);
    lesson.tasks.forEach((task, index) => {
      const question = document.createElement('p');
      question.textContent = `${index + 1}. ${task.question}`;
      tasks.append(question);
      if (task.hint) {
        const hint = document.createElement('p');
        hint.className = 'preview-hint';
        hint.textContent = `Подсказка: ${task.hint}`;
        tasks.append(hint);
      }
    });
    const note = document.createElement('p');
    note.className = 'preview-task-note';
    note.textContent = 'Откройте урок, чтобы написать и отправить решения.';
    tasks.append(note);
    content.append(tasks);
  }

  modal.hidden = false;
  document.body.classList.add('modal-open');
  modal.querySelector('.preview-dialog')?.focus();
}

function closeLessonPreview(event) {
  const modal = document.getElementById('lessonPreviewModal');
  if (!modal || (event && event.target !== modal)) return;
  modal.hidden = true;
  document.body.classList.remove('modal-open');
}

function showToast(message) {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast-message';
  toast.textContent = message;
  container.appendChild(toast);
  window.setTimeout(() => toast.remove(), 3200);
}

function initDashboardHeatmap() {
  const grid = document.getElementById('dashboardHeatmap');
  const detail = document.getElementById('heatmapDetail');
  if (!grid || !detail) return;
  const show = (cell) => {
    const count = Number(cell.dataset.count);
    detail.textContent = currentInterfaceLanguage === 'en'
      ? `${cell.dataset.date}: ${count} ${count === 1 ? 'activity' : 'activities'}`
      : `${cell.dataset.date}: ${count} ${count === 1 ? 'действие' : 'действий'}`;
  };
  grid.addEventListener('mouseover', (event) => {
    const cell = event.target.closest('.activity-cell');
    if (cell) show(cell);
  });
  grid.addEventListener('focusin', (event) => {
    const cell = event.target.closest('.activity-cell');
    if (cell) show(cell);
  });
  grid.addEventListener('click', (event) => {
    const cell = event.target.closest('.activity-cell');
    if (cell) show(cell);
  });
}

// Optional background synth. It starts only after the user presses the control.
let ambientAudioContext = null;
let ambientMasterGain = null;
let ambientAudioTimer = null;
let ambientAudioPlaying = false;
let currentInterfaceLanguage = 'ru';
function updateAudioToggleButtons() {
  const label = currentInterfaceLanguage === 'en'
    ? (ambientAudioPlaying ? 'Stop music' : 'Play music')
    : (ambientAudioPlaying ? 'Выключить музыку' : 'Включить музыку');
  document.querySelectorAll('[data-audio-toggle]').forEach((button) => {
    const labelElement = button.querySelector('[data-audio-label]');
    if (labelElement) labelElement.textContent = label;
    button.setAttribute('aria-label', label);
    button.setAttribute('aria-pressed', String(ambientAudioPlaying));
  });
}

function toggleAmbientAudio(button) {
  if (ambientAudioPlaying) {
    ambientAudioPlaying = false;
    window.clearInterval(ambientAudioTimer);
    ambientMasterGain?.disconnect();
    ambientMasterGain = null;
    ambientAudioContext?.suspend();
    updateAudioToggleButtons();
    showToast(currentInterfaceLanguage === 'en' ? 'Ambient sound stopped' : 'Фоновый звук выключен');
    return;
  }

  try {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    if (!AudioContextClass) throw new Error('Web Audio недоступен в этом браузере.');
    ambientAudioContext ||= new AudioContextClass();
    ambientAudioContext.resume();
    ambientMasterGain = ambientAudioContext.createGain();
    ambientMasterGain.gain.value = 0.08;
    ambientMasterGain.connect(ambientAudioContext.destination);
    const chords = [[174.61, 220, 261.63, 329.63], [164.81, 196, 246.94, 293.66], [146.83, 174.61, 220, 261.63], [130.81, 164.81, 196, 246.94]];
    let step = 0;
    const playChord = () => {
      if (!ambientAudioPlaying) return;
      const start = ambientAudioContext.currentTime;
      chords[step++ % chords.length].forEach((frequency) => {
        const oscillator = ambientAudioContext.createOscillator();
        const envelope = ambientAudioContext.createGain();
        oscillator.type = 'triangle';
        oscillator.frequency.value = frequency;
        envelope.gain.setValueAtTime(0.0001, start);
        envelope.gain.exponentialRampToValueAtTime(0.22, start + 0.6);
        envelope.gain.exponentialRampToValueAtTime(0.0001, start + 3.1);
        oscillator.connect(envelope);
        envelope.connect(ambientMasterGain);
        oscillator.start(start);
        oscillator.stop(start + 3.2);
      });
    };
    ambientAudioPlaying = true;
    playChord();
    ambientAudioTimer = window.setInterval(playChord, 3200);
    updateAudioToggleButtons();
    showToast(currentInterfaceLanguage === 'en' ? 'Ambient synth enabled' : 'Фоновый синтезатор включён');
  } catch (error) {
    showToast(currentInterfaceLanguage === 'en' ? 'Could not start ambient music' : (error.message || 'Не удалось включить звук'));
  }
}

function setInterfaceLanguage(language) {
  const selected = language === 'en' ? 'en' : 'ru';
  currentInterfaceLanguage = selected;
  document.documentElement.lang = selected;
  localStorage.setItem('codepath-language', selected);
  document.querySelectorAll('[data-ru][data-en]').forEach((element) => {
    const value = element.dataset[selected];
    if (value) element.textContent = value;
  });
  document.querySelectorAll('[data-placeholder-ru][data-placeholder-en]').forEach((element) => {
    element.placeholder = element.dataset[`placeholder${selected === 'en' ? 'En' : 'Ru'}`];
  });
  document.querySelectorAll('[data-locale-button]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.localeButton === selected));
  });
  updateAudioToggleButtons();
}

function initInterfaceLanguage() {
  const saved = localStorage.getItem('codepath-language') || 'ru';
  setInterfaceLanguage(saved);
  document.querySelectorAll('[data-locale-button]').forEach((button) => {
    button.addEventListener('click', () => setInterfaceLanguage(button.dataset.localeButton));
  });
}

function initAvatarPreview() {
  const input = document.querySelector('input[type="file"][name="avatar"]');
  const preview = document.getElementById('profileAvatarPreview');
  if (!input || !preview) return;
  let previewUrl = null;
  input.addEventListener('change', () => {
    const image = input.files?.[0];
    if (!image) return;
    if (image.type && !image.type.startsWith('image/')) {
      input.value = '';
      showToast('Выберите файл изображения.');
      return;
    }
    if (image.size > 5 * 1024 * 1024) {
      input.value = '';
      showToast('Размер изображения не должен превышать 5 МБ.');
      return;
    }
    if (previewUrl) URL.revokeObjectURL(previewUrl);
    previewUrl = URL.createObjectURL(image);
    let previewImage = preview.querySelector('img');
    if (!previewImage) {
      previewImage = document.createElement('img');
      previewImage.alt = 'Предпросмотр аватара';
      preview.replaceChildren(previewImage);
    }
    previewImage.src = previewUrl;
  });
}

let catalogFilter = 'all';
function updateLanguageCatalog() {
  const grid = document.getElementById('languageCatalog');
  if (!grid) return;
  const query = (document.getElementById('catalogSearch')?.value || '').trim().toLocaleLowerCase();
  const cards = [...grid.querySelectorAll('.catalog-language-card')];
  let visible = 0;
  cards.forEach((card) => {
    const searchMatch = !query || card.dataset.search.includes(query);
    const filterMatch = catalogFilter === 'all'
      || (catalogFilter === 'beginner' ? card.dataset.beginner === 'true' : card.dataset.status === catalogFilter);
    card.hidden = !(searchMatch && filterMatch);
    if (!card.hidden) visible += 1;
  });
  const count = document.getElementById('catalogResultCount');
  const empty = document.getElementById('catalogEmptyState');
  if (count) {
    const noun = currentInterfaceLanguage === 'en'
      ? (visible === 1 ? 'language' : 'languages')
      : (visible === 1 ? 'язык' : visible >= 2 && visible <= 4 ? 'языка' : 'языков');
    count.textContent = `${visible} ${noun}`;
  }
  if (empty) empty.hidden = visible > 0;
}

function toggleLanguageNotice(button) {
  const key = `codepath-notify-${button.dataset.languageSlug}`;
  const subscribed = localStorage.getItem(key) === 'true';
  if (subscribed) {
    localStorage.removeItem(key);
    button.classList.remove('is-subscribed');
    button.textContent = currentInterfaceLanguage === 'en' ? 'Follow launch' : 'Следить за запуском';
    showToast(currentInterfaceLanguage === 'en'
      ? `Launch reminder for ${button.dataset.languageName} removed.`
      : `Отметка о запуске ${button.dataset.languageName} снята.`);
  } else {
    localStorage.setItem(key, 'true');
    button.classList.add('is-subscribed');
    button.textContent = currentInterfaceLanguage === 'en' ? 'Following ✓' : 'Отмечено ✓';
    showToast(currentInterfaceLanguage === 'en'
      ? `A reminder will appear when you reopen the catalog after ${button.dataset.languageName} launches.`
      : `Напомним при следующем открытии каталога, когда появятся курсы ${button.dataset.languageName}.`);
  }
}

function initLanguageCatalog() {
  const search = document.getElementById('catalogSearch');
  const grid = document.getElementById('languageCatalog');
  const buttons = document.querySelectorAll('.catalog-filter');
  if (!grid) return;
  search?.addEventListener('input', updateLanguageCatalog);
  buttons.forEach((button) => button.addEventListener('click', () => {
    catalogFilter = button.dataset.cfilter || 'all';
    buttons.forEach((filterButton) => {
      const active = filterButton === button;
      filterButton.classList.toggle('is-active', active);
      filterButton.setAttribute('aria-pressed', String(active));
    });
    updateLanguageCatalog();
  }));
  document.querySelectorAll('.catalog-notify-button').forEach((button) => {
    if (localStorage.getItem(`codepath-notify-${button.dataset.languageSlug}`) === 'true') {
      button.classList.add('is-subscribed');
      button.textContent = currentInterfaceLanguage === 'en' ? 'Following ✓' : 'Отмечено ✓';
    }
  });
  grid.querySelectorAll('.catalog-language-card[data-status="active"][data-language-slug]').forEach((card) => {
    const key = `codepath-notify-${card.dataset.languageSlug}`;
    if (localStorage.getItem(key) === 'true') {
      localStorage.removeItem(key);
      showToast(currentInterfaceLanguage === 'en'
        ? `New courses are now available for ${card.querySelector('h2')?.textContent.trim()}.`
        : `Для языка ${card.querySelector('h2')?.textContent.trim()} появились курсы.`);
    }
  });
  updateLanguageCatalog();
}

document.addEventListener('DOMContentLoaded', () => {
  initDashboardHeatmap();
  initInterfaceLanguage();
  initAvatarPreview();
  initLanguageCatalog();
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeLessonPreview();
  });
});

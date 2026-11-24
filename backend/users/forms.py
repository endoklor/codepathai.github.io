from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, UserProfile


class RegisterForm(UserCreationForm):
    phone = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(attrs={'placeholder': '+7 900 000-00-00'}),
    )
    username = forms.CharField(label='Никнейм')

    class Meta:
        model = User
        fields = ('phone', 'username', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    username = forms.CharField(label='Никнейм')
    MAX_AVATAR_SIZE = 5 * 1024 * 1024

    class Meta:
        model = UserProfile
        fields = ('bio', 'avatar')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({
            'accept': 'image/*',
            'class': 'avatar-upload-input',
        })
        if self.user:
            self.fields['username'].initial = self.user.username

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        uploaded_avatar = self.files.get(self.add_prefix('avatar'))
        if uploaded_avatar and uploaded_avatar.size > self.MAX_AVATAR_SIZE:
            raise forms.ValidationError('Размер изображения не должен превышать 5 МБ.')
        return avatar

    def save(self, commit=True):
        profile = super().save(commit=False)
        if self.user:
            self.user.username = self.cleaned_data['username']
            if commit:
                self.user.save()
        if commit:
            profile.save()
        return profile

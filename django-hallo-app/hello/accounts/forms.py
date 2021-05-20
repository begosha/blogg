from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile
from django import forms
from django.forms.widgets import PasswordInput


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit)
        Profile.objects.create(user=user)
        return user


class ProfileUpdateForm(forms.ModelForm):
    """
    Форма редактирвоания данных профилья пользователя
    """
    class Meta:
        model = Profile
        exclude = ('user',)


class UserUpdateFrom(forms.ModelForm):
    """
    Форма редактирвоания данных пользователя
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class UserChangePasswordForm(forms.ModelForm):
    """
    Форма смены пароля
    """
    old_password = forms.CharField(required=True, label='Старый пароль', widget=PasswordInput)
    new_password = forms.CharField(required=True, label='Новый пароль', widget=PasswordInput)
    password_confirm = forms.CharField(required=True, label='Подтверждение пароля', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password', 'password_confirm')

    def clean_password_confirm(self):
        """
        https://docs.djangoproject.com/en/3.2/ref/forms/validation/#form-and-field-validation

        В данном методе выполняется валидация подтверждения пароля (Проверяется, что
        новый пароль и подтверждение пароля совпадают).
        """
        new_password = self.cleaned_data.get('new_password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if new_password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return new_password

    def clean_old_password(self):
        """
        https://docs.djangoproject.com/en/3.2/ref/forms/validation/#form-and-field-validation

        В данном методе выполняется валидация старого пароля (Проверяем, что введённый старый
        пароль соответствует текущему пароль пользователя).
        """
        old_password = self.cleaned_data.get('old_password')

        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Пароль введён не верно')

        return old_password

    def save(self, commit=True):
        """
        При сохранении устанавливаем пароль используя метод пользователя set_password
        """
        user = self.instance
        user.set_password(self.cleaned_data.get('new_password'))
        if commit:
            user.save()
        return user

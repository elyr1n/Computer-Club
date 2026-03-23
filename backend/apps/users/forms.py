from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Ник-нейм",
        widget=forms.TextInput(
            attrs={"placeholder": "Ник-нейм", "class": "cyber-input"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль", "class": "cyber-input"}
        ),
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Подтверждение пароля", "class": "cyber-input"}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username",)

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if not (16 <= len(password) <= 32):
            raise ValidationError("Пароль должен быть от 16 до 32 символов!")
        return password


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Ник-нейм",
        widget=forms.TextInput(
            attrs={"placeholder": "Ник-нейм", "class": "cyber-input"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Пароль", "class": "cyber-input"}
        ),
    )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["avatar"]
        widgets = {"avatar": forms.FileInput(attrs={"class": "cyber-input"})}

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(required=True, help_text="Загрузите аватар")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Создаём профиль и сохраняем аватар
            profile = user.profile
            profile.avatar = self.cleaned_data['avatar']
            profile.save()
        return user

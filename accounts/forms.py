from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'nick')

class UserNickEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nick']

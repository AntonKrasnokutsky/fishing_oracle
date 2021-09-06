from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'nick')
    
    def clean(self, *args, **kwargs):
        super().clean()
        nick = self.cleaned_data.get('nick')

        if len(nick) > 14:
            self.add_error(None, 'Должно быть не более 14 букв и цифр.')
        return super().clean()
    

class UserNickEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nick']
    
    def clean(self, *args, **kwargs):
        super().clean()
        nick = self.cleaned_data.get('nick')

        if len(nick) > 14:
            self.add_error(None, 'Должно быть не более 14 букв и цифр.')
        return super().clean()

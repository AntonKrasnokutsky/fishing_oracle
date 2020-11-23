from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)
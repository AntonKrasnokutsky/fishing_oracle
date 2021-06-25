from django.urls import path
 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',
         views.RegistrationView.as_view(),
         name='registrations'),
    path('editnick/',
         views.UserNickEdit.as_view(),
         name='editnick'),
]

from django.urls import path
from . import views

app_name = 'fishing'
urlpatterns = [
    path('', views.fishing, name='fushing'),
    path('<int:fishing_id>/', views.detail, name='detail'),
    path('fish/<int:fish_id>/', views.renewal_name_fish, name="renewal_fish"),
    path('add/', views.fishing_add, name='fishing_add')
]

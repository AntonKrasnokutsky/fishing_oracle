from django.urls import path
from . import views

app_name = 'fishing'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:fishing_id>/', views.detail, name='detail'),
    path('add/', views.fishing_add, name='fishing_add')
]

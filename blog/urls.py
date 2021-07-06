from django.urls import path
from django.urls.conf import re_path
from . import views

app_name = 'news'
urlpatterns = [
    path('<int:news_id>/', views.NewsDetails.as_view(), name='detail'),
    path('<int:news_id>/edit/', views.NewsEdit.as_view(), name='edit'),
    path('new/', views.NewsNew.as_view(), name='add'),
    path('<int:news_id>/delete/', views.NewsDelete.as_view(), name='delete'),
    
]
from django.urls import path
from . import views

app_name = 'fishing'
urlpatterns = [
    path('', views.index, name='index'),
    path('fishing/', views.fishing, name='fishing'),
    path('<int:fishing_id>/', views.detail, name='detail'),
    path('fish/', views.fish, name='fish'),
    path('fish/<int:fish_id>', views.fish_details, name='fish_details'),
    path('fish/<int:fish_id>/', views.renewal_fish, name="renewal_fish"),
    path('fish/add/', views.add_fish, name='add_fish'),
    path('add/', views.fishing_add, name='fishing_add')
]

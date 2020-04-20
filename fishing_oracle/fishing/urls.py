from django.urls import path
from . import views

app_name = 'fishing'
urlpatterns = [
    path('', views.index, name='index'),
    path('fishing/', views.fishing, name='fishing'),
    path('<int:fishing_id>/', views.detail, name='detail'),
    path('fish/', views.fishs, name='fish'),
    path('fish/<int:fish_id>', views.fish_details, name='fish_details'),
    path('fish/<int:fish_id>/', views.fish_renewal, name="fish_renewal"),
    path('fish/add/', views.fish_add, name='fish_add'),
    path('fish/remove/<int:fish_id>/', views.fish_remove, name='fish_remove'),
    path('districts/', views.districts, name='districts'),
    path('districts/add', views.district_add, name='district_add'),
    path('district/<int:district_id>/',
         views.district_renewal, name='district_renewal'),
    path('districts/remove/<int:district_id>/',
         views.district_remove, name='district_remove'),
    path('primings/', views.primings, name='primings'),
    path('primings/add/', views.priming_add, name='priming_add'),
    path('primings/<int:priming_id>',
         views.priming_renewal, name='priming_renewal'),
    path('primings/remove/<int:priming_id>',
         views.priming_remove, name='priming_remove'),
    path('add/', views.fishing_add, name='fishing_add')
]

from django.urls import path
from fishing.view import views_fishs as views


urlpatterns = [
    # Настройки сайта
    # Справочник рыб
    path('',
         views.FishList.as_view(),
         name='fish_list'),
    # Описание рыбы
    path('<int:fish_id>/',
         views.FishDetails.as_view(),
         name='fish_details'),
    ]

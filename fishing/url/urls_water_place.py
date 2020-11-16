from django.urls import path
from fishing.view import views_water_place


urlpatterns = [
    # Водоёмы
    # Список водоёмов
    path('',
         views_water_place.WaterList.as_view(),
         name='water'),
    path('add/',
         views_water_place.WaterAdd.as_view(),
         name='water_add'),
    path('<int:water_id>/delete',
         views_water_place.WaterDelete.as_view(),
         name='water_delete'),
    path('<int:water_id>/edit',
         views_water_place.WaterEdit.as_view(),
         name='water_edit'),
    ]

from django.urls import path, include
from fishing.view import views_water_place as views


urlpatterns = [
    # Водоёмы
    # Список водоёмов
    path('',
         views.WaterList.as_view(),
         name='water'),
    path('add/',
         views.WaterAdd.as_view(),
         name='water_add'),
    path('<int:water_id>/delete',
         views.WaterDelete.as_view(),
         name='water_delete'),
    path('<int:water_id>/edit',
         views.WaterEdit.as_view(),
         name='water_edit'),
    path('<int:water_id>/places',
         views.PlaceList.as_view(),
         name='places'),
    path('<int:water_id>/places/add',
         views.PlaceAdd.as_view(),
         name='place_add'),
    path('<int:water_id>/places/<int:place_id>/edit',
         views.PlaceEdit.as_view(),
         name='place_edit'),
    path('<int:water_id>/places/<int:place_id>/delete',
         views.PlaceDelete.as_view(),
         name='place_delete'),
    path('<int:water_id>/places/<int:place_id>/coordinates/add',
         views.PlaceCoordinatesAdd.as_view(),
         name='place_coordinates_add'),
    # Реализация маркерных карт отложена
    # path('<int:water_id>/places/<int:place_id>/bottommap/', include('fishing.url.urls_bottom_map')),
    ]

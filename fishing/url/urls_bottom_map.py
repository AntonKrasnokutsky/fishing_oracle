from django.urls import path
from fishing.view import views_bottom_map as views


urlpatterns = [
    # Блок маркерных карт
    # Список маркерных карт
    path('',
         views.bottom_map_list,
         name='bottom_map'),
    # Добавление маркерной карты
    path('add/',
         views.bottom_map_add,
         name='bottom_map_add'),
    # Редактирование маркерной карты
    path('<int:bottom_map_id>/renewal/',
         views.bottom_map_renewal,
         name='bottom_map_renewal'),
    # Описание маркерной карты
    path('<int:bottom_map_id>/',
         views.bottom_map_details,
         name='bottom_map_details'),
    # Удаление маркерной карты
    path('<int:bottom_map_id>/remove/',
         views.bottom_map_remove,
         name='bottom_map_remove'),
    # Точки маркерной карты
    path('<int:bottom_map_id>/point/',
         views.bottom_map_point_list,
         name='point'),
    # Добавление точки маркерной карты
    path('<int:bottom_map_id>/point/add/',
         views.bottom_map_point_add,
         name='point_add'),
    # Редактирование точки маркерной карты
    path('<int:bottom_map_id>/point/<int:point_id>/renewal/',
         views.bottom_map_point_renewal,
         name='point_renewal'),
    # Информация о точке маркерной карты
    path('<int:bottom_map_id>/point/<int:point_id>',
         views.bottom_map_point_details,
         name='point_details'),
    # Удаление точки маркерной карты
    path('<int:bottom_map_id>/point/<int:point_id>/remove/',
         views.bottom_map_point_remove,
         name='point_remove'),
    ]

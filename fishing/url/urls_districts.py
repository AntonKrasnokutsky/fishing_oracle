from django.urls import path
from fishing.view import views_districts as views


urlpatterns = [
    # Блок Районов
    # Список районов
    path('',
         views.district_list,
         name='districts'),
    # Добавление района
    path('add/',
         views.district_add,
         name='district_add'),
    # Редактирование района
    path('<int:district_id>/renewal',
         views.district_renewal,
         name='district_renewal'),
    # Удаление района
    path('<int:district_id>/remove/',
         views.district_remove,
         name='district_remove'),
        ]

from django.urls import path
from fishing.view import views_leash as views


urlpatterns = [
    # Поводки
    # Список поводков
    path('',
         views.LeashList.as_view(),
         name='leash'),
    # Добавление поводка
    path('add/',
         views.LeashAdd.as_view(),
         name='leash_add'),
    # Редактирование поводка
    path('<int:leash_id>/edit/',
         views.LeashEdit.as_view(),
         name='leash_edit'),
    # Удаление поводка
    path('<int:leash_id>/delete/',
         views.LeashDelete.as_view(),
         name='leash_delete'),
    ]

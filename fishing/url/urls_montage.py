from django.urls import path
from fishing.view import views_montage as views


urlpatterns = [
    # Монтажи
    # Список монтажей
    path('',
         views.MontageList.as_view(),
         name='montage'),
    # Добавить монтаж
    path('add/',
         views.MontageAdd.as_view(),
         name='montage_add'),
    # Изменить монтаж
    path('<int:montage_id>/edit/',
         views.MontageEdit.as_view(),
         name='montage_edit'),
    # Удалить монтаж
    path('<int:montage_id>/delete/',
         views.MontageDelete.as_view(),
         name='montage_delete'),
    ]

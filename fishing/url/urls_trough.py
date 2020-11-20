from django.urls import path
from fishing.view import views_trough as views


urlpatterns = [
    # Кормушки
    # Список кормушек
    path('',
         views.TroughList.as_view(),
         name='trough'),
    # Добавление кормушки
    path('add/',
         views.TroughAdd.as_view(),
         name='trough_add'),
    # Редактирование кормушки
    path('<int:trough_id>/edit/',
         views.TroughEdit.as_view(),
         name='trough_edit'),
    # Удаление кормушки
    path('<int:trough_id>/delete/',
         views.TroughDelete.as_view(),
         name='trough_delete'),
    ]

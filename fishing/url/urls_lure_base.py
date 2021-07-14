from django.urls import path
from fishing.view import views_lure_base as views


urlpatterns = [
    # Прикорм
    # Список прикормов
    path('',
         views.LureBaseList.as_view(),
         name='lure_base'),
    # Добавление прикорма
    path('add/',
         views.LureBaseAdd.as_view(),
         name='lure_base_add'),
    # Редактирование прикорма
    path('<int:lure_base_id>/edit/',
         views.LureBaseEdit.as_view(),
         name='lure_base_edit'),
    # Удаление прикорма
    path('<int:lure_base_id>/delete/',
         views.LureBaseDelete.as_view(),
         name='lure_base_delete'),
    ]

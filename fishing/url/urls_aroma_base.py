from django.urls import path
from fishing.view import views_aroma_base as views


urlpatterns = [
    # Арома базовая
    # Список аром
    path('',
         views.AromaBaseList.as_view(),
         name='aroma_base'),
    # Добавление аромы
    path('add/',
         views.AromaBaseAdd.as_view(),
         name='aroma_base_add'),
    # Редактирование аромы
    path('<int:aroma_base_id>/edit/',
         views.AromaBaseEdit.as_view(),
         name='aroma_base_edit'),
    # Удаление аромы
    path('<int:aroma_base_id>/delete/',
         views.AromaBaseDelete.as_view(),
         name='aroma_base_delete'),
    ]

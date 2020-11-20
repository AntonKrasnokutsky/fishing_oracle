from django.urls import path
from fishing.view import views_crochet as views


urlpatterns = [
    # Крючки
    # Список крючков
    path('',
         views.CrochetList.as_view(),
         name='crochet'),
    # Добавление крючка
    path('add/',
         views.CrochetAdd.as_view(),
         name='crochet_add'),
    # Редактирование крючка
    path('<int:crochet_id>/edit/',
         views.CrochetEdit.as_view(),
         name='crochet_edit'),
    # Удаление крючка
    path('<int:crochet_id>/delete/',
         views.CrochetDelete.as_view(),
         name='crochet_delete'),
    ]

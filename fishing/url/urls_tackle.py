from django.urls import path
from fishing.view import views_tackle as views


urlpatterns = [
    # Снасти
    # Список снастей
    path('',
         views.TackleList.as_view(),
         name='tackle'),
    # Добавление снасти
    path('add/',
         views.TackleAdd.as_view(),
         name='tackle_add'),
    # Редактирование снасти
    path('<int:tackle_id>/edit/',
         views.TackleEdit.as_view(),
         name='tackle_edit'),
    # Удаление снасти
    path('<int:tackle_id>/delete/',
         views.TackleDelete.as_view(),
         name='tackle_delete'),
    ]

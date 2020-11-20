from django.urls import path
from fishing.view import views_nozzle_base as views


urlpatterns = [
    # Состояние наживки
    # Добавление состояния наживки
    path('state/add/',
         views.NozzleStateAdd.as_view(),
         name='nozzle_state_add'),
    # Редактирование состояния наживки
    path('state/<int:nozzle_state_id>/edit/',
         views.NozzleStateEdit.as_view(),
         name='nozzle_state_edit'),
    # Удаление состояния наживки
    path('state/<int:nozzle_state_id>/delete/',
         views.NozzleStateDelete.as_view(),
         name='nozzle_state_delete'),

    # Наживки
    # Список насадок/наживок
    path('',
         views.NozzleBaseList.as_view(),
         name='nozzle_base'),
    # Добавление насадки
    path('add/',
         views.NozzleBaseAdd.as_view(),
         name='nozzle_base_add'),
    # Редактирование насадки
    path('<int:nozzle_base_id>/edit/',
         views.NozzleBaseEdit.as_view(),
         name='nozzle_base_edit'),
    # Удаление насадки
    path('<int:nozzle_base_id>/delete/',
         views.NozzleBaseDelete.as_view(),
         name='nozzle_base_delete'),

    # Добавление наживки
    path('add/bait/',
         views.BaitBaseAdd.as_view(),
         name='bait_base_add'),
    # Редактирование наживки
    path('<int:bait_base_id>/bait/edit/',
         views.BaitBaseEdit.as_view(),
         name='bait_base_edit'),
    ]

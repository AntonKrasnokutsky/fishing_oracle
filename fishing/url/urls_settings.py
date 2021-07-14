from django.urls import path
from fishing.view import views_settings as views


urlpatterns = [
    # Настройки сайта
    path('',
         views.Settings.as_view(),
         name='settings'),
    
    # Блок грунта
    # Список вариантов грунта
    path('primings/',
         views.PrimingList.as_view(),
         name='primings'),
    # Добавление грунта
    path('primings/add/',
         views.PrimingAdd.as_view(),
         name='priming_add'),
    # Редактирование грунта
    path('primings/<int:priming_id>/edit/',
         views.PrimingEdit.as_view(),
         name='priming_edit'),
    # Удаление грунта
    path('primings/<int:priming_id>/delete/',
         views.PrimingDelete.as_view(),
         name='priming_delete'),
    
    # Погодные явления
    # Список погодных явления
    path('condition/',
         views.ConditionsList.as_view(),
         name='conditions'),
    # Добавление погодного явления
    path('conditions/add/',
         views.ConditionsAdd.as_view(),
         name="conditions_add"),
    # Редактирование погодного явления
    path('conditions/<int:conditions_id>/edit/',
         views.ConditionsEdit.as_view(),
         name='conditions_edit'),
    # Удаление погодного явления
    path('conditions/<int:conditions_id>/delete/',
         views.ConditionsDelete.as_view(),
         name='conditions_delete'),

    # Облачность
    # Список вариантов облачности
    path('overcast/',
         views.OvercastList.as_view(),
         name='overcast'),
    # Добавдение варианта облачности
    path('overcast/add/',
         views.OvercastAdd.as_view(),
         name='overcast_add'),
    # Редактирование варианта облачности
    path('overcast/<int:overcast_id>/edit/',
         views.OvercastEdit.as_view(),
         name='overcast_edit'),
    # Удаление варианта облачности
    path('overcast/<int:overcast_id>/delete/',
         views.OvercastDelete.as_view(),
         name='overcast_delete'),

    # Темп
    # Список вариантов таблицы Темп
    path('pace/',
         views.PaceList.as_view(),
         name='pace'),
    # Добавление варианта темпа
    path('pace/add/',
         views.PaceAdd.as_view(),
         name='pace_add'),
    # Редактирование варианта темпа
    path('pace/<int:pace_id>/edit',
         views.PaceEdit.as_view(),
         name='pace_edit'),
    # Удаление варианта темпа
    path('pace/<int:pace_id>/delete/',
         views.PaceDelete.as_view(),
         name='pace_delete'),

    # Тип наживок
    # Список типов наживок
    path('nozzletype/',
         views.NozzleTypeList.as_view(),
         name='nozzle_type'),
    # Добавление типа наживки
    path('nozzletype/add/',
         views.NozzleTypeAdd.as_view(),
         name='nozzle_type_add'),
    # Редактирование типа наживки
    path('nozzle/<int:type_id>/edit/',
         views.NozzleTypeEdit.as_view(),
         name='nozzle_type_edit'),
    # Удаление типа наживки
    path('nozzle/<int:type_id>/delete/',
         views.NozzleTypeDelete.as_view(),
         name='nozzle_type_delete'),

    # Кормоемкость
    # Списк вариантов кормоемкости
    path('capacity/',
         views.CapacityList.as_view(),
         name='feed_capacity'),
    # Добавление варианта кормоемкости
    path('capacity/add/',
         views.CapacityAdd.as_view(),
         name='feed_capacity_add'),
    # Редактирование варианта кормоемскости
    path('capacity/<int:capacity_id>/edit/',
         views.CapacityEdit.as_view(),
         name='feed_capacity_edit'),
    # Удаление варианта кормоемкости
    path('capacity/<int:capacity_id>/delete/',
         views.CapacityDelete.as_view(),
         name='feed_capacity_delete'),

    # Справочник рыб
    path('fish/',
         views.FishList.as_view(),
         name='settings_fish_list'),
    # Описание рыбы
    path('fish/<int:fish_id>/',
         views.FishDetails.as_view(),
         name='settings_fish_details'),
    # Редактирование названия рыбы и описания
    path('fish/<int:fish_id>/edit/',
         views.FishEdit.as_view(),
         name="settings_fish_edit"),
    # Добавление рыбы
    path('fish/add/',
         views.FishAdd.as_view(),
         name='settings_fish_add'),
    # Удаление рыбы
    path('fish/<int:fish_id>/delete/',
         views.FishDelete.as_view(),
         name='settings_fish_delete'),
    
    # Категории водоемов
    # Списк категорий водоемов
    path('watercategory/',
         views.WaterCategoryList.as_view(),
         name='water_category'),
    # Добавление категории водоема
    path('watercategory/add/',
         views.WaterCategoryAdd.as_view(),
         name='water_category_add'),
    # Редактирование категории водоема
    path('watercategory/<int:water_category_id>/edit/',
         views.WaterCategoryEdit.as_view(),
         name='water_category_edit'),
    # Удаление категории водоема
    path('watercategory/<int:water_category_id>/delete/',
         views.WaterCategoryDelete.as_view(),
         name='water_category_delete'),
    # Переменные среды
    path('environments/',
         views.EnvironmentVariables.as_view(),
         name='environments'),
    # Список пользователей
    path('users/',
         views.UsersList.as_view(),
         name='fishermans'),
    ]

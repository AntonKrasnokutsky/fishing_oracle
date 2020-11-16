from django.urls import path
from fishing.view import views_settings


urlpatterns = [
    # Настройки сайта
    path('',
         views_settings.Settings.as_view(),
         name='settings'),
    
    # Блок грунта
    # Список вариантов грунта
    path('primings/',
         views_settings.PrimingList.as_view(),
         name='primings'),
    # Добавление грунта
    path('primings/add/',
         views_settings.PrimingAdd.as_view(),
         name='priming_add'),
    # Редактирование грунта
    path('primings/<int:priming_id>/edit/',
         views_settings.PrimingEdit.as_view(),
         name='priming_edit'),
    # Удаление грунта
    path('primings/<int:priming_id>/delete/',
         views_settings.PrimingDelete.as_view(),
         name='priming_delete'),
    
    # Погодные явления
    # Список погодных явления
    path('condition/',
         views_settings.ConditionsList.as_view(),
         name='conditions'),
    # Добавление погодного явления
    path('conditions/add/',
         views_settings.ConditionsAdd.as_view(),
         name="conditions_add"),
    # Редактирование погодного явления
    path('conditions/<int:conditions_id>/edit/',
         views_settings.ConditionsEdit.as_view(),
         name='conditions_edit'),
    # Удаление погодного явления
    path('conditions/<int:conditions_id>/delete/',
         views_settings.ConditionsDelete.as_view(),
         name='conditions_delete'),

    # Облачность
    # Список вариантов облачности
    path('overcast/',
         views_settings.OvercastList.as_view(),
         name='overcast'),
    # Добавдение варианта облачности
    path('overcast/add/',
         views_settings.OvercastAdd.as_view(),
         name='overcast_add'),
    # Редактирование варианта облачности
    path('overcast/<int:overcast_id>/edit/',
         views_settings.OvercastEdit.as_view(),
         name='overcast_edit'),
    # Удаление варианта облачности
    path('overcast/<int:overcast_id>/delete/',
         views_settings.OvercastDelete.as_view(),
         name='overcast_delete'),

    # Темп
    # Список вариантов таблицы Темп
    path('pace/',
         views_settings.PaceList.as_view(),
         name='pace'),
    # Добавление варианта темпа
    path('pace/add/',
         views_settings.PaceAdd.as_view(),
         name='pace_add'),
    # Редактирование варианта темпа
    path('pace/<int:pace_id>/edit',
         views_settings.PaceEdit.as_view(),
         name='pace_edit'),
    # Удаление варианта темпа
    path('pace/<int:pace_id>/delete/',
         views_settings.PaceDelete.as_view(),
         name='pace_delete'),

    # Тип наживок
    # Список типов наживок
    path('nozzletype/',
         views_settings.NozzleTypeList.as_view(),
         name='nozzle_type'),
    # Добавление типа наживки
    path('nozzletype/add/',
         views_settings.NozzleTypeAdd.as_view(),
         name='nozzle_type_add'),
    # Редактирование типа наживки
    path('nozzle/<int:type_id>/edit/',
         views_settings.NozzleTypeEdit.as_view(),
         name='nozzle_type_edit'),
    # Удаление типа наживки
    path('nozzle/<int:type_id>/delete/',
         views_settings.NozzleTypeDelete.as_view(),
         name='nozzle_type_delete'),

    # Кормоемкость
    # Списк вариантов кормоемкости
    path('capacity/',
         views_settings.CapacityList.as_view(),
         name='feed_capacity'),
    # Добавление варианта кормоемкости
    path('capacity/add/',
         views_settings.CapacityAdd.as_view(),
         name='feed_capacity_add'),
    # Редактирование варианта кормоемскости
    path('capacity/<int:capacity_id>/edit/',
         views_settings.CapacityEdit.as_view(),
         name='feed_capacity_edit'),
    # Удаление варианта кормоемкости
    path('capacity/<int:capacity_id>/delete/',
         views_settings.CapacityDelete.as_view(),
         name='feed_capacity_delete'),

    # Справочник рыб
    path('fish/',
         views_settings.FishList.as_view(),
         name='fish_list'),
    # Описание рыбы
    path('fish/<int:fish_id>/',
         views_settings.FishDetails.as_view(),
         name='fish_details'),
    # Редактирование названия рыбы и описания
    path('fish/<int:fish_id>/edit/',
         views_settings.FishEdit.as_view(),
         name="fish_edit"),
    # Добавление рыбы
    path('fish/add/',
         views_settings.FishAdd.as_view(),
         name='fish_add'),
    # Удаление рыбы
    path('fish/<int:fish_id>/delete/',
         views_settings.FishDelete.as_view(),
         name='fish_delete'),
    
    # Категории водоемов
    # Списк категорий водоемов
    path('watercategory/',
         views_settings.WaterCategoryList.as_view(),
         name='water_category'),
    # Добавление категории водоема
    path('watercategory/add/',
         views_settings.WaterCategoryAdd.as_view(),
         name='water_category_add'),
    # Редактирование категории водоема
    path('watercategory/<int:water_category_id>/edit/',
         views_settings.WaterCategoryEdit.as_view(),
         name='water_category_edit'),
    # Удаление категории водоема
    path('watercategory/<int:water_category_id>/delete/',
         views_settings.WaterCategoryDelete.as_view(),
         name='water_category_delete'),
    ]

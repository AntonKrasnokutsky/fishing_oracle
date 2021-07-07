from django.urls import path
from fishing.view import views_fishing as views

urlpatterns = [
    # Блок рыбалки
    # Список рыбалок
    path('',
         views.FishingList.as_view(),
         name='fishing'),
    # Простомтр делатлей о рыбалке
    path('<int:fishing_id>/details',
         views.FishingDetails.as_view(),
         name='fishing_details'),
    # Добавление рыбалки
    path('add/',
         views.FishingAdd.as_view(),
         name='fishing_add'),
    # Редактирование
    path('<int:fishing_id>/edit/',
         views.FishingEdit.as_view(),
         name='fishing_edit'),
    # Удаление рыбалки
    path('<int:fishing_id>/delete/',
         views.FishingDelete.as_view(),
         name='fishing_delete'),
    
    # Место рыбалки
    # Добавление места рыбалки
    path('<int:fishing_id>/select/placefishing/',
         views.FishingPlaceSelect.as_view(),
         name='fishing_place_select'),
    # Добавление и изменение места рыбалки
    path('<int:fishing_id>/add/fishingplace/<int:place_id>/',
         views.FishingPlaceAdd.as_view(),
         name='fishing_place_add'),
    # Удаление места рыбалки
    path('<int:fishing_id>/delete/fishingplace/<int:fishing_place_id>/',
         views.FishingPlaceDelete.as_view(),
         name='fishing_place_delete'),
    
    # Погода на рыбалке
    # Добавить погоду на рыбалке
    path('<int:fishing_id>/add/fishingweather/',
         views.FishingWeatherAdd.as_view(),
         name='fishing_weather_add'),
    # Удалить погоду на рыбалке
    path('<int:fishing_id>/delete/fishingweather/<int:fishing_weather_id>/',
         views.FishingWeatherDelete.as_view(),
         name='fishing_weather_delete'),
    # Выбрать погоду на рыбалке
    path('<int:fishing_id>/edit/fishingweather/<int:fishing_weather_id>/',
         views.FishingWeatherEdit.as_view(),
         name='fishing_weather_edit'),
    
    # Снасть использованная в рыбалке
    # Добавпить снасть в рыбалку
    path('<int:fishing_id>/add/fishingtackle/<int:tackle_id>/<int:fishing_tackle_id>/',
         views.FishingTackleAdd.as_view(),
         name='fishing_tackle_add'),
    # Выбор снасти для рыбалки
    path('<int:fishing_id>/select/fishingtackle/<int:fishing_tackle_id>/',
         views.FishingTackleSelect.as_view(),
         name='fishing_tackle_select'),
    # Удалить снасть в рыбалке
    path('<int:fishing_id>/delete/fishingtackle/<int:fishing_tackle_id>/',
         views.FishingTackleDelete.as_view(),
         name='fishing_tackle_delete'),
    # Добавить новую снасть
    path('<int:fishing_id>/select/fishingtackle/<int:fishing_tackle_id>/add/',
         views.FishingNewTackleAdd.as_view(),
         name='fishing_new_tackle_add'),
    
    # Монтаж использованный в рыбалке
    # Добавить/изменить мотаж в использованный в рыбалке
    path('<int:fishing_id>/add/fishingmontage/<int:fishing_tackle_id>/<int:montage_id>/<int:fishing_montage_id>/',
         views.FishingMontageAdd.as_view(),
         name='fishing_montage_add'),
    # Удалить монтаж использованнй в рыбалке
    path('<int:fishing_id>/delete/fishingmontage/<int:fishing_montage_id>/',
         views.FishingMontageDelete.as_view(),
         name='fishing_montage_delete'),
    # Выбрать монтаж использованный в рыбалке
    path('<int:fishing_id>/select/fishingmontage/<int:fishing_tackle_id>/<int:fishing_montage_id>/',
         views.FishingMontageSelect.as_view(),
         name='fishing_montage_select'),
    # Добавить новый монтаж
    path('<int:fishing_id>/select/fishingmontage/<int:fishing_tackle_id>/<int:fishing_montage_id>/add/',
         views.FishingNewMontageAdd.as_view(),
         name='fishing_new_montage_add'),
    
    # Кормушки использованные в рыбалке
    # Добавить кормушку использованную в рыбалке
    path('<int:fishing_id>/add/fishingtrough/<int:fishing_tackle_id>/<int:trough_id>/<int:fishing_trough_id>/',
         views.FishingTroughAdd.as_view(),
         name='fishing_trough_add'),
    # Удалить кормушку использованную в рыбалке
    path('<int:fishing_id>/delete/fishingtrough/<int:fishing_trough_id>/',
         views.FishingTroughDelete.as_view(),
         name='fishing_trough_delete'),
    # Выбрать кормушку использованную в рыбалке
    path('<int:fishing_id>/select/fishingtrough/<int:fishing_tackle_id>/<int:fishing_trough_id>/',
         views.FishingTroughSelect.as_view(),
         name='fishing_trough_select'),
    # Добавить новую кормушку использованную в рыбалке
    path('<int:fishing_id>/select/fishingtrough/<int:fishing_tackle_id>/<int:fishing_trough_id>/add/',
         views.FishingNewTroughAdd.as_view(),
         name='fishing_new_trough_add'),
    
    # Поводки использованные в рыбалке
    # Добавление поводка использованного в рыбалке
    path('<int:fishing_id>/add/fishingleash/<int:fishing_tackle_id><int:leash_id><int:fishing_leash_id>/',
         views.FishingLeashAdd.as_view(),
         name='fishing_leash_add'),
    # Удаление поводка использованного в рыбалке
    path('<int:fishing_id>/delete/fishingleash/<int:fishing_leash_id>/',
         views.FishingLeashDelete.as_view(),
         name='fishing_leash_delete'),
    # Выбор поводка использованного в рыбалке
    path('<int:fishing_id>/select/fishingleash/<int:fishing_tackle_id><int:fishing_leash_id>/',
         views.FishingLeashSelect.as_view(),
         name='fishing_leash_select'),
    # Добавить поводок использованный в рыбалке
    path('<int:fishing_id>/select/fishingleash/<int:fishing_tackle_id>/<int:fishing_leash_id>/add/',
         views.FishingNewLeashAdd.as_view(),
         name='fishing_new_leash_add'),
    
    # Крючки использованные в рыбалке
    # Добавить крючок в рыбалку
    path('<int:fishing_id>/add/fishingcrochet/<int:fishing_tackle_id><int:crochet_id><int:fishing_crochet_id>/',
         views.FishingCrochetAdd.as_view(),
         name='fishing_crochet_add'),
    # Удалить крючек из рыбалки
    path('<int:fishing_id>/delete/fishingcrochet/<int:fishing_crochet_id>',
         views.FishingCrochetDelete.as_view(),
         name='fishing_crochet_delete'),
    # Выбрать крючок в рыбалке
    path('<int:fishing_id>/select/fishingcrochet/<int:fishing_tackle_id><int:fishing_crochet_id>/',
         views.FishingCrochetSelect.as_view(),
         name='fishing_crochet_select'),
    # Добавить крючок использованный в рыбалке
    path('<int:fishing_id>/select/fishingcrochet/<int:fishing_tackle_id>/<int:fishing_crochet_id>/add/',
         views.FishingNewCrochetAdd.as_view(),
         name='fishing_new_crochet_add'),
    
    # Насадки/наживки использованные в рыбалке\
    # Добавить наживку в рыбалку
    path('<int:fishing_id>/add/fishingnozzle/<int:fishing_tackle_id>/<int:nozzle_id>/<int:fishing_nozzle_id>/',
         views.FishingNozzleAdd.as_view(),
         name='fishing_nozzle_add'),
    # Удалить наживку/насадку из рыбалки
    path('<int:fishing_id>/delete/fishingnozzle/<int:fishing_nozzle_id>/',
         views.FishingNozzleDelete.as_view(),
         name='fishing_nozzle_delete'),
    # Выбрать насадку/наживку для рыбалки
    path('<int:fishing_id>/select/fishingnozzle/<int:fishing_tackle_id><int:fishing_nozzle_id>/',
         views.FishingNozzleSelect.as_view(),
         name='fishing_nozzle_select'),
    
    # Темп рыбалки
    # Добаввить темп рыбалки
    path('<int:fishing_id>/add/fishingpace/<int:fishing_tackle_id><int:pace_id><int:fishing_pace_id>/',
         views.FishingPaceAdd.as_view(),
         name='fishing_pace_add'),
    # Убрать темп рыбалки
    path('<int:fishing_id>/delete/fishingpace/<int:fishing_pace_id>/',
         views.FishingPaceDelete.as_view(),
         name='fishing_pace_delete'),
    # Выбрать темп рыбалки
    path('<int:fishing_id>/select/fishingpace/<int:fishing_tackle_id><int:fishing_pace_id>/',
         views.FishingPaceSelect.as_view(),
         name='fishing_pace_select'),
    
    # Прикормочная смесь для рыбалки
    # Добавить прикормочную смесь
    path('<int:fishing_id>/add/fishinglure/<int:lure_mix_id><int:fishing_lure_mix_id>/',
         views.FishingLureMixAdd.as_view(),
         name='fishing_lure_mix_add'),
    # Удалить прикормочную смесь
    path('<int:fishing_id>/delete/fishinglure/<int:fishing_lure_mix_id>/',
         views.FishingLureMixDelete.as_view(),
         name='fishing_lure_mix_delete'),
    # Выбрать прикормочную смесь
    path('<int:fishing_id>/select/fishinglure/<int:fishing_lure_mix_id>/',
         views.FishingLureMixSelect.as_view(),
         name='fishing_lure_mix_select'),
    
    # Прикорм для рыбалки
    # Указать часть прикорма в рыбалке
    path('<int:fishing_id>/change/lure/<int:lure_base_id><int:fishing_lure_id>/',
         views.FishingLureChangeWeight.as_view(),
         name='fishing_lure_change_weight'),
    # Удалить прикорм из рыбалки
    path('<int:fishing_id>/delete/lure/<int:fishing_lure_id>',
         views.FishingLureDelete.as_view(),
         name='fishing_lure_delete'),
    # Выбрать прикорм для рыбалки
    path('<int:fishing_id>/select/lure/',
         views.FishingLureSelect.as_view(),
         name='fishing_lure_select'),
    
    # Результат рыбалки
    # Добавление результата рыбалки
    path('<int:fishing_id>/add/fishingresult/',
         views.FishingResultAdd.as_view(),
         name='fishing_result_add'),
    # Редактирование ррезультата рыбалки
    path('<int:fishing_id>/edit/fishingresult/<int:fishing_result_id>/',
         views.FishingResultEdit.as_view(),
         name='fishing_result_edit'),
    # Удаление результата рыбалки
    path('<int:fishing_id>/delete/fishingresult/<int:fishing_result_id>/',
         views.FishingResultDelete.as_view(),
         name='fishing_result_delete'),
    
    # Трофейные уловы
    # Добавление трофейного улова
    path('<int:fishing_id>/add/fishingtrophy/',
         views.FishingTrophyAdd.as_view(),
         name='fish_trophy_add'),
    # Редактирование трофейного улова
    path('<int:fishing_id>/edit/fishingtrophy/<int:fishing_trophy_id>/',
         views.FishingTrophyEdit.as_view(),
         name='fish_trophy_edit'),
    # Удаление трофейного улова
    path('<int:fishing_id>/delete/fishingtrophy/<int:fishing_trophy_id>/',
         views.FishingTrophyDelete.as_view(),
         name='fish_trophy_delete'),
    path('<int:fishing_id>/edit/note/',
         views.FishingNoteAddEdit.as_view(),
         name='fishing_note'),
    path('<int:fishing_id>/report_settings',
         views.FishingReportSetingsView.as_view(),
         name='fishing_report_settings'),
    path('<int:fishing_id>/report_settings/delete',
         views.FishingReportsSettingsDelete.as_view(),
         name='fishing_report_settings_delete'),
    
    # Добавление водоемов и мест при оформлении рыбалки
    path('<int:fishing_id>/details/water/select',
         views.FishingPlaceWaterSelect.as_view(),
         name="fishing_place_water_select"),
    
    path('<int:fishing_id>/details/water/add',
         views.FishingPlaceWaterAdd.as_view(),
         name="fishing_place_water_add"),
    
    path('<int:fishing_id>/details/water/<int:water_id>/place',
         views.FishingPlaceWaterPlaceAdd.as_view(),
         name="fishing_place_water_place_add"),
    ]

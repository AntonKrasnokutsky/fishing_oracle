from django.urls import path
from . import views

app_name = 'fishing'
urlpatterns = [
    # Настройки сайта
    path('settings/',
         views.Settings.as_view(),
         name='settings'),
    # Главная страница
    path('',
         views.index,
         name='index'),
    # Блок рыбалки
    # Список рыбалок
    path('fishing/',
         views.fishing_list,
         name='fishing'),
    # Простомтр делатлей о рыбалке
    path('fishing/<int:fishing_id>/details',
         views.fishing_details,
         name='fishing_details'),
    # Добавление рыбалки
    path('fishing/add/',
         views.FishingViews.as_view(),
         name='fishing_add'),
    # Редактирование
    path('fishing/<int:fishing_id>/renewal/',
         views.fishing_renewal,
         name='fishing_renewal'),
    # Удаление рыбалки
    path('fishing/<int:fishing_id>/remove/',
         views.fishing_remove,
         name='fishing_remove'),
    # Блок рыб
    # Справочник рыб
    path('fish/',
         views.FishList.as_view(),
         name='fish_list'),
    # Описание рыбы
    path('fish/<int:fish_id>/',
         views.FishDetails.as_view(),
         name='fish_details'),
    # Редактирование названия рыбы и описания
    path('fish/<int:fish_id>/edit/',
         views.FishEdit.as_view(),
         name="fish_edit"),
    # Добавление рыбы
    path('fish/add/',
         views.FishAdd.as_view(),
         name='fish_add'),
    # Удаление рыбы
    path('fish/<int:fish_id>/delete/',
         views.FishDelete.as_view(),
         name='fish_delete'),
    # Блок Районов
    # Список районов
    path('districts/',
         views.district_list,
         name='districts'),
    # Добавление района
    path('districts/add/',
         views.district_add,
         name='district_add'),
    # Редактирование района
    path('district/<int:district_id>/renewal',
         views.district_renewal,
         name='district_renewal'),
    # Удаление района
    path('districts/<int:district_id>/remove/',
         views.district_remove,
         name='district_remove'),
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
    # Блок погоды
    # Погода
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/weather/',
         views.weather_list,
         name='weather'),
    # Добавление погоды
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/weather/add/',
         views.weather_add,
         name='weather_add'),
    # Редактирование погоды
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/weather/<int:weather_id>/renewal/',
         views.weather_renewal,
         name='weather_renewal'),
    # Детали погоды
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/weather/<int:weather_id>/details/',
         views.weather_details,
         name='weather_details'),
    # Удаление погоды
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/weather/<int:weather_id>/remove/',
         views.weather_remove,
         name='weather_remove'),
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
    # Погодные явления
    # Список погодных явления
    path('weather/condition/',
         views.ConditionsList.as_view(),
         name='conditions'),
    # Добавление погодного явления
    path('weather/conditions/add/',
         views.ConditionsAdd.as_view(),
         name="conditions_add"),
    # Редактирование погодного явления
    path('weather/conditions/<int:conditions_id>/edit/',
         views.ConditionsEdit.as_view(),
         name='conditions_edit'),
    # Удаление погодного явления
    path('weather/conditions/<int:conditions_id>/delete/',
         views.ConditionsDelete.as_view(),
         name='conditions_delete'),
    # Блок кормушек
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
    # Водоемы
    # Список водоемов
    path('districts/<int:district_id>/water/',
         views.water_list,
         name='water'),
    # Добавление водоема
    path('districts/<int:district_id>/water/add/',
         views.water_add,
         name='water_add'),
    # Редактирование водоема
    path('districts/<int:district_id>/water/<int:water_id>/renewal/',
         views.water_renewal,
         name='water_renewal'),
    # Удаление водоема
    path('districts/<int:district_id>/water/<int:water_id>/remove/',
         views.water_remove,
         name='water_remove'),
    # Место на водоёме
    # Список мест
    path('districts/<int:district_id>/water/<int:water_id>/place/',
         views.place_list,
         name='place'),
    # Просмотр деетальной информации о месте
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/',
         views.place_detail,
         name='place_detail'),
    # Добавление места
    path('districts/<int:district_id>/water/<int:water_id>/place/add/',
         views.place_add,
         name='place_add'),
    # Редактирование места
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/renewal/',
         views.place_renewal,
         name='place_renewal'),
    # Удаление места
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/remove/',
         views.place_remove,
         name='place_remove'),
    # Блок точек ловли
    # Список точек ловли
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/fishingpoint/',
         views.fishing_point_list,
         name='fishing_point'),
    # Добавление точки ловли
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/fishingpoint/add/',
         views.fishing_point_add,
         name='fishing_point_add'),
    # Редактирование точки ловли
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/fishingpoint/<int:fishing_point_id>/renewal/',
         views.fishing_point_renewal,
         name='fishing_point_renewal'),
    # Просмотр точки ловли
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/fishingpoint/<int:fishing_point_id>/',
         views.fishing_point_details,
         name='fishing_point_details'),
    # Удаление точки ловли
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/fishingpoint/<int:fishing_point_id>/remove/',
         views.fishing_point_remove,
         name='fishing_point_remove'),
    # Блок маркерных карт
    # Список маркерных карт
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/',
         views.bottom_map_list,
         name='bottom_map'),
    # Добавление маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/add/',
         views.bottom_map_add,
         name='bottom_map_add'),
    # Редактирование маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/renewal/',
         views.bottom_map_renewal,
         name='bottom_map_renewal'),
    # Описание маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/',
         views.bottom_map_details,
         name='bottom_map_details'),
    # Удаление маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/remove/',
         views.bottom_map_remove,
         name='bottom_map_remove'),
    # Точки маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/point/',
         views.bottom_map_point_list,
         name='point'),
    # Добавление точки маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/point/add/',
         views.bottom_map_point_add,
         name='point_add'),
    # Редактирование точки маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/point/<int:point_id>/renewal/',
         views.bottom_map_point_renewal,
         name='point_renewal'),
    # Информация о точке маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/point/<int:point_id>',
         views.bottom_map_point_details,
         name='point_details'),
    # Удаление точки маркерной карты
    path('districts/<int:district_id>/water/<int:water_id>/place/<int:place_id>/bottommap/<int:bottom_map_id>/point/<int:point_id>/remove/',
         views.bottom_map_point_remove,
         name='point_remove'),
    # Снасти
    # Список снастей
    path('tackle/',
         views.TackleList.as_view(),
         name='tackle'),
    # Добавление снасти
    path('tackle/add/',
         views.TackleAdd.as_view(),
         name='tackle_add'),
    # Редактирование снасти
    path('tackle/<int:tackle_id>/edit/',
         views.TackleEdit.as_view(),
         name='tackle_edit'),
    # Удаление снасти
    path('tackle/<int:tackle_id>/delete/',
         views.TackleDelete.as_view(),
         name='tackle_delete'),
    # Монтажи
    # Список монтажей
    path('montage/',
         views.MontageList.as_view(),
         name='montage'),
    # Добавить монтаж
    path('montage/add/',
         views.MontageAdd.as_view(),
         name='montage_add'),
    # Изменить монтаж
    path('montage/<int:montage_id>/edit/',
         views.MontageEdit.as_view(),
         name='montage_edit'),
    # Удалить монтаж
    path('montage/<int:montage_id>/delete/',
         views.MontageDelete.as_view(),
         name='montage_delete'),
    # Кормушки
    # Список кормушек
    path('trough/',
         views.TroughList.as_view(),
         name='trough'),
    # Добавление кормушки
    path('trough/add/',
         views.TroughAdd.as_view(),
         name='trough_add'),
    # Редактирование кормушки
    path('trough/<int:trough_id>/edit/',
         views.TroughEdit.as_view(),
         name='trough_edit'),
    # Удаление кормушки
    path('trough/<int:trough_id>/delete/',
         views.TroughDelete.as_view(),
         name='trough_delete'),
    # Состояние наживки
    # Добавление состояния наживки
    path('nozzle/state/add/',
         views.NozzleStateAdd.as_view(),
         name='nozzle_state_add'),
    # Редактирование состояния наживки
    path('nozzle/state/<int:nozzle_state_id>/edit/',
         views.NozzleStateEdit.as_view(),
         name='nozzle_state_edit'),
    # Удаление состояния наживки
    path('nozzle/state/<int:nozzle_state_id>/delete/',
         views.NozzleStateDelete.as_view(),
         name='nozzle_state_delete'),

    # Наживки
    # Список насадок/наживок
    path('nozzle/',
         views.NozzleBaseList.as_view(),
         name='nozzle_base'),
    # Добавление насадки
    path('nozzle/add/',
         views.NozzleBaseAdd.as_view(),
         name='nozzle_base_add'),
    # Редактирование насадки
    path('nozzle/<int:nozzle_base_id>/edit/',
         views.NozzleBaseEdit.as_view(),
         name='nozzle_base_edit'),
    # Удаление насадки
    path('nozzle/<int:nozzle_base_id>/delete/',
         views.NozzleBaseDelete.as_view(),
         name='nozzle_base_delete'),

    # Добавление наживки
    path('nozzle/add/bait/',
         views.BaitBaseAdd.as_view(),
         name='bait_base_add'),
    # Редактирование наживки
    path('nozzle/<int:bait_base_id>/bait/edit/',
         views.BaitBaseEdit.as_view(),
         name='bait_base_edit'),

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
    
    # Прикормочная смесь
    # Список прикормочных смесей
    path('fishinglure/',
         views.fishing_lure_list,
         name='fishing_lure'),
    # Добавление прикормочной смеси
    path('fishinglure/add/',
         views.fishing_lure_add,
         name='fishing_lure_add'),
    # Детали прикормочной смеси
    path('fishinglure/<int:fishing_lure_id>/details/',
         views.fishing_lure_details,
         name='fishing_lure_details'),
    # Редактирование прикормочной смеси
    path('fishinglure/<int:fishing_lure_id>/renewal/',
         views.fishing_lure_renewal,
         name='fishing_lure_renewal'),
    # Удаление прикормочной смеси
    path('fishinglure/<int:fishing_lure_id>/remove/',
         views.fishing_lure_remove,
         name='fishing_lure_remove'),
    # Прикорм
    # Список прикормов
    path('lurebase/',
         views.LureBaseList.as_view(),
         name='lure_base'),
    # Добавление прикорма
    path('lurebase/add/',
         views.LureBaseAdd.as_view(),
         name='lure_base_add'),
    # Редактирование прикорма
    path('lurebase/<int:lure_base_id>/edit/',
         views.LureBaseEdit.as_view(),
         name='lure_base_edit'),
    # Удаление прикорма
    path('lurebase/<int:lure_base_id>/delete/',
         views.LureBaseDelete.as_view(),
         name='lure_base_delete'),
    # Смеси прикорма
    # Добавление прикорма в смесь
    path('fishinglure/<int:fishing_lure_id>/lure/add/',
         views.lure_add,
         name='lure_add'),
    # Редактирование прикорма в смеси
    path('fishinglure/<int:fishing_lure_id>/lure/<int:lure_id>/renewal/',
         views.lure_renewal,
         name='lure_renewal'),
    # Удаление прикорма из смеси
    path('fishinglure/<int:fishing_lure_id>/lure/<int:lure_id>/remove/',
         views.lure_remove,
         name='lure_remove'),
    # Арома базовая
    # Список аром
    path('aromabase/',
         views.AromaBaseList.as_view(),
         name='aroma_base'),
    # Добавление аромы
    path('aromabase/add/',
         views.AromaBaseAdd.as_view(),
         name='aroma_base_add'),
    # Редактирование аромы
    path('aromabase/<int:aroma_base_id>/edit/',
         views.AromaBaseEdit.as_view(),
         name='aroma_base_edit'),
    # Удаление аромы
    path('aromabase/<int:aroma_base_id>/delete/',
         views.AromaBaseDelete.as_view(),
         name='aroma_base_delete'),
    # Аромы в прикорме
    # Добавление аромы в прикорм
    path('fishinglure/<int:fishing_lure_id>/aroma/add/',
         views.aroma_add,
         name='aroma_add'),
    # Редактирование аромы в прикорме
    path('fishinglure/<int:fishing_lure_id>/aroma/<int:aroma_id>/renewal/',
         views.aroma_renewal,
         name='aroma_renewal'),
    # Удаление аромы из приколрма
    path('fishinglure/<int:fishing_lure_id>/aroma/<int:aroma_id>/remove/',
         views.aroma_remove,
         name='aroma_remove'),
    # Крючки
    # Список крючков
    path('crochet/',
         views.CrochetList.as_view(),
         name='crochet'),
    # Добавление крючка
    path('crochet/add/',
         views.CrochetAdd.as_view(),
         name='crochet_add'),
    # Редактирование крючка
    path('crochet/<int:crochet_id>/edit/',
         views.CrochetEdit.as_view(),
         name='crochet_edit'),
    # Удаление крючка
    path('crochet/<int:crochet_id>/delete/',
         views.CrochetDelete.as_view(),
         name='crochet_delete'),
    # Поводки
    # Список поводков
    path('leash/',
         views.LeashList.as_view(),
         name='leash'),
    # Добавление поводка
    path('leash/add/',
         views.LeashAdd.as_view(),
         name='leash_add'),
    # Редактирование поводка
    path('leash/<int:leash_id>/edit/',
         views.LeashEdit.as_view(),
         name='leash_edit'),
    # Удаление поводка
    path('leash/<int:leash_id>/delete/',
         views.LeashDelete.as_view(),
         name='leash_delete'),
    # Результат рыбалки
    # Добавление результата рыбалки
    path('fishing/<int:fishing_id>/fishingresult/add/',
         views.fishing_result_add,
         name='fishing_result_add'),
    # Редактирование ррезультата рыбалки
    path('fishing/<int:fishing_id>/fishingresult/<int:fishing_result_id>/renewal/',
         views.fishing_result_renewal,
         name='fishing_result_renewal'),
    # Удаление результата рыбалки
    path('fishing/<int:fishing_id>/fishingresult/<int:fishing_result_id>/remove/',
         views.fishing_result_remove,
         name='fishing_result_remove'),
    # Трофейные уловы
    # Добавление трофейного улова
    path('fishing/<int:fishing_id>/fishtrophy/add/',
         views.fish_trophy_add,
         name='fish_trophy_add'),
    # Редактирование трофейного улова
    path('fishing/<int:fishing_id>/fishtrophy/<int:fish_trophy_id>/renewal/',
         views.fish_trophy_renewal,
         name='fish_trophy_renewal'),
    # Удаление трофейного улова
    path('fishing/<int:fishing_id>/fishtrophy/<int:fish_trophy_id>/remove/',
         views.fish_trophy_remove,
         name='fish_trophy_remove'),
    # Место рыбалки
    # Добавление места рыбалки
    path('fishing/<int:fishing_id>/placefishing/select/',
         views.place_fishing_select,
         name='place_fishing_select'),
    # Добавление и изменение места рыбалки
    path('fishing/<int:fishing_id>/placefishing/<int:place_id>/add/',
         views.place_fishing_add,
         name='place_fishing_add'),
    # Удаление места рыбалки
    path('fishing/<int:fishing_id>/placefishing/<int:place_fishing_id>/remove/',
         views.place_fishing_remove,
         name='place_fishing_remove'),
    # Снасть использованная в рыбалке
    # Добавпить снасть в рыбалку
    path('fishing/<int:fishing_id>/fishingtackle/<int:tackle_id>/add/<int:fishing_tackle_id>/',
         views.fishing_tackle_add,
         name='fishing_tackle_add'),
    # Выбор снасти для рыбалки
    path('fishing/<int:fishing_id>/fishingtackle/select/<int:fishing_tackle_id>/',
         views.fishing_tackle_select,
         name='fishing_tackle_select'),
    # Удалить снасть в рыбалке
    path('fishing/<int:fishing_id>/fishingtackle/<int:fishing_tackle_id>/remove/',
         views.fishing_tackle_remove,
         name='fishing_tackle_remove'),
    # Монтаж использованный в рыбалке
    # Добавить/изменить мотаж в использованный в рыбалке
    path('fishing/<int:fishing_id>/fishingmontage/<int:fishing_tackle_id><int:montage_id>/add/<int:fishing_montage_id>/',
         views.fishing_montage_add,
         name='fishing_montage_add'),
    # Удалить монтаж использованнй в рыбалке
    path('fishing/<int:fishing_id>/fishingmontage/<int:fishing_montage_id>/remove/',
         views.fishing_montage_remove,
         name='fishing_montage_remove'),
    # Выбрать монтаж использованный в рыбалке
    path('fishing/<int:fishing_id>/fishingmontage/select/<int:fishing_tackle_id><int:fishing_montage_id>/',
         views.fishing_montage_select,
         name='fishing_montage_select'),
    # Кормушки использованные в рыбалке
    # Добавить кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/<int:fishing_tackle_id><int:trough_id>/add/<int:fishing_trough_id>/',
         views.fishing_trough_add,
         name='fishing_trough_add'),
    # Удалить кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/<int:fishing_trough_id>/remove/',
         views.fishing_trough_remove,
         name='fishing_trough_remove'),
    # Выбрать кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/select/<int:fishing_tackle_id><int:fishing_trough_id>/',
         views.fishing_trough_select,
         name='fishing_trough_select'),
    # Поводки использованные в рыбалке
    # Добавление поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/<int:fishing_tackle_id><int:leash_id>/add/<int:fishing_leash_id>/',
         views.fishing_leash_add,
         name='fishing_leash_add'),
    # Удаление поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/<int:fishing_leash_id>/remove/',
         views.fishing_leash_remove,
         name='fishing_leash_remove'),
    # Выбор поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/select/<int:fishing_tackle_id><int:fishing_leash_id>/',
         views.fishing_leash_select,
         name='fishing_leash_select'),
    # Крючки использованные в рыбалке
    # Добавить крючок в рыбалку
    path('fishing/<int:fishing_id>/fishingcrochet/<int:fishing_tackle_id><int:crochet_id>/add/<int:fishing_crochet_id>/',
         views.FishingCrochetViews.as_view(),
         name='fishing_crochet_add'),
    # Удалить крючек из рыбалки
    path('fishing/<int:fishing_id>/fishingcrochet/<int:fishing_crochet_id>/remove/',
         views.FishingCrochetDelete.as_view(),
         name='fishing_crochet_remove'),
    # Выбрать крючок в рыбалке
    path('fishing/<int:fishing_id>/fishingcrochet/select/<int:fishing_tackle_id><int:fishing_crochet_id>/',
         views.FishingCrochetViews.as_view(),
         name='fishing_crochet_select'),
    # Насадки/наживки использованные в рыбалке\
    # Добавить наживку в рыбалку
    path('fishing/<int:fishing_id>/fishingnozzle/<int:fishing_tackle_id><int:nozzle_id>/add/<int:fishing_nozzle_id>/',
         views.FishingNozzleViews.as_view(),
         name='fishing_nozzle_add'),
    # Удалить наживку/насадку из рыбалки
    path('fishing/<int:fishing_id>/fishingnozzle/<int:fishing_nozzle_id>/remove/',
         views.FishingNozzleDelete.as_view(),
         name='fishing_nozzle_remove'),
    # Выбрать насадку/наживку для рыбалки
    path('fishing/<int:fishing_id>/fishingnozzle/select/<int:fishing_tackle_id><int:fishing_nozzle_id>/',
         views.FishingNozzleViews.as_view(),
         name='fishing_nozzle_select'),
    # Темп рыбалки
    # Добаввить темп рыбалки
    path('fishing/<int:fishing_id>/fishingpace/<int:fishing_tackle_id><int:pace_id>/add/<int:fishing_pace_id>/',
         views.FishingPaceViews.as_view(),
         name='fishing_pace_add'),
    # Убрать темп рыбалки
    path('fishing/<int:fishing_id>/fishingpace/<int:fishing_pace_id>/remove/',
         views.FishingPaceDelete.as_view(),
         name='fishing_pace_remove'),
    # Выбрать темп рыбалки
    path('fishing/<int:fishing_id>/fishingpace/select/<int:fishing_tackle_id><int:fishing_pace_id>/',
         views.FishingPaceViews.as_view(),
         name='fishing_pace_select'),
    # Погода на рыбалке
    # Добавить погоду на рыбалке
    path('fishing/<int:fishing_id>/fishingweather/<int:weather_id>/add/<int:fishing_weather_id>/',
         views.FishingWeatherViews.as_view(),
         name='fishing_weather_add'),
    # Удалить погоду на рыбалке
    path('fishing/<int:fishing_id>/fishingweather/<int:fishing_weather_id>/remove/',
         views.FishingWeatherDelete.as_view(),
         name='fishing_weather_remove'),
    # Выбрать погоду на рыбалке
    path('fishing/<int:fishing_id>/fishingweather/select/<int:fishing_weather_id>/',
         views.FishingWeatherViews.as_view(),
         name='fishing_weather_select'),
    # Прикормочная смесь для рыбалки
    # Добавить прикормочную смесь
    path('fishing/<int:fishing_id>/fishinglure/<int:lure_mix_id>/add/<int:fishing_lure_id>/',
         views.FishingLureViews.as_view(),
         name='fishing_lure_add'),
    # Удалить прикормочную смесь
    path('fishing/<int:fishing_id>/fishinglure/<int:fishing_lure_id>/remove/',
         views.FishingLureDelete.as_view(),
         name='fishing_lure_remove'),
    # Выбрать прикормочную смесь
    path('fishing/<int:fishing_id>/fishinglure/select/<int:fishing_lure_id>/',
         views.FishingLureViews.as_view(),
         name='fishing_lure_select'),
    # Новая прикормочная смесь из выбора смеси
    path('fishing/<int:fishing_id>/fishinglure/add/<int:fishing_lure_id>/',
         views.LureMixNewAddInFishingLure.as_view(),
         name='lure_mix_in_fishing_lure'),
    # Прикорм в миксе
    # Добавить прикорм в микс
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/lure/<int:lure_base_id>/select/',
         views.LureInLureMixViews.as_view(),
         name='lure_in_lure_mix_select'),
    # Удалить прикорм из микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/lure/<int:lure_id>/remove/',
         views.LureInLureMixDelete.as_view(),
         name='lure_in_lure_mix_remove'),
    # Список прикормов для микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/lure/',
         views.LureInLureMixSelect.as_view(),
         name='lure_in_lure_mix'),
    # Арома в миксе
    # Добавить арому в микс
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/aroma/<int:aroma_base_id>/select/',
         views.AromaInLureMixViews.as_view(),
         name='aroma_in_lure_mix_select'),
    # Удалить арому из микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/aroma/<int:aroma_id>/remove/',
         views.AromaInLureMixDelete.as_view(),
         name='aroma_in_lure_mix_remove'),
    # Список арому для микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/aroma/',
         views.AromaInLureMixSelect.as_view(),
         name='aroma_in_lure_mix'),
    # Добавки в миксе
    # Добавить добавки в микс
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/nozzle/<int:nozzle_base_id>/select/',
         views.NozzleInLureMixViews.as_view(),
         name='nozzle_in_lure_mix_select'),
    # Удалить добавки из микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/nozzle/<int:nozzle_id>/remove/',
         views.NozzleInLureMixDelete.as_view(),
         name='nozzle_in_lure_mix_remove'),
    # Список добавки для микса
    path('fishing/<int:fishing_id>/mix/<int:lure_mix_id>/nozzle/',
         views.NozzleInLureMixSelect.as_view(),
         name='nozzle_in_lure_mix'),
    
]

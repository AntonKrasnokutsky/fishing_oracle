from django.urls import path
from . import views
from .views import FishingCrochetViews

app_name = 'fishing'
urlpatterns = [
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
         views.fishing_add,
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
         views.fish_list,
         name='fish'),
    # Описание рыбы
    path('fish/<int:fish_id>/',
         views.fish_details,
         name='fish_details'),
    # Редактирование названия рыбы и описания
    path('fish/<int:fish_id>/renewal/',
         views.fish_renewal,
         name="fish_renewal"),
    # Добавление рыбы
    path('fish/add/',
         views.fish_add,
         name='fish_add'),
    # Удаление рыбы
    path('fish/<int:fish_id>/remove/',
         views.fish_remove,
         name='fish_remove'),
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
         views.priming_list,
         name='primings'),
    # Добавление грунта
    path('primings/add/',
         views.priming_add,
         name='priming_add'),
    # Редактирование грунта
    path('primings/<int:priming_id>/renewal/',
         views.priming_renewal,
         name='priming_renewal'),
    # Удаление грунта
    path('primings/<int:priming_id>/remove',
         views.priming_remove,
         name='priming_remove'),
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
    path('weather/overcast/',
         views.overcast_list,
         name='overcast'),
    # Добавдение варианта облачности
    path('weather/overcast/add/',
         views.overcast_add,
         name='overcast_add'),
    # Редактирование варианта облачности
    path('weather/overcast/<int:overcast_id>/renewal/',
         views.overcast_renewal,
         name='overcast_renewal'),
    # Удаление варианта облачности
    path('weather/overcast/<int:overcast_id>/remove/',
         views.overcast_remove,
         name='overcast_remove'),
    # Погодные явления
    # Список погодных явления
    path('weather/phenomena/',
         views.weather_phenomenas_list,
         name='weatherphenomena'),
    # Добавление погодного явления
    path('weather/phenomena/add/',
         views.weather_phenomenas_add,
         name="weatherphenomena_add"),
    # Редактирование погодного явления
    path('weather/phenomena/<int:phenomena_id>/renewal/',
         views.weather_phenomenas_renewal,
         name='weatherphenomena_renewal'),
    # Удаление погодного явления
    path('weather/phenomena/<int:phenomena_id>/remove/',
         views.weather_phenomenas_remove,
         name='weatherphenomena_remove'),
    # Блок кормушек
    # Кормоемкость
    # Списк вариантов кормоемкости
    path('capacity/',
         views.feed_capacity_list,
         name='feed_capacity'),
    # Добавление варианта кормоемкости
    path('capacity/add/',
         views.feed_capacity_add,
         name='feed_capacity_add'),
    # Редактирование варианта кормоемскости
    path('capacity/<int:feed_capacity_id>/renewal/',
         views.feed_capacity_renewal,
         name='feed_capacity_renewal'),
    # Удаление варианта кормоемкости
    path('capacity/<int:feed_capacity_id>/remove/',
         views.feed_capacity_remove,
         name='feed_capacity_remove'),
    # Темп
    # Список вариантов таблицы Темп
    path('pace/',
         views.pace_list,
         name='pace'),
    # Добавление варианта темпа
    path('pace/add/',
         views.pace_add, name='pace_add'),
    # Редактирование варианта темпа
    path('pace/<int:pace_id>/renewal',
         views.pace_renewal,
         name='pace_renewal'),
    # Удаление варианта темпа
    path('pace/<int:pace_int>/remove/',
         views.pace_remove,
         name='pace_remove'),
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
         views.tackle_list,
         name='tackle'),
    # Добавление снасти
    path('tackle/add/',
         views.tackle_add,
         name='tackle_add'),
    # Редактирование снасти
    path('tackle/<int:tackle_id>/renewal/',
         views.tackle_renewal,
         name='tackle_renewal'),
    # Удаление снасти
    path('tackle/<int:tackle_id>/remove/',
         views.tackle_remove,
         name='tackle_remove'),
    # Монтажи
    # Список монтажей
    path('montage/',
         views.montage_list,
         name='montage'),
    # Добавить монтаж
    path('montage/add/',
         views.montage_add,
         name='montage_add'),
    # Изменить монтаж
    path('montage/<int:montage_id>/renewal/',
         views.montage_renewal,
         name='montage_renewal'),
    # Удалить монтаж
    path('montage/<int:montage_id>/remove/',
         views.montage_remove,
         name='montage_remove'),
    # Названия моделей кормушек
    # Список названий моделей кормушек
    path('modeltroughname/',
         views.model_trough_name_list,
         name='model_trough_name'),
    # Добавление названия модели кормушек
    path('modeltroughname/add/',
         views.model_trough_name_add,
         name='model_trough_name_add'),
    # Редактирование названия модели кормушек
    path('modeltroughname/<int:model_trough_name_id>/renewal/',
         views.model_trough_name_renewal,
         name='model_trough_name_renewal'),
    # Удаление названия моделей кормушек
    path('modeltroughname/<int:model_trough_name_id>/remove/',
         views.model_trough_name_remove,
         name='model_trough_name_remove'),
    # Комбинации моделей кормушек
    # Список комбинаций моделей кормушек
    path('modeltrough/',
         views.model_trough_list,
         name='model_trough'),
    # Добавлении комбинации модели кормушек
    path('modeltrough/add/',
         views.model_trough_add,
         name='model_trough_add'),
    # Редактирование комбинация моделей кормушек
    path('modeltrough/<int:model_trough_id>/renewal/',
         views.model_trough_renewal,
         name='model_trough_renewal'),
    # Удаление комбинаций моделей кормушек
    path('modeltrough/<int:model_trough_id>/remove/',
         views.model_trough_remove,
         name='model_trough_remove'),
    # Кормушки
    # Список кормушек
    path('trough/',
         views.trough_list,
         name='trough'),
    # Добавление кормушки
    path('trough/add/',
         views.trough_add,
         name='trough_add'),
    # Редактирование кормушки
    path('trough/<int:trough_id>/renewal/',
         views.trough_renewal,
         name='trough_renewal'),
    # Удаление кормушки
    path('trough/<int:trough_id>/remove/',
         views.trough_remove,
         name='trough_remove'),
    # Состояние наживки
    # Список состояний наживки
    path('nozzlestate/',
         views.nozzle_state_list,
         name='nozzle_state'),
    # Добавление состояния наживки
    path('nozzlestate/add/',
         views.nozzle_state_add,
         name='nozzle_state_add'),
    # Редактирование состояния наживки
    path('nozzlestate/<int:nozzle_state_id>/renewal/',
         views.nozzle_state_renewal,
         name='nozzle_state_renewal'),
    # Удаление состояния наживки
    path('nozzlestate/<int:nozzle_state_id>/remove/',
         views.nozzle_state_remove,
         name='nozzle_state_remove'),
    # Наживки
    # Список наживок
    path('nozzle/',
         views.nozzle_list,
         name='nozzle'),
    # Описание наживки
    path('nozzle/<int:nozzle_id>/details/',
         views.nozzle_details,
         name='nozzle_details'),
    # Добавление наживки
    path('nozzle/add/',
         views.nozzle_add,
         name='nozzle_add'),
    # Редактирование наживки
    path('nozzle/<int:nozzle_id>/renewal/',
         views.nozzle_renewal,
         name='nozzle_renewal'),
    # Удаление наживки
    path('nozzle/<int:nozzle_id>/remove/',
         views.nozzle_remove,
         name='nozzle_remove'),
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
         views.lure_base_list,
         name='lure_base'),
    # Добавление прикорма
    path('lurebase/add/',
         views.lure_base_add,
         name='lure_base_add'),
    # Редактирование прикорма
    path('lurebase/<int:lure_base_id>/renewal/',
         views.lure_base_renewal,
         name='lure_base_renewal'),
    # Удаление прикорма
    path('lurebase/<int:lure_base_id>/remove/',
         views.lure_base_remove,
         name='lure_base_remove'),
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
         views.aroma_base_list,
         name='aroma_base'),
    # Добавление аромы
    path('aromabase/add/',
         views.aroma_base_add,
         name='aroma_base_add'),
    # Редактирование аромы
    path('aromabase/<int:aroma_base_id>/renewal/',
         views.aroma_base_renewal,
         name='aroma_base_renewal'),
    # Удаление аромы
    path('aromabase/<int:aroma_base_id>/remove/',
         views.aroma_base_remove,
         name='aroma_base_remove'),
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
         views.crochet_list,
         name='crochet'),
    # Добавление крючка
    path('crochet/add/',
         views.crochet_add,
         name='crochet_add'),
    # Редактирование крючка
    path('crochet/<int:crochet_id>/renewal/',
         views.crochet_renewal,
         name='crochet_renewal'),
    # Удаление крючка
    path('crochet/<int:crochet_id>/remove/',
         views.crochet_remove,
         name='crochet_remove'),
    # Поводки
    # Список поводков
    path('leash/',
         views.leash_list,
         name='leash'),
    # Добавление поводка
    path('leash/add/',
         views.leash_add,
         name='leash_add'),
    # Редактирование поводка
    path('leash/<int:leash_id>/renewal/',
         views.leash_renewal,
         name='leash_renewal'),
    # Удаление поводка
    path('leash/<int:leash_id>/remove/',
         views.leash_remove,
         name='leash_remove'),
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
    path('fishing/<int:fishing_id>/fishingmontage/<int:montage_id>/add/<int:fishing_montage_id>/',
         views.fishing_montage_add,
         name='fishing_montage_add'),
    # Удалить монтаж использованнй в рыбалке
    path('fishing/<int:fishing_id>/fishingmontage/<int:fishing_montage_id>/remove/',
         views.fishing_montage_remove,
         name='fishing_montage_remove'),
    # Выбрать монтаж использованный в рыбалке
    path('fishing/<int:fishing_id>/fishingmontage/select/<int:fishing_montage_id>/',
         views.fishing_montage_select,
         name='fishing_montage_select'),
    #Кормушки использованные в рыбалке
    #Добавить кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/<int:trough_id>/add/<int:fishing_trough_id>/',
         views.fishing_trough_add,
         name='fishing_trough_add'),
    #Удалить кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/<int:fishing_trough_id>/remove/',
         views.fishing_trough_remove,
         name='fishing_trough_remove'),
    #Выбрать кормушку использованную в рыбалке
    path('fishing/<int:fishing_id>/fishingtrough/select/<int:fishing_trough_id>/',
         views.fishing_trough_select,
         name='fishing_trough_select'),
    #Поводки использованные в рыбалке
    #Добавление поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/<int:leash_id>/add/<int:fishing_leash_id>/',
         views.fishing_leash_add,
         name='fishing_leash_add'),
    #Удаление поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/<int:fishing_leash_id>/remove/',
         views.fishing_leash_remove,
         name='fishing_leash_remove'),
    #Выбор поводка использованного в рыбалке
    path('fishing/<int:fishing_id>/fishingleash/select/<int:fishing_leash_id>/',
         views.fishing_leash_select,
         name='fishing_leash_select'),
    #Крючки использованные в рыбалке
    #Добавить крючок в рыбалку
    path('fishing/<int:fishing_id>/fishingcrochet/<int:crochet_id>/add/<int:fishing_crochet_id>/',
         FishingCrochetViews.as_view(),
         name='fishing_crochet_add'),
    #Удалть крючек из рыбалки
    path('fishing/<int:fishing_id>/fishingcrochet/<int:fishing_crochet_id>/remove/',
         views.FishingCrochetDelete.as_view(),
         name='fishing_crochet_remove'),
    #Выбрать крючок в рыбалке
    path('fishing/<int:fishing_id>/fishingcrochet/select/<int:fishing_crochet_id>/',
         FishingCrochetViews.as_view(),
         name='fishing_crochet_select'),
]

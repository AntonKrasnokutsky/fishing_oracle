from django.urls import path
from . import views

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
    path('fishing/<int:fishing_id>/',
         views.fishing_detail,
         name='detail'),
    # Добавление рыбалки
    path('add/',
         views.fishing_add,
         name='fishing_add'),
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
    path('fishingtackle/',
         views.fishing_tackle_list,
         name='fishing_tackle'),
    # Добавление снасти
    path('fishingtackle/add/',
         views.fishing_tackle_add,
         name='fishing_tackle_add'),
    # Редактирование снасти
    path('fishingtackle/<int:fishing_tackle_id>/renewal/',
         views.fishing_tackle_renewal,
         name='fishing_tackle_renewal'),
    # Удаление снасти
    path('fishingtackle/<int:fishing_tackle_id>/remove/',
         views.fishing_tackle_remove,
         name='fishing_tackle_remove'),
    # Монтажи
    # Список монтажей
    path('fishingmontage/',
         views.fishing_montage_list,
         name='fishing_montage'),
    # Добавить монтаж
    path('fishingmontage/add/',
         views.fishing_montage_add,
         name='fishing_montage_add'),
    # Изменить монтаж
    path('fishingmontage/<int:fishing_montage_id>/renewal/',
         views.fishing_montage_renewal,
         name='fishing_montage_renewal'),
    # Удалить монтаж
    path('fishingmontage/<int:fishing_montage_id>/remove/',
         views.fishing_montage_remove,
         name='fishing_montage_remove'),
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
    path('fishingtrough/',
         views.fishing_trough_list,
         name='fishing_trough'),
    # Добавление кормушки
    path('fishingtrough/add/',
         views.fishing_trough_add,
         name='fishing_trough_add'),
    # Редактирование кормушки
    path('fishingtrough/<int:fishing_trough_id>/renewal/',
         views.fishing_trough_renewal,
         name='fishing_trough_renewal'),
    # Удаление кормушки
    path('fishingtrough/<int:fishing_trough_id>/remove/',
         views.fishing_trough_remove,
         name='fishing_trough_remove'),
]

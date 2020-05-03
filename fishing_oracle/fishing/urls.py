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
    path('fish/<int:fish_id>',
         views.fish_details,
         name='fish_details'),
    # Редактирование названия рыбы и описания
    path('fish/renewal/<int:fish_id>/',
         views.fish_renewal,
         name="fish_renewal"),
    # Добавление рыбы
    path('fish/add/',
         views.fish_add,
         name='fish_add'),
    # Удаление рыбы
    path('fish/remove/<int:fish_id>/',
         views.fish_remove,
         name='fish_remove'),
    # Блок Районов
    # Список районов
    path('districts/',
         views.district_list,
         name='districts'),
    # Добавление района
    path('districts/add',
         views.district_add,
         name='district_add'),
    # Редактирование района
    path('district/renewal/<int:district_id>/',
         views.district_renewal,
         name='district_renewal'),
    # Удаление района
    path('districts/remove/<int:district_id>/',
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
    path('primings/renewal/<int:priming_id>',
         views.priming_renewal,
         name='priming_renewal'),
    # Удаление грунта
    path('primings/remove/<int:priming_id>',
         views.priming_remove,
         name='priming_remove'),
    # Блок погоды
    # Облачность
    # Список вариантов облачности
    path('overcast/',
         views.overcast_list,
         name='overcast'),
    # Добавдение варианта облачности
    path('overcast/add/',
         views.overcast_add,
         name='overcast_add'),
    # Редактирование варианта облачности
    path('overcast/renewal/<int:overcast_id>',
         views.overcast_renewal,
         name='overcast_renewal'),
    # Удаление варианта облачности
    path('overcast/remove/<int:overcast_id>',
         views.overcast_remove,
         name='overcast_remove'),
    # Погодные явления
    # Список погодных явления
    path('phenomena/',
         views.weather_phenomenas_list,
         name='weatherphenomena'),
    # Добавление погодного явления
    path('phenomena/add',
         views.weather_phenomenas_add,
         name="weatherphenomena_add"),
    # Редактирование погодного явления
    path('phenomena/renewal/<int:phenomena_id>',
         views.weather_phenomenas_renewal,
         name='weatherphenomena_renewal'),
    # Удаление погодного явления
    path('phenomena/remove/<int:phenomena_id>',
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
    path('capacity/renewal/<int:feed_capacity_id>',
         views.feed_capacity_renewal,
         name='feed_capacity_renewal'),
    # Удаление варианта кормоемкости
    path('capacity/remove/<int:feed_capacity_id>',
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
    path('pace/renewal/<int:pace_id>',
         views.pace_renewal,
         name='pace_renewal'),
    # Удаление варианта темпа
    path('pace/remove/<int:pace_int>',
         views.pace_remove,
         name='pace_remove'),
    # Водоемы
    # Список водоемов
    path('district/water/<int:district_id>',
         views.water_list,
         name='water'),
    # Добавление водоема
    path('water/add',
         views.water_add,
         name='water_add'),
    # Редактирование водоема
    path('water/renewal/<int:water_id>',
         views.water_renewal,
         name='water_renewal'),
    # Удаление водоема
    path('water/remove/<int:water_id>',
         views.water_remove,
         name='water_remove'),
]

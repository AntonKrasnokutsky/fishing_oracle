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
]

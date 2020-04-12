from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Fishing(models.Model):
    """
    Содержит всю информацию о рыбалке
    """
    class Meta:
        verbose_name = "Рыбалка"
        verbose_name_plural = "Рыбалки"
    # Дата проведения рыбалки
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата рыбалки")
    # Время начала рыбалки
    time = models.TimeField(
        auto_now_add=True,
        verbose_name="Время начала")
    # Место проведения рыбалки
    place = models.ForeignKey(
        'Place',
        on_delete=models.PROTECT,
        verbose_name="Место рыбалки")
    # Погода
    weather = models.ForeignKey(
        'Weather',
        on_delete=models.PROTECT,
        verbose_name="Погода")
    # Снасть
    fishing_tackle = models.ForeignKey(
        'Fishing_Tackle',
        on_delete=models.PROTECT,
        verbose_name="Снасть")
    # Монтаж
    fishing_montage = models.ForeignKey(
        'Fishing_Montage',
        on_delete=models.PROTECT,
        verbose_name="Монтаж")
    # Используемая кормушка
    fishing_trough = models.ForeignKey(
        'Fishing_Trough',
        on_delete=models.PROTECT,
        verbose_name="Кормушка")
    # Прикормочная смесь
    fishing_lure = models.ForeignKey(
        'Fishing_Lure',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Арома
    aroma = models.ForeignKey(
        'Aroma',
        on_delete=models.PROTECT,
        verbose_name="Арома")
    # Поводок
    fishing_leash = models.ForeignKey(
        'Fishing_Leash',
        on_delete=models.PROTECT,
        verbose_name='Поводок')
    # Крючек
    crochet = models.ForeignKey(
        'Crochet',
        on_delete=models.PROTECT,
        verbose_name="Крючек")
    # Наживка/насадка
    nozzle = models.ForeignKey(
        'Nozzle',
        on_delete=models.PROTECT,
        verbose_name="Наживка/насадка")
    # Темп
    pace = models.ForeignKey(
        'Pace',
        on_delete=models.PROTECT,
        verbose_name="Темп")
    # Результат рыбалки
    # Трофей


class Fish(models.Model):
    """
    Таблица хранящая в себе информацию о породах рыб,
    в дальнейшем планируется добавление изображение рыб
    """
    # Название рыбы https://gdekluet.ru/directory/fish/
    name_of_fish = models.CharField(
        max_length=20,
        verbose_name="Рыба")
    fish_description = models.TextField(
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Рыба"
        verbose_name_plural = "Рыбы"

    def __str__(self):
        return self.name_of_fish


class Place(models.Model):
    """
    Содержит информацию о месте рыбалки
    """
    class Meta:
        verbose_name = "Место рыбалки"
        verbose_name_plural = "Места рыбалок"
    # Привязка к водоему
    water = models.ForeignKey(
        'Water',
        on_delete=models.PROTECT,
        verbose_name="Водоем")
    # Близайший населенный пункт
    place_locality = models.CharField(
        max_length=50,
        verbose_name="Начеленный пункт")
    # Карта дна

    # Координа места рыбалки, градусы северной широты от -90 до 90
    place_northern_degree = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ],
        verbose_name="N° (-90 до 90)")
    # Координа места рыбалки, минуты северной широты от 0 до 60
    place_northern_minute = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ],
        verbose_name="N' (0 до 59)")
    # Координа места рыбалки, секунты северной широты с тысячными долями
    # Дпустимые значения от 0 до 60
    place_northern_second = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0,
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ],
        verbose_name='N" (0 до 59.999)')
    # Координа места рыбалки, градусы восточной долготы от -180 до 180
    place_easter_degree = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ],
        verbose_name="E° (-180 до 180)")
    # Координа места рыбалки, минуты восточной долготы от 0 до 60
    place_easter_minute = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ],
        verbose_name="E' (0 до 59)")
    # Координа места рыбалки, секунты восточной долготы с тысячными долями
    # Дпустимые значения от 0 до 60
    place_easter_second = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0,
        validators=[
            MaxValueValidator(59.999),
            MinValueValidator(0)
        ],
        verbose_name='E" (0 до 59.999)')
    # Точка ловли
    fishing_point = models.ForeignKey(
        'Fishing_Point',
        on_delete=models.PROTECT,
        verbose_name="Точка ловли"
    )
    # Фотография места рыбалки
    # photo_place=models.ImageField(
    #     verbose_name="Места")


class Bottom_Map(models.Model):
    """
    Содержит информацию о маркерной карте, включает в себя
    координаты базовой точки, и привязку всех маркерных точек
    (в одельной таблице)
    """
    # Привязка к водоему
    class Meta:
        verbose_name = "Карта дна"
        verbose_name_plural = "Карты дна"
    water = models.OneToOneField(
        'Water',
        on_delete=models.CASCADE,
        verbose_name="Водоем")
    # Координа базовой точки, градусы северной широты от -90 до 90
    bottom_map_northern_degree = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(90),
            MinValueValidator(-90)
        ],
        verbose_name="N° (-90 до 90)")
    # Координа базовой точки, минуты северной широты от 0 до 60
    bottom_map_northern_minute = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ],
        verbose_name="N' (0 до 59)")
    # Координа базовой точки, секунты северной широты с тысячными долями
    # Дпустимые значения от 0 до 60
    bottom_map_northern_second = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0,
        validators=[
            MaxValueValidator(59.999),
            MinValueValidator(0)
        ],
        verbose_name='N" (0 до 59.999)')
    # Координа базовой точки, градусы восточной долготы от -180 до 180
    bottom_map_easter_degree = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(180),
            MinValueValidator(-180)
        ],
        verbose_name="E° (-180 до 180)")
    # Координа базовой точки, минуты восточной долготы от 0 до 60
    bottom_map_easter_minute = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(59),
            MinValueValidator(0)
        ],
        verbose_name="E' (0 до 59)")
    # Координа базовой точки, секунты восточной долготы с тысячными долями
    # Дпустимые значения от 0 до 60
    bottom_map_easter_second = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        default=0,
        validators=[
            MaxValueValidator(59.999),
            MinValueValidator(0)
        ],
        verbose_name='E" (0 до 59.999)')
    # Фотография места
    # bottom_map_photo=models.ImageField()


class Point(models.Model):
    """
    Содержит информацию о маркерной точке, привязывается
    к маркерной карте. Информация о грунте возмоно выбор
    из списка
    """
    class Meta:
        verbose_name = "Точка карты дна"
        verbose_name_plural = "Точки карт дна"
    # Привязка к маркерной карте
    bottom_map = models.OneToOneField(
        'Bottom_Map',
        on_delete=models.CASCADE,
        verbose_name="Карта дна")
    # Азимут луча (по компасу)
    point_azimuth = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(359),
            MinValueValidator(0)
        ],
        verbose_name="Азимут")
    # Дистанций до точки
    point_distance = models.PositiveIntegerField(
        default=0,
        verbose_name="Дистанция")
    # Глубина в точке
    point_depth = models.PositiveIntegerField(
        default=0,
        verbose_name="Глубина")
    # Грунт
    priming = models.ForeignKey(
        'Priming',
        on_delete=models.PROTECT,
        verbose_name="Грунт")


class Fishing_Point(models.Model):
    """
    Содежит информацию о точке ловли, возможно использование
    в нескольких рыбалках
    """
    class Meta:
        verbose_name = "Точка ловли"
        verbose_name_plural = "Точки ловли"
    # Азимут заброса
    fishing_point_azimuth = models.PositiveIntegerField(
        default=0,
        verbose_name="Азимут")
    # Дистанция до точки ловли
    fishing_point_distance = models.PositiveIntegerField(
        default=0,
        verbose_name="Дистанция")
    # Глубина в точке ловли
    fishing_poiny_depth = models.PositiveIntegerField(
        default=0,
        verbose_name="Глубина")
    # Грунт в точке ловли
    priming = models.ForeignKey(
        'Priming',
        on_delete=models.PROTECT,
        verbose_name="Грунт"
    )


class Priming(models.Model):
    """
    Содержит варианты дна, например ил, камень, песок и т.д.
    Возможно отказаться от таблицы, т.к. варианты можно выбить из списка
    """
    class Meta:
        verbose_name = "Покрытие дна"
        verbose_name_plural = "Покрытие дна"
    # Наименование покрытия дна
    priming_name = models.CharField(
        max_length=50,
        verbose_name="Грунт")

    def __str__(self):
        return self.priming_name


class Weather(models.Model):
    """
    Содержит сводные сведения о погоде
    опираясь на ручной ввод
    """
    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"
    # Облачность
    overcast = models.ForeignKey(
        'Overcast',
        on_delete=models.PROTECT,
        verbose_name="Облачность")
    # Связь с таблицей "Явления погоды"
    weather_phenomena = models.ForeignKey(
        'Weather_Phenomena',
        on_delete=models.PROTECT,
        verbose_name="Явления погоды")
    # Температура воздуха
    weather_temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0,
        verbose_name="Температура воздуха")
    # Давление
    pressure = models.PositiveIntegerField(
        default=760,
        verbose_name="Давление")
    # Направление ветра
    direction_wind = models.CharField(
        max_length=30,
        verbose_name="Направление ветра")
    # Скорость ветра
    wind_speed = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0,
        verbose_name="Скорость ветра")
    # Лунный день
    lunar_day = models.PositiveIntegerField(
        default=0,
        verbose_name="Лунный день")


class Overcast(models.Model):
    """
    Содержит варианты облочности для блока 'Погода'
    """
    class Meta:
        verbose_name = "Облачность"
        verbose_name_plural = "Облачность"
    #
    overcast_name = models.CharField(
        max_length=20,
        verbose_name="Классификация облачности")


class Weather_Phenomena(models.Model):
    """
    Явления погоды, возможно несколько записей
    для одного выезда
    """
    class Meta:
        verbose_name = "Погодное явление"
        verbose_name_plural = "Погодные явления"

    # Погодные явления
    weather_phenomena_name = models.CharField(
        max_length=20,
        verbose_name="Погодные явления")


class Fishing_Tackle(models.Model):
    """
    Содержит информацию о снасти: донная, поплавочная и т.д.
    """
    class Meta:
        verbose_name = "Рыболовная снасть"
        verbose_name_plural = "Рыболовные снасти"
    # Инормация о используемой снасти
    fishing_tackle_name = models.CharField(
        max_length=30,
        verbose_name="Снасть")


class Fishing_Montage(models.Model):
    """
    Содержит в себе варианты монтажей с вариантом выбора
    скользящего
    """
    # Вариант монтажа
    fishing_montage_name = models.CharField(
        max_length=15,
        verbose_name="Монтаж")
    # Скользащий да или нет
    fishing_montage_sliding = models.BooleanField(
        default=False,
        verbose_name="Скользящий монтаж")

    class Meta:
        verbose_name = "Монтаж"
        verbose_name_plural = "Монтажи"


class Fishing_Trough(models.Model):
    """
    Содержит информацию о кормушках
    """
    # Производитель кормушки
    fishing_trough_manufacturer = models.CharField(
        max_length=50,
        verbose_name="Поизводитель")
    # Связь с таблицей модели кормушки
    model_trough = models.ForeignKey(
        'Model_Trough',
        on_delete=models.PROTECT,
        verbose_name="Модель кормушки")
    # Связь с таблицей кормоемкости
    feed_capacity = models.ForeignKey(
        'Feed_Capacity',
        on_delete=models.PROTECT,
        verbose_name="Кормоёмкость")
    # Вес кормушки
    fishing_trough_weight = models.PositiveIntegerField(
        default=0,
        verbose_name="Вес кормушки"
    )

    class Meta:
        verbose_name = "Рыболовная кормушка"
        verbose_name_plural = "Рыболовные кормушки"


class Model_Trough(models.Model):
    """
    Содержит комбинации моделей кормушек
    """
    # Связь со списком моделей
    model_trough_name = models.ForeignKey(
        'Model_Trough_Name',
        on_delete=models.PROTECT,
        verbose_name="Модель кормушки")
    # Метка пластиковй кормушки
    model_trough_plastic = models.BooleanField(
        default=False,
        verbose_name="Пластик")
    # Метка наличия грунтозацепов
    model_trough_lugs = models.BooleanField(
        default=False,
        verbose_name="грунтозацепы")

    class Meta:
        verbose_name = "Модель кормушки"
        verbose_name_plural = "Модели кормушек"


class Model_Trough_Name(models.Model):
    """
    Содержит варианты моделей кормкшек
    """
    # Название модели кормушки
    model_trough_name = models.CharField(
        max_length=20,
        verbose_name="Модель кормушки")

    class Meta:
        verbose_name = "Название модели кормушки"
        verbose_name_plural = "Названия моделей кормушек"


class Feed_Capacity(models.Model):
    """
    Содержит варианты кормоемкости кормушек
    """
    # Кормоемкость кормушки
    feed_capacity_name = models.CharField(
        max_length=20,
        verbose_name="Кормоемкость")

    class Meta:
        verbose_name = "Кормоёмкость кормушки"
        verbose_name_plural = "Кормоёмкость кормушек"


class Fishing_Lure(models.Model):
    """
    Содержит информацию о прикормочной смеси
    используемой в рыбалке
    """
    class Meta:
        verbose_name = "Прикормочная смесь"
        verbose_name_plural = "Прикормочные смеси"
    #Прикорм - Ok
    # Наживка
    nozzle = models.ForeignKey(
        'Nozzle',
        on_delete=models.PROTECT,
        verbose_name="Наживка")
    # Информация о состояни наживки
    nozzle_state = models.ForeignKey(
        'Nozzle_State',
        on_delete=models.PROTECT,
        verbose_name="Состояние наживки")


class Lure(models.Model):
    """
    Содежит информацию о названии
    производителя и названии прикормки
    """
    class Meta:
        verbose_name = "Прикорм"
        verbose_name_plural = "Прикорм"
    # Связь с прикормочной смесью
    fishing_lure = models.ForeignKey(
        'Fishing_Lure',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Название производителя прикорки
    lure_manufacturer = models.CharField(
        max_length=100,
        verbose_name="Производитель")
    # Название прикормки
    lure_name = models.CharField(
        max_length=100,
        verbose_name="Название")


class Nozzle(models.Model):
    """
    Сожердит информацию о наживках/насадках
    При bait=True наживка (поле nozzle_manufacturer
    неактивно) иначе насадка
    """
    class Meta:
        verbose_name = "Наживка/насадка"
        verbose_name_plural = "Наживки/насадки"
    # True наживка иначе насадка
    bait = models.BooleanField(
        default=False,
        verbose_name="Живой компонент")
    # Производитель насадки
    nozzle_manufacturer = models.CharField(
        max_length=100,
        verbose_name="Производитель")
    # Название насадки/наживки
    nozzle_name = models.CharField(
        max_length=100,
        verbose_name="Название")
    # Диаметр насадки
    nozzel_diameter = models.PositiveIntegerField(
        default=0,
        verbose_name="Диаметр насадки")
    # тип насадки (Плавающий, тонущий, пылящий и т.д.)
    nozzel_type = models.CharField(
        max_length=20,
        verbose_name="Тип насадки")


class Nozzle_State(models.Model):
    """
    Содержит информацию о состоянии насадки
    """
    class Meta:
        verbose_name = "Состояние насадки"
        verbose_name_plural = "Состояние насадок"
    # Состояние
    state = models.CharField(
        max_length=20,
        verbose_name="Состояние наживки")


class Aroma(models.Model):
    """
    Содержит информацию о производителе и названию аромы
    """
    class Meta:
        verbose_name = "Арома"
        verbose_name_plural = "Аромы"

    # Название производителя
    aroma_manufacturer = models.CharField(
        max_length=100,
        verbose_name="Производтель")
    # Название аромы
    aroma_name = models.CharField(
        max_length=100,
        verbose_name="Название")


class Fishing_Leash(models.Model):
    """
    Содержит информацию о поводках
    """
    class Meta:
        verbose_name = "Поводок"
        verbose_name_plural = "Поводки"
    # Поводочный материал
    fishing_leash_material = models.CharField(
        max_length=20,
        verbose_name="Поводочный материал")
    # Диаметр поводочного материала
    fishing_leash_diameter = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        verbose_name="Диамет поводочного материла")
    # Длина поводка
    fishing_leash_length = models.PositiveIntegerField(
        default=0,
        verbose_name="Длина поводка")


class Crochet(models.Model):
    """
    Содержит информацию о производителях и моделях крючков
    """
    class Meta:
        verbose_name = "Крючок"
        verbose_name_plural = "Крючки"
    # Производитель
    crochet_manufacturer = models.CharField(
        max_length=20,
        verbose_name="Производитель крючка")
    # модель
    crochet_model = models.CharField(
        max_length=20,
        verbose_name="Модель крючка")
    # размер
    crochet_size = models.PositiveIntegerField(
        default=0,
        verbose_name="Размер крючка")


class Pace(models.Model):
    """
    Содержит информацию о темпе
    """
    class Meta:
        verbose_name = "Темп"
        verbose_name_plural = "Темп"
    # Темп
    pace_interval = models.CharField(
        max_length=20,
        verbose_name="Темп")


class Fishing_Result(models.Model):
    """
    Содержит информацию о результате рыбалки, принимает
    в себя несколько значений пойманной рыбы
    """
    class Meta:
        verbose_name = "Результат рыбалки"
        verbose_name_plural = "Результат рыбалок"
    # Привязка к рыбалке, т.к. может быть несколько вариантов
    # то именное модель результатов привязываем, а не на
    # оборот
    fishing = models.ForeignKey(
        'Fishing',
        on_delete=models.CASCADE,
        verbose_name="Рыбалка")
    # Рыба
    fish = models.ForeignKey(
        'Fish',
        on_delete=models.PROTECT,
        verbose_name="Рыба")
    # Количество хвостов
    nuber_of_fish = models.PositiveIntegerField(
        verbose_name="Количество рыб")
    # Масса улова по выбранной рыбе
    fish_weight = models.PositiveIntegerField(
        verbose_name="Вес улова")


class Fish_Trophy(models.Model):
    """
    Содержит информацию о пойманных трофеях
    """
    class Meta:
        verbose_name = "Трофейный улов"
        verbose_name_plural = "Трофейные уловы"
    # Привязка к рыбалке, т.к. может быть несколько вариантов
    # то именное модель трофеев привязываем, а не на
    # оборот
    fishing = models.ForeignKey(
        'Fishing',
        on_delete=models.CASCADE,
        verbose_name="Рыбалка")
    # Порода трофея
    fish = models.ForeignKey(
        'Fish',
        on_delete=models.PROTECT,
        verbose_name="Рыба"
    )
    # Вес трофея
    fish_trophy_weight = models.PositiveIntegerField(
        verbose_name="Вес трофея")
#    fish_trophy_photo=models.ImageField(verbose_name="Фото трофея")


class District(models.Model):
    """
    Содержит информацию о районе рыбалки
    """
    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
    # Название района
    district_name = models.CharField(
        max_length=50,
        verbose_name="Район")


class Water(models.Model):
    """
    Содержит название водоема с привязкой к району
    """
    class Meta:
        verbose_name = "Водоем"
        verbose_name_plural = "Водоемы"
    # Привязка к району
    district = models.ForeignKey(
        'District',
        on_delete=models.CASCADE,
        verbose_name="Район")
    # Название водоема
    water_name = models.CharField(
        max_length=100,
        verbose_name="Водоем")

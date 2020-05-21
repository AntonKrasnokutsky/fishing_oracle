from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser


class Aroma(models.Model):  # Аромы в прикормочной смеси
    class Meta:
        verbose_name = 'Арома в прикормочной смеси'
        verbose_name_plural = 'Аромы в прикормочной смеси'
        ordering = ['fishing_lure', 'aroma_base', 'aroma_volume', ]
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    fishing_lure = models.ForeignKey(
        'FishingLure',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    aroma_base = models.ForeignKey(
        'AromaBase',
        on_delete=models.PROTECT,
        verbose_name="Арома базовая")
    aroma_volume = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        verbose_name="Объем аромы в литрах")


class AromaBase(models.Model):  # Аромы базовые
    """
    Содержит информацию о производителе и названию аромы
    """
    class Meta:
        verbose_name = "Арома базовая"
        verbose_name_plural = "Аромы базовые"
        ordering = ['aroma_manufacturer', 'aroma_name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название производителя
    aroma_manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производтель")
    # Название аромы
    aroma_name = models.CharField(
        max_length=100,
        verbose_name="Название")

    def __str__(self):
        return self.aroma_manufacturer + ' ' + self.aroma_name


class BottomMap(models.Model):  # Карты дна
    """
    Содержит информацию о маркерной карте, включает в себя
    координаты базовой точки, и привязку всех маркерных точек
    (в одельной таблице)
    """
    # Привязка к водоему
    class Meta:
        verbose_name = "Карта дна"
        verbose_name_plural = "Карты дна"
        ordering = ['bottom_map_northern_degree', 'bottom_map_northern_minute',
                    'bottom_map_northern_second', 'bottom_map_easter_degree',
                    'bottom_map_easter_minute', 'bottom_map_easter_second', ]
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        verbose_name="Место")
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
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

    def __str__(self):
        str_n = ('N: ' + str(self.bottom_map_northern_degree) + '° ' +
                 str(self.bottom_map_northern_minute) + "' " +
                 str(self.bottom_map_northern_second) + '" ')
        str_e = ('E: ' + str(self.bottom_map_easter_degree) + '° ' +
                 str(self.bottom_map_easter_minute) + "' " +
                 str(self.bottom_map_easter_second) + '"')
        return (str_n + ' ' + str_e)


class Crochet(models.Model):  # Крючки
    """
    Содержит информацию о производителях и моделях крючков
    """
    class Meta:
        verbose_name = "Крючок"
        verbose_name_plural = "Крючки"
        ordering = ['crochet_manufacturer', 'crochet_model', 'crochet_size', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель
    crochet_manufacturer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Производитель крючка")
    # модель
    crochet_model = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Модель крючка")
    # размер
    crochet_size = models.PositiveIntegerField(
        default=0,
        verbose_name="Размер крючка")

    def __str__(self):
        return self.crochet_manufacturer + ' ' + self.crochet_model + ' ' + str(self.crochet_size)


class District(models.Model):  # Районы
    """
    Содержит информацию о районе рыбалки
    """
    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Районы"
        ordering = ['district_name', ]
    # Название района
    district_name = models.CharField(
        max_length=50,
        verbose_name="Район",
        unique=True)

    def __str__(self):
        return self.district_name


class FeedCapacity(models.Model):  # Кормоёмкость
    """
    Содержит варианты кормоемкости кормушек
    """
    class Meta:
        verbose_name = "Кормоёмкость кормушки"
        verbose_name_plural = "Кормоёмкость кормушек"
        ordering = ['feed_capacity_name']
    # Кормоемкость кормушки
    feed_capacity_name = models.CharField(
        max_length=20,
        verbose_name="Кормоемкость",
        unique=True)

    def __str__(self):
        return self.feed_capacity_name


class Fish(models.Model):  # Рыбы
    """
    Таблица хранящая в себе информацию о породах рыб,
    в дальнейшем планируется добавление изображение рыб
    """
    class Meta:
        verbose_name = "Рыба"
        verbose_name_plural = "Рыбы"
        ordering = ['name_of_fish']
    # Название рыбы https://gdekluet.ru/directory/fish/
    name_of_fish = models.CharField(
        max_length=20,
        verbose_name="Рыба",
        unique=True)
    fish_description = models.TextField(blank=True,
                                        verbose_name="Описание")

    def __str__(self):
        return self.name_of_fish


class Fishing(models.Model):  # Рыбалки
    """
    Содержит всю информацию о рыбалке
    """
    class Meta:
        verbose_name = "Рыбалка"
        verbose_name_plural = "Рыбалки"
        ordering = ['date', 'time', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Дата проведения рыбалки
    date = models.DateField(
        auto_now_add=False,
        verbose_name="Дата рыбалки")
    # Время начала рыбалки
    time = models.TimeField(
        auto_now_add=False,
        verbose_name="Время начала")
    # Место проведения рыбалки
    # PlaceFishing
    # Погода
    weather = models.ForeignKey(
        'Weather',
        on_delete=models.PROTECT,
        verbose_name="Погода")
    # Снасть
    fishing_tackle = models.ForeignKey(
        'FishingTackle',
        on_delete=models.PROTECT,
        verbose_name="Снасть")
    # Монтаж
    fishing_montage = models.ForeignKey(
        'FishingMontage',
        on_delete=models.PROTECT,
        verbose_name="Монтаж")
    # Используемая кормушка
    fishing_trough = models.ForeignKey(
        'FishingTrough',
        on_delete=models.PROTECT,
        verbose_name="Кормушка")
    # Прикормочная смесь
    fishing_lure = models.ForeignKey(
        'FishingLure',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Арома
    aroma = models.ForeignKey(
        'Aroma',
        on_delete=models.PROTECT,
        verbose_name="Арома")
    # Поводок
    fishing_leash = models.ForeignKey(
        'FishingLeash',
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

    def __str__(self):
        return str(self.date) + ' ' + str(self.time)


class FishingLeash(models.Model):  # Поводки
    """
    Содержит информацию о поводках
    """
    class Meta:
        verbose_name = "Поводок"
        verbose_name_plural = "Поводки"
        ordering = ['fishing_leash_material', 'fishing_leash_diameter',
                    'fishing_leash_length', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи"
    )
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

    def __str__(self):
        return (self.fishing_leash_material + ' ' + str(self.fishing_leash_diameter) +
                ' ' + str(self.fishing_leash_length) + ' см.')


class FishingLure(models.Model):  # Прикормочный состав
    """
    Содержит информацию о прикормочной смеси
    используемой в рыбалке
    """
    class Meta:
        verbose_name = "Прикормочная смесь"
        verbose_name_plural = "Прикормочные смеси"
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи"
    )
    #Прикорм - Ok
    # Наживка
    nozzle = models.ForeignKey(
        'Nozzle',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name="Наживка")
    # Информация о состояни наживки
    nozzle_state = models.ForeignKey(
        'NozzleState',
        on_delete=models.PROTECT,
        blank=True,
        verbose_name="Состояние наживки")


class FishingMontage(models.Model):  # Монтажи
    """
    Содержит в себе варианты монтажей с вариантом выбора
    скользящего
    """
    class Meta:
        verbose_name = "Монтаж"
        verbose_name_plural = "Монтажи"
        ordering = ['fishing_montage_name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Вариант монтажа
    fishing_montage_name = models.CharField(
        max_length=15,
        verbose_name="Монтаж")
    # Скользащий да или нет
    fishing_montage_sliding = models.BooleanField(
        default=False,
        verbose_name="Скользящий монтаж")

    def __str__(self):
        return (self.fishing_montage_name + ' ' +
                ('скользящий' if self.fishing_montage_sliding else ''))


class FishingPoint(models.Model):  # Точки ловли
    """
    Содежит информацию о точке ловли, возможно использование
    в нескольких рыбалках
    """
    class Meta:
        verbose_name = "Точка ловли"
        verbose_name_plural = "Точки ловли"
        ordering = ['fishing_point_distance', ]
    # Владелец записи
    owner = models.ForeignKey(CustomUser,
                              on_delete=models.PROTECT,
                              verbose_name="Владелец записи")
    # Привязка к месту
    place = models.OneToOneField('Place',
                                 on_delete=models.PROTECT,
                                 verbose_name='Место ловли')
    # Азимут заброса
    fishing_point_azimuth = models.PositiveIntegerField(
        default=0,
        verbose_name="Азимут")
    # Дистанция до точки ловли
    fishing_point_distance = models.PositiveIntegerField(
        default=0,
        verbose_name="Дистанция")
    # Глубина в точке ловли
    fishing_poiny_depth = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Глубина")
    # Грунт в точке ловли
    priming = models.ForeignKey(
        'Priming',
        on_delete=models.PROTECT,
        verbose_name="Грунт"
    )

    def __str__(self):
        return (str(self.priming) + 'Дистанция: ' +
                str(self.fishing_point_distance) + 'м.')


class FishingResult(models.Model):  # Результат рыбалки
    """
    Содержит информацию о результате рыбалки, принимает
    в себя несколько значений пойманной рыбы
    """
    class Meta:
        verbose_name = "Результат рыбалки"
        verbose_name_plural = "Результат рыбалок"
        ordering = ['fish', ]
    # Привязка к рыбалке, т.к. может быть несколько вариантов
    # то именное модель результатов привязываем, а не на
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи"
    )
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
    number_of_fish = models.PositiveIntegerField(
        blank=True,
        verbose_name="Количество рыб")
    # Масса улова по выбранной рыбе
    fish_weight = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        blank=True,
        verbose_name="Вес улова")

    def __str__(self):
        return (str(self.fish) + ': ' + str(self.number_of_fish) +
                'шт. ' + str(self.fish_weight) + 'кг.')


class FishingTackle(models.Model):  # Снасти
    """
    Содержит информацию о снасти: донная, поплавочная и т.д.
    """
    class Meta:
        verbose_name = "Рыболовная снасть"
        verbose_name_plural = "Рыболовные снасти"
        ordering = ['fishing_tackle_manufacturer', 'fishing_tackle_name',
                    'fishing_tackle_length', 'fishing_tackle_casting_weight', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель снасти
    fishing_tackle_manufacturer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Производитель")
    # Инормация о используемой снасти
    fishing_tackle_name = models.CharField(
        max_length=30,
        verbose_name="Название")
    fishing_tackle_length = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0,
        verbose_name="Длина (м)")
    fishing_tackle_casting_weight = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Тест удилища (гр)")

    def __str__(self):
        return (self.fishing_tackle_manufacturer + ' ' + self.fishing_tackle_name +
                ' ' + str(self.fishing_tackle_length) + ' ' +
                str(self.fishing_tackle_casting_weight))


class FishingTrough(models.Model):  # Кормушки
    """
    Содержит информацию о кормушках
    """
    class Meta:
        verbose_name = "Рыболовная кормушка"
        verbose_name_plural = "Рыболовные кормушки"
        ordering = ['fishing_trough_manufacturer', 'model_trough',
                    'fishing_trough_weight', 'feed_capacity', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель кормушки
    fishing_trough_manufacturer = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Поизводитель")
    # Связь с таблицей модели кормушки
    model_trough = models.ForeignKey(
        'ModelTrough',
        on_delete=models.PROTECT,
        verbose_name="Модель кормушки")
    # Связь с таблицей кормоемкости
    feed_capacity = models.ForeignKey(
        'FeedCapacity',
        on_delete=models.PROTECT,
        verbose_name="Кормоёмкость")
    # Вес кормушки
    fishing_trough_weight = models.PositiveIntegerField(
        default=0,
        verbose_name="Вес кормушки")

    def __str__(self):
        return (self.fishing_trough_manufacturer + ': ' + str(self.feed_capacity) +
                ' ' + str(self.model_trough) + ' ' +
                str(self.fishing_trough_weight) + 'гр.')


class FishTrophy(models.Model):  # Трофей рыбалки
    """
    Содержит информацию о пойманных трофеях
    """
    class Meta:
        verbose_name = "Трофейный улов"
        verbose_name_plural = "Трофейные уловы"
        ordering = ['fish_trophy_weight', 'fish', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
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
        verbose_name="Рыба")
    # Вес трофея
    fish_trophy_weight = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name="Вес трофея")
    #fish_trophy_photo=models.ImageField(verbose_name="Фото трофея")

    def __str__(self):
        return 'Трофей: ' + str(self.fish) + ' ' + str(self.fish_trophy_weight) + 'кг.'


class Lure(models.Model):  # Смесь прикорма
    """
    Содежит информацию о прикорме в составе смеси
    """
    class Meta:
        verbose_name = "Прикорм"
        verbose_name_plural = "Прикорм"
        ordering = ['lure_base', 'lure_weight', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь с прикормочной смесью
    fishing_lure = models.ForeignKey(
        'FishingLure',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Связь с базовым прикормом
    lure_base = models.ForeignKey(
        'LureBase',
        on_delete=models.PROTECT,
        verbose_name="Базовый прикорм")
    # Вес базового прикорма
    lure_weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Вес прикорма")

    def __str__(self):
        return str(self.lure_base)


class LureBase(models.Model):  # Прикорм
    """
    Содержит базовые прикормы, из которых в свою
    очередь замещивается кормовая смесь
    """
    class Meta:
        verbose_name = "Базовый прикорм"
        verbose_name_plural = "Базовый прикорм"
        ordering = ['lure_manufacturer', 'lure_name']

    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название производителя прикорки
    lure_manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производитель")
    # Название прикормки
    lure_name = models.CharField(
        max_length=100,
        verbose_name="Название")

    def __str__(self):
        return self.lure_manufacturer + ' ' + self.lure_name


class ModelTrough(models.Model):  # Модели кормушек
    """
    Содержит комбинации моделей кормушек
    """
    class Meta:
        verbose_name = "Модель кормушки"
        verbose_name_plural = "Модели кормушек"
        ordering = ['model_trough_name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь со списком моделей
    model_trough_name = models.ForeignKey(
        'ModelTroughName',
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

    def __str__(self):
        return str(self.model_trough_name)


class ModelTroughName(models.Model):  # Название моделей кормушек
    """
    Содержит варианты моделей кормкшек
    """
    class Meta:
        verbose_name = "Название модели кормушки"
        verbose_name_plural = "Названия моделей кормушек"
        ordering = ['model_trough_name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название модели кормушки
    model_trough_name = models.CharField(
        max_length=20,
        verbose_name="Модель кормушки",
        unique=True)

    def __str__(self):
        return self.model_trough_name


class Nozzle(models.Model):  # Насдаки и наживки
    """
    Сожердит информацию о наживках/насадках
    При bait=True наживка (поле nozzle_manufacturer
    неактивно) иначе насадка
    """
    class Meta:
        verbose_name = "Наживка/насадка"
        verbose_name_plural = "Наживки/насадки"
        ordering = ['bait', 'nozzle_manufacturer', 'nozzle_name',
                    'nozzle_type', 'nozzle_diameter', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # True наживка иначе насадка
    bait = models.BooleanField(
        default=False,
        verbose_name="Живой компонент")
    # Производитель насадки
    nozzle_manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производитель")
    # Название насадки/наживки
    nozzle_name = models.CharField(
        max_length=100,
        verbose_name="Название")
    # Диаметр насадки
    nozzle_diameter = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Диаметр насадки")
    # тип насадки (Плавающий, тонущий, пылящий и т.д.)
    nozzle_type = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Тип насадки")

    def __str__(self):
        return self.nozzle_name


class NozzleState(models.Model):  # Состояние наживки
    """
    Содержит информацию о состоянии насадки
    """
    class Meta:
        verbose_name = "Состояние насадки"
        verbose_name_plural = "Состояние насадок"
        ordering = ['state', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Состояние
    state = models.CharField(
        max_length=20,
        verbose_name="Состояние наживки",
        unique=True)

    def __str__(self):
        return self.state


class Overcast(models.Model):  # Облачность
    """
    Содержит варианты облочности для блока 'Погода'
    """
    class Meta:
        verbose_name = "Облачность"
        verbose_name_plural = "Облачность"
        ordering = ["overcast_name"]
    # Вариант облачности
    overcast_name = models.CharField(
        max_length=30,
        verbose_name="Классификация облачности",
        unique=True)

    def __str__(self):
        return self.overcast_name


class Pace(models.Model):  # Темп
    """
    Содержит информацию о темпе
    """
    class Meta:
        verbose_name = "Темп"
        verbose_name_plural = "Темп"
        ordering = ['pace_interval', ]
    # Темп
    pace_interval = models.CharField(
        max_length=30,
        verbose_name="Темп",
        unique=True)

    def __str__(self):
        return self.pace_interval


class Place(models.Model):  # Места
    """
    Содержит информацию о месте рыбалки
    """
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ['place_locality', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к водоему
    water = models.ForeignKey(
        'Water',
        on_delete=models.PROTECT,
        verbose_name="Водоем")
    # Ближайший населенный пункт
    place_locality = models.CharField(
        max_length=50,
        verbose_name="Населенный пункт",
        help_text="Название ближайшего населенного пункта")
    # Название места
    place_name = models.CharField(
        max_length=50,
        verbose_name="Название места")
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
    # Фотография места рыбалки
    # photo_place=models.ImageField(
    #     verbose_name="Места")

    def __str__(self):
        return self.place_locality


class PlaceFishing(models.Model):
    class Meta:
        verbose_name = 'Место рыбалки'
        verbose_name_plural = 'Места рыбалки'
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Рыбалка
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.PROTECT,
                                verbose_name='Рыбалка')
    # Место
    place = models.ForeignKey('Place',
                              on_delete=models.PROTECT,
                              verbose_name='Место рыбалки')


class Point(models.Model):  # Точки карт дна
    """
    Содержит информацию о маркерной точке, привязывается
    к маркерной карте. Информация о грунте возмоно выбор
    из списка
    """
    class Meta:
        verbose_name = "Точка карты дна"
        verbose_name_plural = "Точки карт дна"
        ordering = ['point_azimuth', 'point_distance', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к маркерной карте
    bottom_map = models.ForeignKey(
        'BottomMap',
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
    point_depth = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Глубина")
    # Грунт
    priming = models.ForeignKey(
        'Priming',
        on_delete=models.PROTECT,
        verbose_name="Грунт")

    def __str__(self):
        return (str(self.bottom_map) + ': ' + str(self.point_azimuth) +
                ' ' + str(self.point_distance))


class Priming(models.Model):  # Грунт
    """
    Содержит варианты дна, например ил, камень, песок и т.д.
    Возможно отказаться от таблицы, т.к. варианты можно выбить из списка
    """
    class Meta:
        verbose_name = "Покрытие дна"
        verbose_name_plural = "Покрытие дна"
        ordering = ['priming_name']
    # Наименование покрытия дна
    priming_name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Грунт")

    def __str__(self):
        return self.priming_name


class Water(models.Model):  # Водоемы
    """
    Содержит название водоема с привязкой к району
    """
    class Meta:
        verbose_name = "Водоем"
        verbose_name_plural = "Водоемы"
        ordering = ['water_name', ]
    # Привязка к району
    district = models.ForeignKey(
        'District',
        on_delete=models.CASCADE,
        verbose_name="Район")
    # Название водоема
    water_name = models.CharField(
        max_length=100,
        verbose_name="Водоем")

    def __str__(self):
        return self.water_name


class Weather(models.Model):  # Погода
    """
    Содержит сводные сведения о погоде
    опираясь на ручной ввод
    """
    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"
        ordering = ['date', ]
    # Привязка к месту
    place = models.ForeignKey('Place',
                              on_delete=models.PROTECT,
                              verbose_name='Место')
    # Дата погоды
    date = models.DateField(
        auto_now_add=False,
        verbose_name="Дата")
    # Облачность
    overcast = models.ForeignKey('Overcast',
                                 on_delete=models.PROTECT,
                                 verbose_name="Облачность")
    # Связь с таблицей "Явления погоды"
    weather_phenomena = models.ForeignKey('WeatherPhenomena',
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

    def __str__(self):
        return str(self.date)


class WeatherPhenomena(models.Model):  # Явления погоды
    """
    Явления погоды, возможно несколько записей
    для одного выезда
    """
    class Meta:
        verbose_name = "Погодное явление"
        verbose_name_plural = "Погодные явления"
        ordering = ["weather_phenomena_name"]

    # Погодные явления
    weather_phenomena_name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Погодные явления")

    def __str__(self):
        return self.weather_phenomena_name

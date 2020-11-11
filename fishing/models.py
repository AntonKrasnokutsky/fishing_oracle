from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from datetime import datetime
from users.models import CustomUser
import re


class Aroma(models.Model):  # Аромы в прикормочной смеси
    """
    Содержит информацию об аромах в прикормочном составе
    """
    class Meta:
        verbose_name = 'Арома в прикормочной смеси'
        verbose_name_plural = 'Аромы в прикормочной смеси'
        ordering = ['lure_mix', 'aroma_base', 'aroma_volume', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Прикормочный состав
    lure_mix = models.ForeignKey(
        'LureMix',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Арома
    aroma_base = models.ForeignKey(
        'AromaBase',
        on_delete=models.PROTECT,
        verbose_name="Арома базовая")
    # Объем аромы
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
        ordering = ['manufacturer', 'name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название производителя
    manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производтель")
    # Название аромы
    name = models.CharField(
        max_length=100,
        verbose_name="Название")

    def __str__(self):
        return self.manufacturer + ' ' + self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
        self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        aroma_base_list = AromaBase.objects.filter(owner=self.owner)
        for aroma_base in aroma_base_list:
            if aroma_base.id != self.id:
                if (aroma_base.manufacturer.lower() == self.manufacturer.lower() and
                    aroma_base.name.lower() == self.name.lower()):
                    return False
        else:
            return True


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
        ordering = ['manufacturer', 'model', 'size', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель
    manufacturer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Производитель крючка")
    # модель
    model = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Модель крючка")
    # размер
    size = models.PositiveIntegerField(
        default=0,
        verbose_name="Размер крючка")

    def __str__(self):
        return 'Крючок ' + self.manufacturer + ' ' + self.model + ' размер ' + str(self.size)

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
        self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        crochet_list = Crochet.objects.filter(owner=self.owner)
        for crochet in crochet_list:
            if crochet.id != self.id:
                if (crochet.manufacturer.lower() == self.manufacturer.lower() and
                    crochet.model.lower() == self.model.lower() and crochet.size == self.size):
                    return False
        else:
            return True


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
        ordering = ['name']
    # Кормоемкость кормушки
    name = models.CharField(
        max_length=20,
        verbose_name="Кормоемкость",
        unique=True)

    def __str__(self):
        return self.name
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)


class Fish(models.Model):  # Рыбы
    """
    Таблица хранящая в себе информацию о породах рыб,
    в дальнейшем планируется добавление изображение рыб
    """
    class Meta:
        verbose_name = "Рыба"
        verbose_name_plural = "Рыбы"
        ordering = ['name']
    # Название рыбы https://gdekluet.ru/directory/fish/
    name = models.CharField(
        max_length=20,
        verbose_name="Рыба",
        unique=True)
    description = models.TextField(blank=True,
                                        verbose_name="Описание")

    def __str__(self):
        return self.name
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)
        #self.description = re.sub(r'\s+', ' ', self.description)


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
    # weather
    # Снасть
    # fishing_tackle
    # Монтаж
    # fishing_montage
    # Используемая кормушка
    # fishing_trough
    # Прикормочная смесь
    # fishing_lure
    # Арома
    # В прикормочной смеси
    # Поводок
    # fishing_leash
    # Крючек
    # crochet
    # Наживка/насадка
    # nozzle
    # Темп
    # pace
    # Результат рыбалки
    # Трофей
    #
    planned = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + ' ' + str(self.time)

    def set_planned(self):
        """
        Поверяет дату проведения рыбалки и текущую дату,
        с выставлением статуса "Запланировано"
        """
        if self.date > datetime.now().date():
            self.planned = True
        else:
            self.planned = False


class FishingCrochet(models.Model):  # Крючки использованные в рыбалке
    """
    Содержит информациб о крючках использованных в рыбалке
    """
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ['crochet']
    # Владелец записи
    owner = models.ForeignKey(CustomUser,
                              models.PROTECT,
                              blank=True,
                              null=True,
                              verbose_name='Владелец записи')
    # Привязка к рыбалке
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Рыбалка')
    # Привязка крючка
    crochet = models.ForeignKey('Crochet',
                                on_delete=models.PROTECT,
                                verbose_name='Крючок')

    def __str__(self):
        return str(self.crochet)


class FishingLeash(models.Model):  # Поводки использованные в рыбалке
    """
    Содержит информацию о поводках
    """
    class Meta:
        verbose_name = "Поводок использованный в рыбалке"
        verbose_name_plural = "Поводки использованные в рыбалке"
        ordering = ['fishing_tackle', 'leash', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Рыбалка
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Рыбалка')
    # Поводок
    leash = models.ForeignKey('Leash',
                              on_delete=models.PROTECT,
                              verbose_name='Поводок')


class FishingLure(models.Model):  # Прикормочный состав для рыбалки
    """
    Содержит информацию о прикормочной смеси
    используемой в рыбалке
    """
    class Meta:
        verbose_name = "Прикормочная смесь в рыбалке"
        verbose_name_plural = "Прикормочные смеси в рыбалке"
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к рыбалке
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.PROTECT,
                                verbose_name='Рыбалка')
    # Привязка к смеси
    lure_mix = models.ForeignKey('LureMix',
                                 on_delete=models.PROTECT,
                                 verbose_name='Прикормочная смесь')


class FishingMontage(models.Model):  # Монтажи в рыбалке
    """
    Содержит в себе варианты монтажей с вариантом выбора
    скользящего
    """
    class Meta:
        verbose_name = "Монтаж на рыбалке"
        verbose_name_plural = "Монтажи на рыбалке"
        ordering = ['fishing_tackle', 'montage', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к рыбалке
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Снасть')
    # Привязка монтажа
    montage = models.ForeignKey('Montage',
                                on_delete=models.PROTECT,
                                verbose_name="Монтаж")


class FishingNozzle(models.Model):  # Наживки\насадки использованные в рыбалке
    """
    Содержит связи наживок и их состояний с рыбалкой
    """
    class Meta:
        verbose_name = 'Наживка использованная в рыбалке'
        verbose_name_plural = 'Наживки использованная в рыбалке'
        ordering = ['id', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь с рыбалкой
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Снасть')
    # Свзять с наживкой
    nozzle_base = models.ForeignKey('NozzleBase',
                                    on_delete=models.PROTECT,
                                    verbose_name='Наживка')
    # Связь с состоянием наживки
    # nozzle_state= models.ForeignKey('NozzleState',
    #                            on_delete=models.PROTECT,
    #                            verbose_name='Состояние наживки')


class FishingPace(models.Model):  # Темп рыбалки
    class Meta:
        verbose_name = 'Темп рыбалки'
        verbose_name_plural = 'Темп рыбалки'
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь с рыбалкой
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Снасть')
    # Связь с темпом
    pace = models.ForeignKey('Pace',
                             on_delete=models.PROTECT,
                             verbose_name='Темп')


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
        verbose_name="Владелец записи")
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
        decimal_places=3,
        blank=True,
        verbose_name="Вес улова")

    def __str__(self):
        return (str(self.fish) + ': ' + str(self.number_of_fish) +
                'шт. ' + str(self.fish_weight) + 'кг.')


class FishingTackle(models.Model):  # Снасть использованная в рыбалке
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к рыбалке
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.PROTECT,
                                verbose_name='Рыбалка')
    # Привязка снасти
    tackle = models.ForeignKey('Tackle',
                               on_delete=models.PROTECT,
                               verbose_name='Снасть')


class FishingTrough(models.Model):  # Кормушки использованные в рыбалке
    """
    Содержит информацию о кормушках исользованных в рыбалке
    """
    class Meta:
        verbose_name = "Рыболовная кормушка"
        verbose_name_plural = "Рыболовные кормушки"
        ordering = ['fishing_tackle', 'trough', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к рыбалке
    fishing_tackle = models.ForeignKey('FishingTackle',
                                       on_delete=models.PROTECT,
                                       blank=True,
                                       null=True,
                                       verbose_name='Снасть')
    # Привязка к кормушке
    trough = models.ForeignKey(
        'Trough',
        on_delete=models.PROTECT,
        verbose_name="Кормушка")


class FishingWeather(models.Model):  # Погода во время рыбалки
    """
    Содержит информацию о погоде во время рыбалки
    """
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь с рыбалкой
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.PROTECT,
                                verbose_name='Рыбалка')
    # Связь с записью погоды
    weather = models.ForeignKey('Weather',
                                on_delete=models.PROTECT,
                                verbose_name='Погода')


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


class Leash(models.Model):  # Поводки
    """
    Содержит информацию о поводках
    """
    class Meta:
        verbose_name = "Поводок"
        verbose_name_plural = "Поводки"
        ordering = ['material', 'diameter', 'length', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи"
    )
    # Поводочный материал
    material = models.CharField(
        max_length=20,
        verbose_name="Материал поводка")
    # Диаметр поводочного материала
    diameter = models.DecimalField(
        max_digits=4,
        decimal_places=3,
        default=0,
        verbose_name="Диаметр поводка")
    # Длина поводка
    length = models.PositiveIntegerField(
        default=0,
        verbose_name="Длина поводка")

    def __str__(self):
        return (self.material + ' ' + str(self.diameter) + ' мм.' +
                ' ' + str(self.length) + ' см.')

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.material = str(self.material[0].upper()) + self.material[1:]
        self.material = re.sub(r'\s+', ' ', self.material)

    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        leash_list = Leash.objects.filter(owner=self.owner)
        for leash in leash_list:
            if leash.id != self.id:
                if leash.material.lower() == self.material.lower() and leash.diameter == self.diameter and leash.length == self.length:
                    return False
        else:
            return True


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
    lure_mix = models.ForeignKey(
        'LureMix',
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
        verbose_name="Вес прикорма, кг.",
        help_text="от 0 до 99.9 кг",
        validators=[MinValueValidator(0.0), MaxValueValidator(99.9)])

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
        ordering = ['manufacturer', 'name']

    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название производителя прикорки
    manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производитель")
    # Название прикормки
    name = models.CharField(
        max_length=100,
        verbose_name="Название")

    def __str__(self):
        return self.manufacturer + ' ' + self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
        self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        lure_base_list = LureBase.objects.filter(owner=self.owner)
        for lure_base in lure_base_list:
            if lure_base.id != self.id:
                if (lure_base.manufacturer.lower() == self.manufacturer.lower() and
                    lure_base.name.lower() == self.name.lower()):
                    return False
        else:
            return True


class LureMix(models.Model):  # Смеси прикромов
    """
    Содержит прикормочный состав
    """
    class Meta:
        verbose_name = 'Прикормочная смесь'
        verbose_name_plural = 'Прикормочные смеси'
        ordering = ['lure_mix_name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название состава
    lure_mix_name = models.CharField(max_length=100,
                                     verbose_name='Название состава')

    def __str__(self):
        return self.lure_mix_name


class Montage(models.Model):  # Монтажи
    """
    Содержит в себе варианты монтажей с вариантом выбора
    скользящего
    """
    class Meta:
        verbose_name = "Монтаж"
        verbose_name_plural = "Монтажи"
        ordering = ['name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Вариант монтажа
    name = models.CharField(
        max_length=50,
        verbose_name="Монтаж")

    def __str__(self):
        return self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        montage_list = Montage.objects.filter(owner=self.owner)
        for montage in montage_list:
            if montage.id != self.id:
                if montage.name.lower() == self.name.lower():
                    return False
        else:
            return True



class Nozzle(models.Model):  # Добавки в прикормочную смесь
    class Meta:
        verbose_name = "Добавка в прикормочную смесь"
        verbose_name_plural = "Добавки в прикормочную смесь"
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Наживка/насадка
    nozzle_base = models.ForeignKey('NozzleBase',
                                    on_delete=models.PROTECT,
                                    verbose_name='Насадка/наживка')
    # Состояние
    nozzle_state = models.ForeignKey('NozzleState',
                                     on_delete=models.PROTECT,
                                     verbose_name='Состояние наживки/насадки')
    # Связь с прикормочной смесью
    lure_mix = models.ForeignKey(
        'LureMix',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")


class NozzleBase(models.Model):  # Насдаки и наживки
    """
    Сожердит информацию о наживках/насадках
    При bait=True наживка (поле nozzle_manufacturer
    неактивно) иначе насадка
    """
    class Meta:
        verbose_name = "Наживка/насадка"
        verbose_name_plural = "Наживки/насадки"
        ordering = ['bait', 'manufacturer', 'name',
                    'ntype', 'size', ]
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
    manufacturer = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Производитель")
    # Название насадки/наживки
    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Название")
    # Диаметр насадки
    size = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Размер насадки")
    # тип насадки (Плавающий, тонущий, пылящий и т.д.)
    ntype = models.ForeignKey(
        'NozzleType',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Тип насадки')

    def __str__(self):
        if self.bait:
            return self.name
        else:
            return self.manufacturer + ' ' + self.name + ' ' + str(self.size) + 'мм.' + (str(self.ntype) if self.ntype != None else '')

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if len(self.manufacturer) > 0:
            self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
            self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        if len(self.name) > 0:
            self.name = str(self.name[0].upper()) + self.name[1:]
            self.name = re.sub(r'\s+', ' ', self.name)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        nozzle_base_list = NozzleBase.objects.filter(owner=self.owner)
        for nozzle_base in nozzle_base_list:
            if nozzle_base.id != self.id:
                if (nozzle_base.manufacturer.lower() == self.manufacturer.lower() and
                    nozzle_base.name.lower() == self.name.lower() and
                    nozzle_base.size == self.size and
                    nozzle_base.ntype == self.ntype and
                    nozzle_base.bait == self.bait):
                    return False
        else:
            return True


class NozzleLure(models.Model):  # Наживки\насадки в прикормочном составе
    """
    """
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Наживка/насадка
    nozzle_base = models.ForeignKey('NozzleBase',
                                    on_delete=models.PROTECT,
                                    verbose_name='Насадка/наживка')
    # Состояние
    nozzle_state = models.ForeignKey('NozzleState',
                                     on_delete=models.PROTECT,
                                     verbose_name='Состояние наживки/насадки')


class NozzleState(models.Model):  # Состояние наживки
    """
    Содержит информацию о состоянии насадки
    """
    class Meta:
        verbose_name = "Состояние наживки или насадки"
        verbose_name_plural = "Состояние насадок или наживок"
        ordering = ['state', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Состояние
    state = models.CharField(
        max_length=20,
        verbose_name="Состояние насадки")

    def __str__(self):
        return self.state

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if len(self.state) > 0:
            self.state = str(self.state[0].upper()) + self.state[1:]
            self.state = re.sub(r'\s+', ' ', self.state)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        nozzle_state_list = NozzleState.objects.filter(owner=self.owner)
        for nozzle_state in nozzle_state_list:
            if nozzle_state.id != self.id:
                if nozzle_state.state.lower() == self.state.lower():
                    return False
        else:
            return True


class NozzleType(models.Model):
    """
    Содержит варианты типов насадки
    """
    class Meta:
        verbose_name = 'Тип насадки'
        verbose_name_plural = 'Типы насадки'
        ordering = ['name']

    # Тип насадки
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Тип насадки')

    def __str__(self):
        return self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)


class Overcast(models.Model):  # Облачность
    """
    Содержит варианты облочности для блока 'Погода'
    """
    class Meta:
        verbose_name = "Облачность"
        verbose_name_plural = "Облачность"
        ordering = ["name"]
    # Вариант облачности
    name = models.CharField(
        max_length=30,
        verbose_name="Вариант облачности",
        unique=True)

    def __str__(self):
        return self.name
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)


class Pace(models.Model):  # Темп
    """
    Содержит информацию о темпе
    """
    class Meta:
        verbose_name = "Темп"
        verbose_name_plural = "Темп"
        ordering = ['interval', ]
    # Темп
    interval = models.CharField(
        max_length=30,
        verbose_name="Темп",
        unique=True)

    def __str__(self):
        return self.interval
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.interval = str(self.interval[0].upper()) + self.interval[1:]
        self.interval = re.sub(r'\s+', ' ', self.interval)


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


class PlaceFishing(models.Model):  # Место рыбалки
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
        verbose_name = "Вариант дна"
        verbose_name_plural = "Варианты дна"
        ordering = ['name']
    # Наименование покрытия дна
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Покрытие")

    def __str__(self):
        return self.name
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)


class Tackle(models.Model):  # Снасти
    """
    Содержит информацию о снасти: донная, поплавочная и т.д.
    """
    class Meta:
        verbose_name = "Рыболовная снасть"
        verbose_name_plural = "Рыболовные снасти"
        ordering = ['tackle_manufacturer', 'tackle_name',
                    'tackle_length', 'tackle_casting_weight', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель снасти
    tackle_manufacturer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Производитель")
    # Инормация о используемой снасти
    tackle_name = models.CharField(
        max_length=30,
        verbose_name="Название")
    tackle_length = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0,
        verbose_name="Длина (м)",
        validators=[MinValueValidator(0.0), MaxValueValidator(99.9)])
    tackle_casting_weight = models.PositiveIntegerField(
        default=0,
        blank=True,
        verbose_name="Тест удилища (гр)")

    def __str__(self):
        return (self.tackle_manufacturer + ' ' + self.tackle_name +
                ' ' + str(self.tackle_length) + ' ' +
                str(self.tackle_casting_weight))


class Trough(models.Model):  # Кормушки
    """
    Содержит информацию о кормушках
    """
    class Meta:
        verbose_name = "Рыболовная кормушка"
        verbose_name_plural = "Рыболовные кормушки"
        ordering = ['manufacturer', 'model_name',
                    'weight', 'feed_capacity', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель кормушки
    manufacturer = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Поизводитель")
    # Название модели кормушки
    model_name = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Модель кормушки")
    # Метка пластиковй кормушки
    plastic = models.BooleanField(
        default=False,
        verbose_name="Пластик")
    # Метка наличия грунтозацепов
    lugs = models.BooleanField(
        default=False,
        verbose_name="грунтозацепы")
    # Связь с таблицей кормоемкости
    feed_capacity = models.ForeignKey(
        'FeedCapacity',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="Кормоёмкость")
    # Вес кормушки
    weight = models.PositiveIntegerField(
        default=0,
        verbose_name="Вес кормушки")

    def __str__(self):
        return (self.manufacturer + ' ' + str(self.model_name) + ' ' +
                str(' пластик' if self.plastic else '') + ' ' +
                ('(' + str(self.feed_capacity) + ' кормоёмкость' + ')' if self.feed_capacity else '')+
                str(' с грунтозацепами' if self.lugs else '') +
                ' ' + str(self.weight) + 'гр.')

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if self.manufacturer:
            self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
            self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        if self.model_name:
            self.model_name = str(self.model_name[0].upper()) + self.model_name[1:]
            self.model_name = re.sub(r'\s+', ' ', self.model_name)

    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        trough_list = Trough.objects.filter(owner=self.owner)
        for trough in trough_list:
            if trough.id != self.id:
                if (trough.manufacturer.lower() == self.manufacturer.lower() and
                    trough.model_name.lower() == self.model_name.lower() and
                    trough.length == self.length and
                    trough.plastic == self.plastic and
                    trough.lugs == self.lugs and
                    trough.feed_capacity == self.feed_capacity and
                    trough.weight == self.weight):
                    return False
        else:
            return True


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
    conditions = models.ForeignKey('Conditions',
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


class Conditions(models.Model):  # Явления погоды
    """
    Явления погоды, возможно несколько записей
    для одного выезда
    """
    class Meta:
        verbose_name = "Погодное явление"
        verbose_name_plural = "Погодные явления"
        ordering = ["name"]

    # Погодные явления
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Погодное явление")

    def __str__(self):
        return self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)

from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from datetime import datetime

from django.shortcuts import get_object_or_404
from users.models import CustomUser
import re

months = ['января',
          'февраля',
          'марта',
          'апреля',
          'мая',
          'июня',
          'июля',
          'августа',
          'сентября',
          'октября',
          'ноября',
          'декабря']


class Aroma(models.Model):  # Аромы в прикормочной смеси
    """
    Содержит информацию об аромах в прикормочном составе
    """
    class Meta:
        verbose_name = 'Арома в прикормочной смеси'
        verbose_name_plural = 'Аромы в прикормочной смеси'
        ordering = ['mix', 'base', 'volume', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Прикормочный состав
    mix = models.ForeignKey(
        'LureMix',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Арома
    base = models.ForeignKey(
        'AromaBase',
        on_delete=models.PROTECT,
        verbose_name="Арома базовая")
    # Объем аромы
    volume = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        verbose_name="Количество аромы")
    
    def __str__(self):
        return str(self.base) + ' ' + str(self.volume) + 'л.'


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
        blank=True,
        verbose_name="Название")

    def __str__(self):
        return self.manufacturer + ' ' + self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if len(self.manufacturer) != 0:
            self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
            self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        if len(self.name) != 0:
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


# class BottomMap(models.Model):  # Карты дна
#     """
#     Содержит информацию о маркерной карте, включает в себя
#     координаты базовой точки, и привязку всех маркерных точек
#     (в одельной таблице)
#     """
#     # Привязка к водоему
#     class Meta:
#         verbose_name = "Карта дна"
#         verbose_name_plural = "Карты дна"
#         ordering = ['date',]
#     place = models.ForeignKey(
#         'Place',
#         on_delete=models.CASCADE,
#         verbose_name="Место")
#     # Владелец записи
#     owner = models.ForeignKey(
#         CustomUser,
#         on_delete=models.PROTECT,
#         verbose_name="Владелец записи")
#     # Дата составления карты
#     date = models.DateField(
#         auto_now_add=False,
#         verbose_name="Дата составления")
#     # Координа базовой точки маркерной карты, градусы северной широты от -90 до 90
#     latitude = models.DecimalField(max_digits=8,
#                                    decimal_places=6,
#                                    blank=True,
#                                    null=True,
#                                    help_text="-90 <> 90",
#                                    verbose_name="Широта")
#     # Координа базовой точки маркерной карты восточной долготы от -180 до 180
#     longitude = models.DecimalField(max_digits=9,
#                                     decimal_places=6,
#                                     blank=True,
#                                     null=True,
#                                     help_text="-180 <> 180",
#                                     verbose_name="Долгота")

#     def __str__(self):
#         return str(self.date)


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
        blank=True,
        verbose_name="Размер крючка")

    def __str__(self):
        return 'Крючок ' + self.manufacturer + ' ' + self.model + ' размер ' + str(self.size)

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if len(self.manufacturer) != 0:
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


# class District(models.Model):  # Районы
#     """
#     Содержит информацию о районе рыбалки
#     """
#     class Meta:
#         verbose_name = "Район"
#         verbose_name_plural = "Районы"
#         ordering = ['district_name', ]
#     # Название района
#     district_name = models.CharField(
#         max_length=50,
#         verbose_name="Район",
#         unique=True)

#     def __str__(self):
#         return self.district_name


class FeedCapacity(models.Model):  # Кормоёмкость
    """
    Содержит варианты кормоемкости кормушек
    """
    class Meta:
        verbose_name = "Кормоёмкость кормушки"
        verbose_name_plural = "Кормоёмкость кормушек"
        ordering = ['id']
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
        verbose_name="Название рыбы",
        unique=True)
    description = models.TextField(blank=True,
                                        verbose_name="Описание рыбы")

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
        ordering = ['date', 'time_start', ]
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
    time_start = models.TimeField(
        auto_now_add=False,
        verbose_name="Время начала")
    # Время начала рыбалки
    time_end = models.TimeField(
        auto_now_add=False,
        verbose_name="Время окончания")
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
    note = models.TextField(blank=True,
                            verbose_name="Заметки о рыбалке")
    report = models.TextField(blank=True,
                              verbose_name="Отчет по рыбалке")

    def date_to_str(self):
        result = str(self.date)[8:10] + ' ' + months[int(str(self.date)[5:7])-1] + ' ' + str(self.date)[:4]
        return result
    
    def __str__(self):
        fp = FishingPlace.objects.filter(fishing=self)
        try:
            fp = str(fp[0])
        except IndexError:
            fp = 'Рыбалка '
        
        return  fp + ' ' + str(self.date) + ': ' + str(self.time_start)[:5] + (' (запланировано)' if self.planned else '')

    def set_planned(self):
        """
        Поверяет дату проведения рыбалки и текущую дату,
        с выставлением статуса "Запланировано"
        """
        if self.date > datetime.now().date():
            self.planned = True
        else:
            self.planned = False
    
    def unique(self):
        fishing_list = Fishing.objects.filter(owner=self.owner)
        for fishing in fishing_list:
            if fishing.id != self.id:
                if (fishing.date == self.date and
                fishing.time_start == self.time_start and
                fishing.time_end == self.time_end):
                    return False
            else:
                break
        return True

    def get_trophys(request):
        result = {}
        result['fish'] = []
        result['weight'] = []
        result['fishing'] = []
        fishings = Fishing.objects.filter(owner=request.user)
        for fishing in fishings:
            try:
                fishing_trophys = FishingTrophy.objects.filter(fishing=fishing)
            except:
                fishing_trophys = None
            if fishing_trophys:
                for fishing_trophy in fishing_trophys:
                    result['fish'].append(str(fishing_trophy.fish))
                    result['weight'].append(str(fishing_trophy.fish_trophy_weight))
                    result['fishing'].append(fishing_trophy.fishing.id)
        return result


class FishingReportsSettings(models.Model):
    
    self_id = models.CharField(max_length=50)
    fishing_id = models.IntegerField()
    fisherman = models.BooleanField(default=True,
                                    verbose_name='Ник рыбака')
    time_start = models.BooleanField(default=True,
                                     verbose_name='Время начала')
    time_end = models.BooleanField(default=True,
                                   verbose_name='Время окончания')
    place_water = models.BooleanField(default=True,
                                      verbose_name='Водоём')
    place_locality = models.BooleanField(default=True,
                                         verbose_name='Населенный пункт')
    place_name = models.BooleanField(default=True,
                                     verbose_name='Название места')
    place_coordinate = models.BooleanField(default=True,
                                           verbose_name='Координаты места')
    weather = models.BooleanField(default=True,
                                  verbose_name='Погода')
    tackle = models.BooleanField(default=True,
                                 verbose_name='Снасти')
    montage = models.BooleanField(default=True,
                                  verbose_name='Монтажи')
    trough = models.BooleanField(default=True,
                                 verbose_name='Кормушки')
    leash = models.BooleanField(default=True,
                                verbose_name='Лески')
    crochet = models.BooleanField(default=True,
                                  verbose_name='Крючки')
    nozzle = models.BooleanField(default=True,
                                 verbose_name='Наживки')
    pace = models.BooleanField(default=True,
                               verbose_name='Темп')
    lure = models.BooleanField(default=True,
                               verbose_name='Прикормы или их смеси')
    result = models.BooleanField(default=True,
                                 verbose_name='Улов')
    trophy = models.BooleanField(default=True,
                                 verbose_name='Трофеи')
    note = models.BooleanField(default=True,
                               verbose_name='Заметки')

    def report_place(self, *args, **kwargs):
        try:
            fishing_place = FishingPlace.objects.get(fishing=kwargs['fishing'])
            report=kwargs['report']
            report['place'] = {}
        except:
            fishing_place = False
        if fishing_place:
            if self.place_water:
                report['place']['water'] = fishing_place.place.water.__str__()
            if self.place_locality:
                report['place']['locality'] = fishing_place.place.locality.__str__()
            if self.place_name:
                report['place']['name'] = fishing_place.place.name.__str__()
            if self.place_coordinate:
                report['place']['coordinate'] = fishing_place.place.coordinates()
            del(fishing_place)
    
    def report_weather(self, *args, **kwargs):
        try:
            fishing_weather = FishingWeather.objects.get(fishing=kwargs['fishing'])
            weather = fishing_weather.weather
            report = kwargs['report']
            report['weather'] = {}
            del(fishing_weather)
        except:
            weather = False
        if weather:
            if weather.overcast:
                report['weather']['overcast'] = weather.overcast.__str__()
            if weather.conditions:
                report['weather']['conditions'] = weather.conditions.__str__()
            if weather.temperature:
                report['weather']['temperature'] = weather.temperature.__str__()
            if weather.pressure:
                report['weather']['pressure'] = weather.pressure.__str__()
            if weather.direction_wind:
                report['weather']['direction_wind'] = weather.direction_wind.__str__()
            if weather.wind_speed:
                report['weather']['wind_speed'] = weather.wind_speed.__str__()
            if weather.lunar_day:
                report['weather']['lunar_day'] = weather.lunar_day.__str__()
        del(weather)
    
    def report_montage(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['montage'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_montage = FishingMontage.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['montage'].append('')
                continue
            montage = fishing_montage.montage
            report['tackles']['montage'].append(montage.__str__())
        for_delete = True
        for montage in report['tackles']['montage']:
            if montage != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('montage')
    
    def report_trough(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['trough'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_trough = FishingTrough.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['trough'].append('')
                continue
            report['tackles']['trough'].append(fishing_trough.trough.__str__())
        for_delete = True
        for trough in report['tackles']['trough']:
            if trough != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('trough')
    
    def report_leash(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['leash'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_leash = FishingLeash.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['leash'].append('')
                continue
            report['tackles']['leash'].append(fishing_leash.leash.__str__())
        for_delete = True
        for leash in report['tackles']['leash']:
            if leash != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('leash')
    
    def report_crochet(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['crochet'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_crochet = FishingCrochet.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['crochet'].append('')
                continue
            report['tackles']['crochet'].append(fishing_crochet.crochet.__str__())
        for_delete = True
        for crochet in report['tackles']['crochet']:
            if crochet != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('crochet')
    
    def report_nozzle(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['nozzle'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_nozzle = FishingNozzle.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['nozzle'].append('')
                continue
            report['tackles']['nozzle'].append(fishing_nozzle.nozzle_base.__str__())
        for_delete = True
        for nozzle in report['tackles']['nozzle']:
            if nozzle != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('nozzle')
    
    def report_pace(self, *args, **kwargs):
        report = kwargs['report']
        report['tackles']['pace'] = []
        fishing_tackles = kwargs['fishing_tackles']
        for fishing_tackle in fishing_tackles:
            try:
                fishing_pace = FishingPace.objects.get(fishing_tackle=fishing_tackle)
            except:
                report['tackles']['pace'].append('')
                continue
            report['tackles']['pace'].append(fishing_pace.pace.__str__())
        for_delete = True
        for pace in report['tackles']['pace']:
            if pace != '':
                for_delete = False
        if for_delete:
            report['tackles'].pop('pace')
    
    def report_tackle(self, *args, **kwargs):
        try:
            fishing_tackles = FishingTackle.objects.filter(fishing=kwargs['fishing'])
            report = kwargs['report']
            report['tackles'] = {}
        except:
            fishing_tackles = False
        if fishing_tackles:
            if self.tackle:
                report['tackles']['tackle'] = []
                for fishing_tackle in fishing_tackles:
                    report['tackles']['tackle'].append(fishing_tackle.tackle.__str__())
            if self.montage:
                self.report_montage(report=report, fishing_tackles=fishing_tackles)
            if self.trough:
                self.report_trough(report=report, fishing_tackles=fishing_tackles)
            if self.leash:
                self.report_leash(report=report, fishing_tackles=fishing_tackles)
            if self.crochet:
                self.report_crochet(report=report, fishing_tackles=fishing_tackles)
            if self.nozzle:
                self.report_nozzle(report=report, fishing_tackles=fishing_tackles)
            if self.pace:
                self.report_pace(report=report, fishing_tackles=fishing_tackles)
    
    def report_lure(self, *args, **kwargs):
        try:
            fishing_luremix = FishingLureMix.objects.get(fishing=kwargs['fishing'])
            lure_mix = fishing_luremix.lure_mix
            del(fishing_luremix)
            report = kwargs['report']
        except:
            lure_mix = False
        try:
            lure = FishingLure.objects.get(fishing=kwargs['fishing'])
            report = kwargs['report']
        except:
            lure = False
        if lure_mix:
            report['luremix'] = {}
            report['luremix']['lures'] = []
            report['luremix']['aromas'] = []
            report['luremix']['nozzles'] = []
            lures = Lure.objects.filter(mix=lure_mix)
            for lure in lures:
                report['luremix']['lures'].append(lure.__str__())
            del(lures)
            aromas = Aroma.objects.filter(mix=lure_mix)
            for aroma in aromas:
                report['luremix']['aromas'].append(aroma.__str__())
            del(aromas)
            nozzles = Nozzle.objects.filter(mix=lure_mix)
            for nozzle in nozzles:
                report['luremix']['nozzles'].append(nozzle.__str__())
            del(nozzles)
            if len(report['luremix']['lures']) == 0:
                report['luremix'].pop('lures')
            if len(report['luremix']['aromas']) == 0:
                report['luremix'].pop('aromas')
            if len(report['luremix']['nozzles']) == 0:
                report['luremix'].pop('nozzles')
        elif lure:
            report['lure'] = lure.__str__()
    
    def report_fishs(self, *args, **kwargs):
        try:
            fishing_results = FishingResult.objects.filter(fishing=kwargs['fishing'])
            report = kwargs['report']
            report['fishs'] = []
        except:
            fishing_results = False
        if fishing_results:
            for fishing_result in fishing_results:
                report['fishs'].append(fishing_result.__str__())
        del(fishing_results)
    
    def report_trophys(self, *agrs, **kwargs):
        try:
            fishing_trophys = FishingTrophy.objects.filter(fishing=kwargs['fishing'])
            report = kwargs['report']
            report['trophys'] = []
        except:
            fishing_trophys = False
        if fishing_trophys:
            for fishing_trophy in fishing_trophys:
                report['trophys'].append(fishing_trophy.__str__())
        del(fishing_trophys)
    
    def report(self, *args, **kwargs):
        report = {}
        fishing = get_object_or_404(Fishing, pk=self.fishing_id)
        report['date'] = fishing.date
        if self.fisherman:
            report['fisherman'] = fishing.owner.nick
        if self.time_start:
            report['time_start'] = fishing.time_start
        if self.time_end:
            report['time_end'] = fishing.time_end
        if (self.place_water or self.place_name or
                self.place_coordinate or self.place_locality):
            self.report_place(report=report, fishing=fishing)
        if self.weather:
            self.report_weather(report=report, fishing=fishing)
        if (self.tackle or self.montage or
                self.trough or self.leash or
                self.crochet or self.nozzle or
                self.pace):
            self.report_tackle(report=report, fishing=fishing)
        if self.lure:
            self.report_lure(report=report, fishing=fishing)
        if self.result:
            self.report_fishs(report=report, fishing=fishing)
        if self.trophy:
            self.report_trophys(report=report, fishing=fishing)
        if self.note:
            report['note'] = str(fishing.note)
        return report

    def get_trophy(request):
        def combine_result(*args, **kwargs):
            if pre_result['fish'] in result['fish']:
                pos = result['fish'].index(pre_result['fish'])
                if pre_result['weight'] > result['weight'][pos]:
                    result['weight'][pos] = pre_result['weight']
                    result['fisherman'][pos] = pre_result['fisherman']
                    result['water'][pos] = pre_result['water']
                    result['date'][pos] = pre_result['date']
            else:
                result['fish'].append(pre_result['fish'])
                result['weight'].append(pre_result['weight'])
                result['fisherman'].append(pre_result['fisherman'])
                result['water'].append(pre_result['water'])
                result['date'].append(pre_result['date'])
        result = {'fish': [],
                  'weight': [],
                  'fisherman': [],
                  'water': [],
                  'date': []}
        try:
            fishing_reports = FishingReportsSettings.objects.filter(trophy=True)
        except:
            fishing_reports = None
        if fishing_reports:
            for fishing_report in fishing_reports:
                fishing = Fishing.objects.get(id=fishing_report.fishing_id)
                if fishing.owner != request.user:
                    try:
                        fishing_trophys = FishingTrophy.objects.filter(fishing=fishing)
                    except:
                        fishing_trophys = None
                    if fishing_trophys:
                        for fishing_trophy in fishing_trophys:
                            pre_result = {}
                            pre_result['date'] = str(fishing.date)
                            if fishing_report.fisherman:
                                pre_result['fisherman'] = str(fishing.owner.nick)
                            else:
                                pre_result['fisherman'] = ''
                            if fishing_report.place_water:
                                try:
                                    fishing_place = FishingPlace.objects.get(fishing=fishing)
                                except:
                                    fishing_place = None
                                if fishing_place:
                                    pre_result['water'] = str(fishing_place.place.water)
                                else:
                                    pre_result['water'] = ''
                            else:
                                pre_result['water'] = ''
                            pre_result['fish'] = str(fishing_trophy.fish.name)
                            pre_result['weight'] = str(fishing_trophy.fish_trophy_weight)
                            combine_result()
        return result


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


class FishingLure(models.Model):
    class Meta:
        verbose_name = "Прикорм использованный в рыбалке"
        verbose_name_plural = "Прикормы использованные в рыбалке"
        
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к рыбалке
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.PROTECT,
                                verbose_name='Рыбалка')
    # Привязка к прикорму
    lure_base = models.ForeignKey('LureBase',
                                  on_delete=models.PROTECT,
                                  verbose_name='Прикорм')
    # Вес базового прикорма
    weight = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 blank=True,
                                 verbose_name="Доля прикорма",
                                 help_text="Укажите долю прикорма в смеси")
    
    def __str__(self):
        return str(self.lure_base) + '\nВес прикрома: ' + str(self.weight) + 'кг.'


class FishingLureMix(models.Model):  # Прикормочный состав для рыбалки
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


class FishingPlace(models.Model):  # Место рыбалки
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
    
    def __str__(self):
        return str(self.place)


# class FishingPoint(models.Model):  # Точки ловли
#     """
#     Содежит информацию о точке ловли, возможно использование
#     в нескольких рыбалках
#     """
#     class Meta:
#         verbose_name = "Точка ловли"
#         verbose_name_plural = "Точки ловли"
#         ordering = ['fishing_point_distance', ]
#     # Владелец записи
#     owner = models.ForeignKey(CustomUser,
#                               on_delete=models.PROTECT,
#                               verbose_name="Владелец записи")
#     # Привязка к месту
#     place = models.OneToOneField('Place',
#                                  on_delete=models.PROTECT,
#                                  verbose_name='Место ловли')
#     # Азимут заброса
#     fishing_point_azimuth = models.PositiveIntegerField(
#         default=0,
#         verbose_name="Азимут")
#     # Дистанция до точки ловли
#     fishing_point_distance = models.PositiveIntegerField(
#         default=0,
#         verbose_name="Дистанция")
#     # Глубина в точке ловли
#     fishing_poiny_depth = models.DecimalField(
#         max_digits=4,
#         decimal_places=2,
#         default=0,
#         blank=True,
#         verbose_name="Глубина")
#     # Грунт в точке ловли
#     priming = models.ForeignKey(
#         'Priming',
#         on_delete=models.PROTECT,
#         verbose_name="Грунт"
#     )

#     def __str__(self):
#         return (str(self.priming) + 'Дистанция: ' +
#                 str(self.fishing_point_distance) + 'м.')


class FishingResult(models.Model):  # Результат рыбалки
    """
    Содержит информацию о результате рыбалки, принимает
    в себя несколько значений пойманной рыбы
    """
    class Meta:
        verbose_name = "Результат рыбалки"
        verbose_name_plural = "Результат рыбалок"
        ordering = ['id', ]
    # Привязка к рыбалке, т.к. может быть несколько вариантов
    # то именное модель результатов привязываем, а не на
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # оборот
    fishing = models.ForeignKey('Fishing',
                                on_delete=models.CASCADE,
                                verbose_name="Рыбалка")
    # Рыба
    fish = models.ForeignKey('Fish',
                             blank=True,
                             null=True,
                             on_delete=models.PROTECT,
                             verbose_name="Рыба")
    # Количество хвостов
    number_of_fish = models.PositiveIntegerField(blank=True,
                                                 null=True,
                                                 verbose_name="Количество рыб, шт.")
    # Масса улова по выбранной рыбе
    fish_weight = models.DecimalField(max_digits=6,
                                      decimal_places=3,
                                      blank=True,
                                      null=True,
                                      verbose_name="Вес улова, кг.")

    def __str__(self):
        return (str(self.fish) + ': ' + ((str(self.number_of_fish) + 'шт. ') if self.number_of_fish else '') +
                ((str(self.fish_weight) + 'кг.') if self.fish_weight else ''))


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


class FishingTrophy(models.Model):  # Трофей рыбалки
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
    fish = models.ForeignKey('Fish',
                             on_delete=models.PROTECT,
                             blank=True,
                             null=True,
                             verbose_name="Рыба")
    # Вес трофея
    fish_trophy_weight = models.DecimalField(max_digits=4,
                                             blank=True,
                                             decimal_places=2,
                                             verbose_name="Вес трофея, кг.")
    #fish_trophy_photo=models.ImageField(verbose_name="Фото трофея")

    def __str__(self):
        return 'Трофей: ' + str(self.fish) + ' ' + str(self.fish_trophy_weight) + 'кг.'


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
        verbose_name = 'Погода во время рыбалки'
        verbose_name_plural = 'Погода во время рыбалки'
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


class Leash(models.Model):  # Поводки
    """
    Содержит информацию о поводках
    """
    class Meta:
        verbose_name = "Поводок"
        verbose_name_plural = "Поводки"
        ordering = ['material', 'diameter', 'length', ]
    # Владелец записи
    owner = models.ForeignKey(CustomUser,
                              on_delete=models.PROTECT,
                              verbose_name="Владелец записи")
    # Поводочный материал
    material = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Материал поводка")
    # Диаметр поводочного материала
    diameter = models.DecimalField(
        max_digits=4,
        decimal_places=3,
        blank=True,
        verbose_name="Диаметр поводка, мм")
    # Длина поводка
    length = models.PositiveIntegerField(blank=True,
                                         verbose_name="Длина поводка, см")

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
        ordering = ['base', 'weight', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Связь с прикормочной смесью
    mix = models.ForeignKey(
        'LureMix',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    # Связь с базовым прикормом
    base = models.ForeignKey(
        'LureBase',
        on_delete=models.PROTECT,
        verbose_name="Базовый прикорм")
    # Вес базового прикорма
    weight = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 blank=True,
                                 verbose_name="Доля прикорма",
                                 help_text="Укажите долю прикорма в смеси")

    def __str__(self):
        return str(self.base) + ' ' + str(self.weight) + 'кг.'


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
        blank=True,
        verbose_name="Название")

    def __str__(self):
        return self.manufacturer + ' ' + self.name

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if self.manufacturer:
            self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
            self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        if self.name:
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
        ordering = ['name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Название состава
    name = models.CharField(max_length=100,
                            blank=True,
                            verbose_name='Название состава')
    description = models.TextField(blank=True,
                                   verbose_name='Описание состава')

    
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
        lure_mix_list = LureMix.objects.filter(owner=self.owner)
        for lure_mix in lure_mix_list:
            if (lure_mix.id != self.id and
                lure_mix.name.lower() == self.name.lower()):
                    return False
        else:
            return True


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
        blank=True,
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
    base = models.ForeignKey('NozzleBase',
                                    on_delete=models.PROTECT,
                                    verbose_name='Насадка/наживка')
    # Состояние
    state = models.ForeignKey('NozzleState',
                              on_delete=models.PROTECT,
                              blank=True,
                              null=True,
                              verbose_name='Состояние наживки/насадки')
    # Связь с прикормочной смесью
    mix = models.ForeignKey(
        'LureMix',
        on_delete=models.PROTECT,
        verbose_name="Прикормочная смесь")
    
    def __str__(self):
        return str(self.base) + ' ' + str(self.state)


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
    size = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Размер насадки, мм")
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
            return (self.manufacturer + ' ' + self.name + ' ' +
                    ((str(self.size) + 'мм.') if self.size != None else '') +
                    ('\nТип: ' + str(self.ntype) if self.ntype != None else ''))

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
        blank=True,
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
        ordering = ['name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Привязка к водоему
    water = models.ForeignKey(
        'Water',
        on_delete=models.PROTECT,
        verbose_name="Водоём")
    # Ближайший населенный пункт
    locality = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Ближайший населенный пункт",
        help_text="Название ближайшего населенного пункта")
    # Название места
    name = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Место",
        help_text='Название места')
    # Координа места рыбалки, градусы северной широты от -90 до 90
    latitude = models.DecimalField(max_digits=8,
                                   decimal_places=6,
                                   blank=True,
                                   null=True,
                                   help_text="-90 <> 90",
                                   verbose_name="Широта")
    # Координа места рыбалки, минуты северной широты от 0 до 60
    longitude = models.DecimalField(max_digits=9,
                                    decimal_places=6,
                                    blank=True,
                                    null=True,
                                    help_text="-180 <> 180",
                                    verbose_name="Долгота")

    def __str__(self):
        return ((self.locality + '. ') if self.locality else '') + self.name

    def coordinates(self):
        if self.latitude and self.longitude:
            return 'с.ш.' + str(self.latitude) + ' в.д.' + str(self.longitude)
        return False
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.name = str(self.name[0].upper()) + self.name[1:]
        self.name = re.sub(r'\s+', ' ', self.name)
        if len(self.locality) != 0:
            self.locality = str(self.locality[0].upper()) + self.locality[1:]
            self.locality = re.sub(r'\s+', ' ', self.locality)

    def unique(self):
        """
        Проверка на уникальность по названию и местоположению
        """
        place_list = Place.objects.filter(owner=self.owner)
        
        for place in place_list:
            if place.id != self.id:
                if (place.locality.lower() == self.locality.lower() and
                    place.water == self.water and
                    place.name.lower() == self.name.lower()):
                    return False
            else:
                break
        return True
    
    def unique_coordinates(self):
        """
        Проверка координат на уникальность
        """
        place_list = Place.objects.filter(owner=self.owner)
        
        for place in place_list:
            if place.id != self.id:
                if (place.latitude == self.latitude and
                    place.longitude == self.longitude):
                    return False
            else:
                break
        return True

    def add_full(request):
        pass


# class Point(models.Model):  # Точки карт дна
#     """
#     Содержит информацию о маркерной точке, привязывается
#     к маркерной карте. Информация о грунте возмоно выбор
#     из списка
#     """
#     class Meta:
#         verbose_name = "Точка карты дна"
#         verbose_name_plural = "Точки карт дна"
#         ordering = ['point_azimuth', 'point_distance', ]
#     # Владелец записи
#     owner = models.ForeignKey(
#         CustomUser,
#         on_delete=models.PROTECT,
#         verbose_name="Владелец записи")
#     # Привязка к маркерной карте
#     bottom_map = models.ForeignKey(
#         'BottomMap',
#         on_delete=models.CASCADE,
#         verbose_name="Карта дна")
#     # Азимут луча (по компасу)
#     point_azimuth = models.PositiveIntegerField(
#         default=0,
#         validators=[
#             MaxValueValidator(359),
#             MinValueValidator(0)
#         ],
#         verbose_name="Азимут")
#     # Дистанций до точки
#     point_distance = models.PositiveIntegerField(
#         default=0,
#         verbose_name="Дистанция")
#     # Глубина в точке
#     point_depth = models.DecimalField(
#         max_digits=4,
#         decimal_places=2,
#         default=0,
#         blank=True,
#         verbose_name="Глубина")
#     # Грунт
#     priming = models.ForeignKey(
#         'Priming',
#         on_delete=models.PROTECT,
#         verbose_name="Грунт")

#     def __str__(self):
#         return (str(self.bottom_map) + ': ' + str(self.point_azimuth) +
#                 ' ' + str(self.point_distance))


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
        ordering = ['manufacturer', 'model_tackle',
                    'length', 'casting_weight', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Производитель снасти
    manufacturer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Производитель")
    # Инормация о используемой снасти
    model_tackle = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Название")
    length = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        verbose_name="Длина, м",
        validators=[MinValueValidator(0.0), MaxValueValidator(99.9)])
    casting_weight = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Тест удилища, гр")

    def __str__(self):
        return (((self.manufacturer + ' ') if self.manufacturer else '') +
                ((self.model_tackle + ' ') if self.model_tackle else '') +
                ((str(self.length) + 'м. ') if self.length else '') +
                ((str(self.casting_weight) + 'гр.') if self.casting_weight else ''))

    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        if self.manufacturer:
            self.manufacturer = str(self.manufacturer[0].upper()) + self.manufacturer[1:]
            self.manufacturer = re.sub(r'\s+', ' ', self.manufacturer)
        if self.model_tackle:
            self.model_tackle = str(self.model_tackle[0].upper()) + self.model_tackle[1:]
            self.model_tackle = re.sub(r'\s+', ' ', self.model_tackle)
    
    def unique(self):
        """
        Проверка записи на уникальность для пользователя
        """
        tackle_list = Tackle.objects.filter(owner=self.owner)
        for tackle in tackle_list:
            if (tackle.id != self.id and
                tackle.manufacturer.lower() == self.manufacturer.lower() and
                tackle.model_tackle.lower() == self.model_tackle.lower() and
                tackle.length == self.length and
                tackle.casting_weight == self.casting_weight):
                    return False
        else:
            return True


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
        blank=True,
        null=True,
        verbose_name="Вес кормушки, гр")

    def __str__(self):
        return (self.manufacturer + ' ' + str(self.model_name) + ' ' +
                str(' пластик' if self.plastic else '') + ' ' +
                ('(' + str(self.feed_capacity) + ' кормоёмкость' + ')' if self.feed_capacity else '')+
                str(' с грунтозацепами' if self.lugs else '') +
                ' ' + ((str(self.weight) + 'гр.') if self.weight else ''))

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
        ordering = ['name', ]
    # Владелец записи
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    # Категория водоема
    category = models.ForeignKey(
        'WaterCategory',
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        verbose_name="Категория водоёма")
    # Название водоема
    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Название водоёма")

    def __str__(self):
        return ((self.category.abbreviation + '. ') if self.category else '') + self.name

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
        water_list = Water.objects.filter(owner=self.owner)
        for water in water_list:
            if water.id != self.id:
                if (water.name.lower() == self.name.lower() and
                    water.category == self.category):
                    return False
        else:
            return True


class WaterCategory(models.Model):
    """
    Категории водоемов
    """
    
    class Meta:
        verbose_name = "Категория водоёма"
        verbose_name_plural = "Категории водоёмов"
        ordering = ['category',]
    category = models.CharField(max_length=20,
                                blank=True,
                                verbose_name="Категория")
    abbreviation = models.CharField(max_length=20,
                                    blank=True,
                                    verbose_name="Аббревиатура")
    
    def __str__(self):
        return self.category + ' (' + self.abbreviation + ')'
    
    def first_upper(self):
        """
        Первая буква названия всегда заглавная
        """
        self.category = str(self.category[0].upper()) + self.category[1:]
        self.category = re.sub(r'\s+', ' ', self.category)

    def getabbreviation(self):
        """
        Добавляет аббривиатуру, если она не внесена в форме
        по первой букве названия, аббривиатура всегда маленькими буквами.
        Если внесена, преводит все в нижний регистр
        """
        if len(self.abbreviation ) == 0:
            self.abbreviation = self.category[0].lower()
        else:
            self.abbreviation = self.abbreviation.lower()
        
    def unique(self):
        """
        Проверка записи на уникальность
        """
        water_category_list = WaterCategory.objects.all()
        for water_category in water_category_list:
            if water_category.id != self.id:
                if (water_category.category.lower() == self.category.lower() or
                    water_category.abbreviation.lower() == self.abbreviation.lower()):
                    return False
        else:
            return True


class Weather(models.Model):  # Погода
    """
    Содержит сводные сведения о погоде
    опираясь на ручной ввод
    """
    class Meta:
        verbose_name = "Погода"
        verbose_name_plural = "Погода"
        ordering = ['date', ]
    # Дата погоды
    date = models.DateField(
        auto_now_add=False,
        verbose_name="Дата")
    # Облачность
    overcast = models.ForeignKey('Overcast',
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 verbose_name="Облачность")
    # Связь с таблицей "Явления погоды"
    conditions = models.ForeignKey('Conditions',
                                   on_delete=models.PROTECT,
                                   blank=True,
                                   null=True,
                                   verbose_name="Явления погоды")
    # Температура воздуха
    temperature = models.DecimalField(max_digits=4,
                                      decimal_places=1,
                                      blank=True,
                                      null=True,
                                      verbose_name="Температура воздуха")
    # Давление
    pressure = models.PositiveIntegerField(blank=True,
                                           null=True,
                                           verbose_name="Давление")
    # Направление ветра
    direction_wind = models.CharField(max_length=30,
                                      blank=True,
                                      verbose_name="Направление ветра")
    # Скорость ветра
    wind_speed = models.DecimalField(max_digits=3,
                                     decimal_places=1,
                                     blank=True,
                                     null=True,
                                     verbose_name="Скорость ветра")
    # Лунный день
    lunar_day = models.PositiveIntegerField(blank=True,
                                            null=True,
                                            verbose_name="Лунный день")

    def __str__(self):
        return str(self.date)

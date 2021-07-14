from django.db.models import fields
from .models import Aroma, FishingLureMix
from .models import AromaBase
# from .models import BottomMap
from .models import Conditions
from .models import Crochet
# from .models import District
from .models import FeedCapacity
from .models import Fish
from .models import Fishing
from .models import FishingLure
# from .models import FishingPoint
from .models import FishingReportsSettings
from .models import FishingResult
from .models import FishingTrophy
from .models import Leash
from .models import Lure
from .models import LureBase
from .models import LureMix
from .models import Montage
from .models import Nozzle
from .models import NozzleBase
from .models import NozzleState
from .models import NozzleType
from .models import Overcast
from .models import Pace
from .models import Place
# from .models import Point
from .models import Priming
from .models import Tackle
from .models import Trough
from .models import Water
from .models import WaterCategory
from .models import Weather

from django import forms
import re

no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                      '№', ';', ':', '?', '<', '>', '/', '|', "'",
                      "`"]

no_valid_char_error_end = ' не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'

# AromaFormErrors
volume_aroma_is_null = 'Необходимо указать объём аромы'
volume_aroma_is_negative = 'Объём аромы должен быть больше 0'

# AromaBaseErrors
manufacturer_and_name_aroma_base_is_empty = 'Название производителя или название аромы должно быть заполнено'
manufacturer_aroma_base_no_valid_char = 'Название производителя' +no_valid_char_error_end
name_aroma_base_no_valid_char = 'Название аромы' + no_valid_char_error_end

# CrochetFormErrors
size_is_empty = 'Укажите размер крючка'
manufacturer_crochet_no_valid_char = 'Название производителя' + no_valid_char_error_end
model_crochet_no_valid_char = 'Название модели' + no_valid_char_error_end

# FishingFormErrors
time_start_and_end_equal = 'Время начала и окончания рыбалки не могут быть равны'
time_start_more_time_end = 'Время окончания рыбалки должно быть больше времени начала'

# FishingResultFormErrors
fishing_result_fish_not_select = 'Выбирете рыбу'
fishing_result_number_of_fish_is_empty = 'Укажите количество рыб'

# FishingTrophyFormErrors
fishing_trophy_fish_is_empty = 'Выберите рыбу'
fishing_trophy_weight_is_empty = 'Укажите вес трофея'

# LeashFormErrors
leash_material_empty = 'Укажите материал поводка'
leash_diameter_empty = 'Укажите диаметр поводка'
leash_length_empty = 'Укажите длину поводка'
leash_no_valid_char_error = 'Название поводочного материала' + no_valid_char_error_end

# LureFormErrors
weight_lure_is_null = 'Необходимо указать долю пркорма'
weight_lure_is_negative = 'Доля прикорма должна быть больше 0'

# LureBaseFormErrors
manufacturer_and_name_lure_base_is_empty = 'Название производителя или название прикорма должно быть заполнено'
manufacturer_lure_base_no_valid_char = 'Название производителя' + no_valid_char_error_end
name_lure_base_no_valid_char = 'Название прикорма' + no_valid_char_error_end

# LureMixFormErrors
lure_mix_name_is_empty = 'Укажите название смеси'
lure_mix_name_no_valid_char = 'Название смеси' + no_valid_char_error_end

# MoontageFormErrors
montage_name_is_empty = 'Укажите название монтажа'
montage_name_no_valid_char = 'Название монтажа' + no_valid_char_error_end

# NozzleBaseFormErrors
manufacturer_and_name_nozzle_is_empty = 'Название производителя или название насадки должно быть указано'
manufacturer_nozzle_no_valid_char = 'Название производителя' + no_valid_char_error_end
name_nozzle_no_valid_char = 'Название насадки' + no_valid_char_error_end
size_nozzle_is_negative = 'Размер насадки должен быть больше 0'

# NozzleStateFormErrors
state_nozzle_is_empty = 'Укажите состояние наживки'
state_nozzle_no_valid_char = 'Состояние' + no_valid_char_error_end

# BaitBaseFormErrors
manufacturer_and_name_bait_is_empty = 'Название производителя или название наживки должно быть указано'
manufacturer_bait_no_valid_char = 'Название производителя' + no_valid_char_error_end
name_bait_no_valid_char = 'Название наживки' + no_valid_char_error_end

# PlaceFormErrors
name_place_is_empty = 'Название места не может быть пустым'
name_place_no_valid_char = 'Название места' + no_valid_char_error_end
locality_place_no_valid_char = 'Название населенного пункта' + no_valid_char_error_end

# TackleFormErrors
tackle_manufacturer_and_model_is_empty = 'Производитель или название должны быть указаны'
tackle_manufacturer_no_valid_char = 'Название производителя' + no_valid_char_error_end
tackle_model_no_valid_char = 'Название модели' + no_valid_char_error_end

# TroughFormErrors
trough_manufacturer_and_model_is_empty = 'Производитель или модель должны быть указаны'
trough_manufacturer_no_valid_char = 'Название производтеля' + no_valid_char_error_end
trough_model_no_valid_char = 'Название модели' + no_valid_char_error_end

# WaterFormErrors
name_water_is_empty = 'Необходимо указать название водоёма'
name_water_no_valid_char = 'Название водоёма' + no_valid_char_error_end

# WeatherFormErrors
# Предельные значения температуры воздуха
weather_min_temperature = -60
weather_max_temperature = 60
weather_min_pressure = 650
weather_max_pressure = 860
weather_form_fields_is_empty = 'Хотя бы одно поле должно иметь значение'
weather_direction_wind_no_valid_char = 'Направление ветра' + no_valid_char_error_end
weather_temperature_is_low = 'Темепература воздуха не может быть ниже ' + str(weather_min_temperature)
weather_temperature_is_high = 'Темепература воздуха не может быть выше ' + str(weather_max_temperature)
weather_pressure_is_low = 'Атмосферное давление не может быть ниже ' + str(weather_min_pressure)
weather_pressure_is_high = 'Атмосферное давление не может быть выше ' + str(weather_max_pressure)
weather_wind_speed_is_negative = 'Сокрость ветра не может быть меньше 0'
weather_wind_speed_is_high = 'Скорость ветра не может быть больше 100 м/с'

class AromaForm(forms.ModelForm):
    class Meta:
        model = Aroma
        fields = ['volume', ]

    def clean(self):
        volume = self.cleaned_data.get('volume')
        
        if volume == None:
            self.add_error('volume', volume_aroma_is_null)
        elif volume <= 0:
            self.add_error('volume', volume_aroma_is_negative)
        
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = Aroma
        self_form = AromaForm
        try:
            fishing = Fishing.objects.get(id=kwargs['fishing_id'])
            fishing_lure_mix = FishingLureMix.objects.get(fishing=fishing)
            lure_mix = fishing_lure_mix.lure_mix
        except:
            try:
                lure_mix = LureMix.objects.get(id=kwargs['lure_mix_id'])
            except:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        if not lure_mix.editable():
            form = self_form(request.POST)
            form.add_error(None, 'Состав нельзя изменять')
            return form
        try:
            model = self_model.objects.get(id=kwargs['aroma_id'])
            if model.owner == request.user:
                aroma_base = model.base
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            aroma_base = AromaBase.objects.get(id=kwargs['aroma_base_id'])
            form = self_form(request.POST)
        if lure_mix.owner == aroma_base.owner:
            if form.is_valid():
                model = form.save(commit=False)
                model.owner = request.user
                model.mix = lure_mix
                model.base = aroma_base
                model.save()
                return model.id
        else:
            form = self_form(request.POST)
            form.add_error(None, 'Что-то пошло не так')
        return form


class AromaBaseForm(forms.ModelForm):
    class Meta:
        model = AromaBase
        fields = ['manufacturer', 'name', ]

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        
        if len(manufacturer) == 0 and len(name) ==0:
            self.add_error(None, manufacturer_and_name_aroma_base_is_empty)
        
        manufacturer_errors = False
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not name_errors:
                if not manufacturer_errors and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', manufacturer_aroma_base_no_valid_char)
                    
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_aroma_base_no_valid_char)
            else:
                break
        return super().clean()
    
    def save_me(request, *args, **kwargs):
        self_model = AromaBase
        self_form = AromaBaseForm
        kwargs_field = 'aroma_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такая арома уже добавлен')
        return form


# class BottomMapForm(forms.ModelForm):
#     date = forms.DateField(
#         input_formats=['%d.%m.%Y'],
#         widget=forms.DateInput(attrs={
#             'class': 'form-control datetimepicker-input',
#             'data-target': '#datetimepicker1'
#         })
#     )
    
#     class Meta:
#         model = BottomMap
#         fields = ['date',]


class ConditionsForm(forms.ModelForm):
    class Meta:
        model = Conditions
        fields = ('name',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        conditions_list = Conditions.objects.all()
        for condition in conditions_list:
            if condition.name.lower() == name.lower():
                form_saved=self.save(commit=False)
                if condition.id != form_saved.id:
                    self.add_error('name', 'Такое погодное явление уже добавлена')
        
        msg = 'Название погодного явления не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class CrochetForm(forms.ModelForm):
    class Meta:
        model = Crochet
        fields = ['manufacturer', 'model', 'size', ]

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        model = self.cleaned_data.get('model')
        size = self.cleaned_data.get('size')
        
        manufacturer_errors = False
        model_errors = False

        if size == None:
            self.add_error('size', size_is_empty)
        
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not model_errors:
                if not manufacturer_errors and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', manufacturer_crochet_no_valid_char)
                if not model_errors and model.startswith(no_valid_char) or model.endswith(no_valid_char):
                    model_errors = True
                    self.add_error('model', model_crochet_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = Crochet
        self_form = CrochetForm
        kwargs_field = 'crochet_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такой Крючок уже добавлен')
        return form


# class DistrictForm(forms.ModelForm):
#     class Meta:
#         model = District
#         fields = ('district_name',)


class FeedCapacityForm(forms.ModelForm):
    class Meta:
        model = FeedCapacity
        fields = ('name',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        capacity_list = FeedCapacity.objects.all()
        for capacity in capacity_list:
            if capacity.name.lower() == name.lower():
                form_saved=self.save(commit=False)
                if capacity.id != form_saved.id:
                    self.add_error('name', 'Такая кормоёмкость уже добавлена')
        
        msg = 'Название кормоёмкости не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class FishForm(forms.ModelForm):

    class Meta:
        model = Fish
        fields = ('name', 'description', )
    
    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        fish_list = Fish.objects.all()
        for fish in fish_list:
            if fish.name.lower() == name.lower():
                form_saved=self.save(commit=False)
                if fish.id != form_saved.id:
                    self.add_error('name', 'Такая рыба уже добавлена')
        
        msg = 'Название рыбы не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'

        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class FishingForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        label='Дата рыбалки'
    )
    time_start = forms.TimeField(
        input_formats=['%H:%M'],
        label='Время начала'
    )
    time_end = forms.TimeField(
        input_formats=['%H:%M'],
        label='Время окончания'
    )

    class Meta:
        model = Fishing
        fields = ['date', 'time_start', 'time_end',]
    
    def clean(self):
        date = self.cleaned_data.get('date')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        
        if time_start > time_end:
            self.add_error('time_end', time_start_more_time_end)
        if time_start == time_end:
            self.add_error(None, time_start_and_end_equal)
        
        return super().clean()


class FishingNoteForm(forms.ModelForm):
    class Meta:
        model = Fishing
        fields = ['note']


class FishingReportsSettingsForm(forms.ModelForm):
    class Meta:
        model = FishingReportsSettings
        fields = ['fisherman', 'time_start', 'time_end', 'place_water', 'place_locality',
                  'place_name', 'place_coordinate', 'weather', 'tackle', 'montage', 'trough',
                  'leash', 'crochet', 'nozzle', 'pace', 'lure', 'result', 'trophy', 'note']


class FishingLureForm(forms.ModelForm):
    class Meta:
        model = FishingLure
        fields = ['weight']
    
    def clean(self):
        weight = self.cleaned_data.get('weight')
        
        if weight == None:
            self.add_error('weight', weight_lure_is_null)
        elif weight <= 0:
            self.add_error('weight', weight_lure_is_negative)
        
        return super().clean()
    
    
# class FishingPointForm(forms.ModelForm):
#     class Meta:
#         model = FishingPoint
#         fields = ['fishing_point_azimuth',
#                   'fishing_point_distance',
#                   'fishing_poiny_depth',
#                   'priming', ]


class FishingResultForm(forms.ModelForm):
    class Meta:
        model = FishingResult
        fields = ['fish', 'number_of_fish', 'fish_weight', ]
    
    def clean(self):
        fish = self.cleaned_data.get('fish')
        number_of_fish = self.cleaned_data.get('number_of_fish')

        if fish == None:
            self.add_error('fish', fishing_result_fish_not_select)
        
        if number_of_fish == None:
            self.add_error('number_of_fish', fishing_result_number_of_fish_is_empty)
        
        return super().clean()


class FishingTrophyForm(forms.ModelForm):
    class Meta:
        model = FishingTrophy
        fields = ['fish', 'fish_trophy_weight', ]
    
    def clean(self):
        fish = self.cleaned_data.get('fish')
        fish_trophy_weight = self.cleaned_data.get('fish_trophy_weight')
        
        if fish == None:
            self.add_error('fish', fishing_trophy_fish_is_empty)
        
        if fish_trophy_weight == None:
            self.add_error('fish_trophy_weight', fishing_trophy_weight_is_empty)
        
        return super().clean()


class LeashForm(forms.ModelForm):
    class Meta:
        model = Leash
        fields = ['material',
                  'diameter', 'length', ]

    def clean(self):
        material = self.cleaned_data.get('material')
        diameter = self.cleaned_data.get('diameter')
        length = self.cleaned_data.get('length')
        
        if len(material) == 0:
            self.add_error('material', leash_material_empty)
        
        if diameter == None:
            self.add_error('diameter', leash_diameter_empty)
        
        if length == None:
            self.add_error('length', leash_length_empty)
        
        for no_valid_char in no_valid_char_list:
            if material.startswith(no_valid_char) or material.endswith(no_valid_char):
                self.add_error('material', leash_no_valid_char_error)
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = Leash
        self_form = LeashForm
        try:
            model = self_model.objects.get(id=kwargs['leash_id'])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такой поводок уже добавлен')
        return form
    

class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = ['weight', ]
    
    def clean(self):
        weight = self.cleaned_data.get('weight')
        
        if weight == None:
            self.add_error('weight', weight_lure_is_null)
        elif weight <= 0:
            self.add_error('weight', weight_lure_is_negative)
        
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = Lure
        self_form = LureForm
        try:
            fishing = Fishing.objects.get(id=kwargs['fishing_id'])
            fishing_lure_mix = FishingLureMix.objects.get(fishing=fishing)
            lure_mix = fishing_lure_mix.lure_mix
        except:
            try:
                lure_mix = LureMix.objects.get(id=kwargs['lure_mix_id'])
            except:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        if not lure_mix.editable():
            form = self_form(request.POST)
            form.add_error(None, 'Состав нельзя изменить')
            return form
        try:
            model = self_model.objects.get(id=kwargs['lure_id'])
            if model.owner == request.user:
                lure_base = model.base
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            lure_base = LureBase.objects.get(id=kwargs['lure_base_id'])
            form = self_form(request.POST)
        if lure_mix.owner == lure_base.owner:
            if form.is_valid():
                model = form.save(commit=False)
                model.owner = request.user
                model.mix = lure_mix
                model.base = lure_base
                model.save()
                return model.id
        else:
            form = self_form(request.POST)
            form.add_error(None, 'Что-то пошло не так')
        return form


class LureBaseForm(forms.ModelForm):
    class Meta:
        model = LureBase
        fields = ('manufacturer', 'name',)

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        
        if len(manufacturer) ==0 and len(name) == 0:
            self.add_error(None, manufacturer_and_name_lure_base_is_empty)
        
        manufacturer_errors = False
        name_errors = False
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not name_errors:
                if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', manufacturer_lure_base_no_valid_char)
                if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_lure_base_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = LureBase
        self_form = LureBaseForm
        kwargs_field = 'lure_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такой прикорм уже добавлен')
        return form


class LureMixForm(forms.ModelForm):
    class Meta:
        model = LureMix
        fields = ('name', 'description')

    def clean(self):
        name = self.cleaned_data.get('name')
        
        if len(name) == 0:
            self.add_error('name', lure_mix_name_is_empty)
        
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not name_errors:
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', lure_mix_name_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = LureMix
        self_form = LureMixForm
        kwargs_field = 'lure_mix_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такая прикормочная смесь уже добавлена')
        return form


class MontageForm(forms.ModelForm):
    class Meta:
        model = Montage
        fields = ('name',)

    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        
        if len(name) == 0:
            self.add_error('name', montage_name_is_empty)
        
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not name_errors:
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', montage_name_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        try:
            montage = Montage.objects.get(id=kwargs['montage_id'])
            if montage.owner == request.user:
                form = MontageForm(request.POST, instance=montage)
            else:
                form = MontageForm(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = MontageForm(request.POST)
        if form.is_valid():
            montage = form.save(commit=False)
            montage.owner = request.user
            if montage.unique():
                montage.first_upper()
                montage.save()
                return montage.id
            else:
                form.add_error(None, 'Такой монтаж уже добавлен')
        return form


class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = ['state', ]


class NozzleBaseForm(forms.ModelForm):
    class Meta:
        model = NozzleBase
        fields = ('manufacturer',
                  'name', 'size',
                  'ntype')

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        size = self.cleaned_data.get('size')
        ntype = self.cleaned_data.get('ntype')
        
        if len(manufacturer) == 0 and len(name) == 0:
            self.add_error(None, manufacturer_and_name_nozzle_is_empty)
        
        if size != None and size <= 0:
            self.add_error('size', size_nozzle_is_negative)
        
        manufacturer_errors = False
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not name_errors:
                if not manufacturer_errors and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', manufacturer_nozzle_no_valid_char)
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_nozzle_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = NozzleBase
        self_form = NozzleBaseForm
        kwargs_field = 'nozzle_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.bait = False
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такая насадка уже добавлена')
        return form


class BaitBaseForm(forms.ModelForm):
    class Meta:
        model = NozzleBase
        fields = ('manufacturer',
                  'name')

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        
        if len(manufacturer) == 0 and len(name) == 0:
            self.add_error(None, manufacturer_and_name_bait_is_empty)
        
        manufacturer_errors = False
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not name_errors:
                if not manufacturer_errors and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', manufacturer_bait_no_valid_char)
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_bait_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = NozzleBase
        self_form = BaitBaseForm
        kwargs_field = 'bait_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.bait = True
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такая наживка уже добавлена')
        return form


class NozzleStateForm(forms.ModelForm):
    class Meta:
        model = NozzleState
        fields = ('state',)

    def clean(self):
        state = self.cleaned_data.get('state')
        
        if len(state) == 0:
            self.add_error('state', state_nozzle_is_empty)
        
        state_errors = False
        for no_valid_char in no_valid_char_list:
            if not state_errors:
                if not state_errors and state.startswith(no_valid_char) or state.endswith(no_valid_char):
                    state_errors = True
                    self.add_error('state', state_nozzle_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = NozzleState
        self_form = NozzleStateForm
        kwargs_field = 'nozzle_state_id'
        try:
            model = self_model.objects.get(id=kwargs[kwargs_field])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такое состояние уже добавлено')
        return form


class NozzleTypeForm(forms.ModelForm):
    class Meta:
        model = NozzleType
        fields = ('name',)

    def clean(self):
        name = self.cleaned_data.get('name')
        nozzle_type_list = NozzleType.objects.all()
        name = re.sub(r'\s+', ' ', name)
        for nozzle_type in nozzle_type_list:
            if nozzle_type.name.lower() == name.lower():
                form_saved = self.save(commit=False)
                if nozzle_type.id != form_saved.id:
                    self.add_error('name', 'Такой тип уже добавлен')
        
        msg = 'Название типа насадки не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class OvercastForm(forms.ModelForm):
    class Meta:
        model = Overcast
        fields = ('name',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        overcast_list = Overcast.objects.all()
        for overcast in overcast_list:
            if overcast.name.lower() == name.lower():
                form_saved=self.save(commit=False)
                if overcast.id != form_saved.id:
                    self.add_error('name', 'Такая облачность уже добавлена')
        
        msg = 'Название облачности не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class PaceForm(forms.ModelForm):
    class Meta:
        model = Pace
        fields = ('interval',)
    
    def clean(self):
        interval = self.cleaned_data.get('interval')
        interval = re.sub(r'\s+', ' ', interval)
        pace_list = Pace.objects.all()
        for pace in pace_list:
            if pace.interval.lower() == interval.lower():
                form_saved=self.save(commit=False)
                if pace.id != form_saved.id:
                    self.add_error('interval', 'Такой темп уже добавлен')
        
        msg = 'Название темпа не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if interval.startswith(no_valid_char) or interval.endswith(no_valid_char):
                self.add_error('interval', msg)
                break

        return super().clean()


class PlaceFullForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['locality', 'name', 'latitude', 'longitude']
    
    def clean(self):
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            self.add_error('name', name_place_is_empty)

        name = re.sub(r'\s+', ' ', name)
        
        locality = self.cleaned_data.get('locality')
        if len(locality) != 0:
            locality = re.sub(r'\s+', ' ', locality)
        
        locality_errors = False
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not locality_errors or not name_errors:
                if not locality_errors and locality.startswith(no_valid_char) or locality.endswith(no_valid_char):
                    locality_errors = True
                    self.add_error('locality', locality_place_no_valid_char)
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_place_no_valid_char)
            else:
                break
        
        msg1 = 'Широта должа быть в пределах от -90 до 90 градусов'
        msg2 = 'Долгота должа быть в пределах от -180 до 180 градусов'
        
        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')
        if latitude == None and longitude == None:
            pass
        elif latitude == None:
            self.add_error('latitude', 'Укажите широту')
        elif latitude < -90 or latitude > 90:
            self.add_error('latitude', msg1)

        if longitude == None and latitude == None:
            pass
        elif longitude == None:
            self.add_error('longitude', 'Укажите долготу')
        elif longitude < -180 or longitude > 180:
            self.add_error('longitude', msg2)
        return super().clean()

    def save_me(request, *args, **kwargs):
        try:
            place = Place.objects.get(id=kwargs['place_id'])
            if place.owner == request.user:
                form = PlaceFullForm(request.POST, instance=place)
            else:
                form = PlaceFullForm(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = PlaceFullForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.owner = request.user
            place.water = kwargs['water']
            if place.unique():
                place.first_upper()
                place.save()
                return place.id
            else:
                form.add_error(None, 'Водоём с таким названием и категорией уже добавлен')
                return form
        return form


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['locality', 'name',]
        
    def clean(self):
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            self.add_error('name', name_place_is_empty)

        name = re.sub(r'\s+', ' ', name)
        
        locality = self.cleaned_data.get('locality')
        if len(locality) != 0:
            locality = re.sub(r'\s+', ' ', locality)
        
        locality_errors = False
        name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not locality_errors or not name_errors:
                if not locality_errors and locality.startswith(no_valid_char) or locality.endswith(no_valid_char):
                    locality_errors = True
                    self.add_error('locality', locality_place_no_valid_char)
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_place_no_valid_char)
            else:
                break
        return super().clean()
    
    def save_me(request, *args, **kwargs):
        try:
            place = Place.objects.get(id=kwargs['place_id'])
            if place.owner == request.user:
                form = PlaceForm(request.POST, instance=place)
            else:
                form = PlaceForm(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.owner = request.user
            place.water = kwargs['water']
            if place.unique():
                place.first_upper()
                place.save()
                return place.id
            else:
                form.add_error(None, 'Водоём с таким названием и категорией уже добавлен')
                return form
        return form


class PlaceCoordinatesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['latitude', 'longitude',]
        
    def clean(self):
        msg1 = 'Широта должа быть в пределах от -90 до 90 градусов'
        msg2 = 'Долгота должа быть в пределах от -180 до 180 градусов'
        
        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')
        if latitude == None:
            self.add_error('latitude', 'Укажите широту')
        elif latitude < -90 or latitude > 90:
            self.add_error('latitude', msg1)

        if longitude == None:
            self.add_error('longitude', 'Укажите долготу')
        elif longitude < -180 or longitude > 180:
            self.add_error('longitude', msg2)
        return super().clean()


# class PointForm(forms.ModelForm):
#     class Meta:
#         model = Point
#         fields = ['point_azimuth', 'point_distance',
#                   'point_depth', 'priming']


class PrimingForm(forms.ModelForm):
    class Meta:
        model = Priming
        fields = ('name',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        priming_list = Priming.objects.all()
        name = re.sub(r'\s+', ' ', name)
        for priming in priming_list:
            if priming.name.lower() == name.lower():
                form_saved=self.save(commit=False)
                if priming.id != form_saved.id:
                    self.add_error('name', 'Такое покрытие уже добавлено')
        
        msg = 'Название покрытия не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return super().clean()


class TackleForm(forms.ModelForm):
    class Meta:
        model = Tackle
        fields = ['manufacturer', 'model_tackle',
                  'length', 'casting_weight', ]

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        model_tackle = self.cleaned_data.get('model_tackle')
        model_tackle = re.sub(r'\s+', ' ', model_tackle)
        length = self.cleaned_data.get('length')
        casting_weight = self.cleaned_data.get('casting_weight')
        
        if not manufacturer and not model_tackle:
            self.add_error(None, tackle_manufacturer_and_model_is_empty)
        
        manufacturer_error = False
        model_error = False
        for no_valid_char in no_valid_char_list:
            if not manufacturer_error or not model_error:
                if not manufacturer_error and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_error = True
                    self.add_error('manufacturer', tackle_manufacturer_no_valid_char)
                if not model_error and model_tackle.startswith(no_valid_char) or model_tackle.endswith(no_valid_char):
                    model_error = True
                    self.add_error('model_tackle', tackle_model_no_valid_char)
            else:
                break
        return super().clean()
    
    def save_me(request, *args, **kwargs):
        try:
            tackle = Tackle.objects.get(id=kwargs['tackle_id'])
            if tackle.owner == request.user:
                form = TackleForm(request.POST, instance=tackle)
            else:
                form = TackleForm(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = TackleForm(request.POST)
        if form.is_valid():
            tackle = form.save(commit=False)
            tackle.owner = request.user
            if tackle.unique():
                tackle.first_upper()
                tackle.save()
                return tackle.id
            else:
                form.add_error(None, 'Такая снасть уже добавлена')
        return form



class TroughForm(forms.ModelForm):
    class Meta:
        model = Trough
        fields = ('manufacturer', 'model_name',
                  'plastic', 'lugs',
                  'feed_capacity', 'weight',)

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        model_name = self.cleaned_data.get('model_name')
        model_name = re.sub(r'\s+', ' ', model_name)
        
        if not manufacturer and not model_name:
            self.add_error('manufacturer', trough_manufacturer_and_model_is_empty)
        
        manufacturer_errors = False
        model_name_errors = False
        
        for no_valid_char in no_valid_char_list:
            if not manufacturer_errors or not model_name_errors:
                if not manufacturer_errors and manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                    manufacturer_errors = True
                    self.add_error('manufacturer', trough_manufacturer_no_valid_char)
                if not model_name_errors and model_name.startswith(no_valid_char) or model_name.endswith(no_valid_char):
                    model_name_errors = True
                    self.add_error('model_name', trough_model_no_valid_char)
            else:
                break
        return super().clean()

    def save_me(request, *args, **kwargs):
        self_model = Trough
        self_form = TroughForm
        try:
            model = self_model.objects.get(id=kwargs['trough_id'])
            if model.owner == request.user:
                form = self_form(request.POST, instance=model)
            else:
                form = self_form(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = self_form(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            if model.unique():
                model.first_upper()
                model.save()
                return model.id
            else:
                form.add_error(None, 'Такая кормушка уже добавлена')
        return form


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ('name', 'category',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            self.add_error('name', name_water_is_empty)
            return super().clean()
        name = re.sub(r'\s+', ' ', name)
        
        name_errors = False
        for no_valid_char in no_valid_char_list:
            if not name_errors:
                if not name_errors and name.startswith(no_valid_char) or name.endswith(no_valid_char):
                    name_errors = True
                    self.add_error('name', name_water_no_valid_char)
            else:
                break
        
        return super().clean()
    
    def save_me(request, *args, **kwargs):
        try:
            water = Water.objects.get(id=kwargs['water_id'])
            if water.owner == request.user:
                form = WaterForm(request.POST, instance=water)
            else:
                form = WaterForm(request.POST)
                form.add_error(None, 'Что-то пошло не так')
                return form
        except:
            form = WaterForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.owner = request.user
            if water.unique():
                water.first_upper()
                water.save()
                return water.id
            else:
                form.add_error(None, 'Водоём с таким названием и категорией уже добавлен')
                return form
        return form


class WaterCategoryForm(forms.ModelForm):
    class Meta:
        model = WaterCategory
        fields = ('category', 'abbreviation',)
    
    def clean(self):
        category = self.cleaned_data.get('category')
        abbreviation = self.cleaned_data.get('abbreviation')
        
        if len(category) == 0:
            msg0 = 'Название категории не может быть пустым'
            self.add_error('category', msg0)
            return super().clean()
        category = re.sub(r'\s+', ' ', category)
        
        msg1 = 'Категория не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|,'
        msg2 = 'Аббривиатура не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|,'
        
        for no_valid_char in no_valid_char_list:
            if category.startswith(no_valid_char) or category.endswith(no_valid_char):
                self.add_error('category', msg1)
                break
            if abbreviation.startswith(no_valid_char) or abbreviation.endswith(no_valid_char):
                self.add_error('abbreviation', msg2)
                break
        return super().clean()


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['overcast', 'conditions',
                  'temperature', 'pressure',
                  'direction_wind', 'wind_speed',
                  'lunar_day']

    def clean(self):
        overcast = self.cleaned_data.get('overcast')
        conditions = self.cleaned_data.get('conditions')
        temperature = self.cleaned_data.get('temperature')
        pressure = self.cleaned_data.get('pressure')
        direction_wind = self.cleaned_data.get('direction_wind')
        wind_speed = self.cleaned_data.get('wind_speed')
        lunar_day = self.cleaned_data.get('lunar_day')
        
        if (overcast == None and conditions == None and temperature == None and
            pressure == None and len(direction_wind) == 0 and wind_speed == None and
            lunar_day == None):
            self.add_error(None, weather_form_fields_is_empty)
            return super().clean()
        
        if temperature != None and temperature < weather_min_temperature:
            self.add_error('temperature', weather_temperature_is_low)
        elif temperature != None and temperature > weather_max_temperature:
            self.add_error('temperature', weather_temperature_is_high)
        
        if pressure != None and pressure < weather_min_pressure:
            self.add_error('pressure', weather_pressure_is_low)
        elif pressure != None and pressure > weather_max_pressure:
            self.add_error('pressure', weather_pressure_is_high)
        
        if wind_speed != None and wind_speed < 0:
            self.add_error('wind_speed', weather_wind_speed_is_negative)
        elif wind_speed != None and wind_speed >= 100:
            self.add_error('wind_speed', weather_wind_speed_is_high)
        
        direction_wind_error = False
        
        for no_valid_char in no_valid_char_list:
            if not direction_wind_error:
                if not direction_wind_error and direction_wind.startswith(no_valid_char) or direction_wind.endswith(no_valid_char):
                    self.add_error('direction_wind', weather_direction_wind_no_valid_char)
            else:
                break
        return super().clean()

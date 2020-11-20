from .models import Aroma
from .models import AromaBase
# from .models import BottomMap
from .models import Conditions
from .models import Crochet
# from .models import District
from .models import FeedCapacity
from .models import Fish
from .models import Fishing
# from .models import FishingPoint
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

class AromaForm(forms.ModelForm):
    class Meta:
        model = Aroma
        fields = ['volume', ]


class AromaBaseForm(forms.ModelForm):
    class Meta:
        model = AromaBase
        fields = ['manufacturer', 'name', ]

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        name = re.sub(r'\s+', ' ', name)
        
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название аромы не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


class CrochetForm(forms.ModelForm):
    class Meta:
        model = Crochet
        fields = ['manufacturer', 'model', 'size', ]

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        model = self.cleaned_data.get('model')
        size = self.cleaned_data.get('size')
        
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        model = re.sub(r'\s+', ' ', model)
        
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название модели не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if model.startswith(no_valid_char) or model.endswith(no_valid_char):
                self.add_error('model', msg2)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


class FishingForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        },),
        label='Дата рыбалки'
    )
    time_start = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'pattern': '[0-2]{1}[0-9]{1}:[0-6]{1}[0-9]{1}',
            'data-target': '#datetimepicker2'
        }),
        label='Время начала рыбалки'
    )
    time_end = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'pattern': '[0-2]{1}[0-9]{1}:[0-6]{1}[0-9]{1}',
            'data-target': '#datetimepicker3'
        }),
        label='Время окончания рыбалки'
    )

    class Meta:
        model = Fishing
        fields = ['date', 'time_start', 'time_end',]
    
    def clean(self):
        msg0 = 'Время начала и окончания рыбалки не могут быть равны'
        msg1 = 'Время начала рыбалки не может быть больше времени окончания'
        date = self.cleaned_data.get('date')
        time_start = self.cleaned_data.get('time_start')
        time_end = self.cleaned_data.get('time_end')
        
        print (type(time_start))
        if time_start > time_end:
            self.add_error('time_start', msg1)
        if time_start == time_end:
            self.add_error('time_start', msg0)
        
        return self.cleaned_data


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


class FishingTrophyForm(forms.ModelForm):
    class Meta:
        model = FishingTrophy
        fields = ['fish', 'fish_trophy_weight', ]


class LeashForm(forms.ModelForm):
    class Meta:
        model = Leash
        fields = ['material',
                  'diameter', 'length', ]

    def clean(self):
        material = self.cleaned_data.get('material')
        diameter = self.cleaned_data.get('diameter')
        length = self.cleaned_data.get('length')
        
        material = re.sub(r'\s+', ' ', material)
        
        msg = 'Название поводочного материала не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if material.startswith(no_valid_char) or material.endswith(no_valid_char):
                self.add_error('material', msg)
                break
        return self.cleaned_data


class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = ['weight', ]


class LureBaseForm(forms.ModelForm):
    class Meta:
        model = LureBase
        fields = ('manufacturer', 'name',)

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        name = self.cleaned_data.get('name')
        
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        name = re.sub(r'\s+', ' ', name)
        
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название прикорма не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class LureMixForm(forms.ModelForm):
    class Meta:
        model = LureMix
        fields = ('name',)

    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class MontageForm(forms.ModelForm):
    class Meta:
        model = Montage
        fields = ('name',)

    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


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
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        size = self.cleaned_data.get('size')
        ntype = self.cleaned_data.get('ntype')
        
        msg0 = 'Производитель или название должны быть указаны'
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        if not manufacturer and not name:
            self.add_error('manufacturer', msg0)
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class BaitBaseForm(forms.ModelForm):
    class Meta:
        model = NozzleBase
        fields = ('manufacturer',
                  'name')

    def clean(self):
        manufacturer = self.cleaned_data.get('manufacturer')
        manufacturer = re.sub(r'\s+', ' ', manufacturer)
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class NozzleStateForm(forms.ModelForm):
    class Meta:
        model = NozzleState
        fields = ('state',)

    def clean(self):
        state = self.cleaned_data.get('state')
        state = re.sub(r'\s+', ' ', state)
        
        msg1 = 'Состояние не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if state.startswith(no_valid_char) or state.endswith(no_valid_char):
                self.add_error('state', msg1)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        for no_valid_char in no_valid_char_list:
            if interval.startswith(no_valid_char) or interval.endswith(no_valid_char):
                self.add_error('interval', msg)
                break

        return self.cleaned_data


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['locality', 'name',]
        
    def clean(self):
        msg0 = 'Название места не может быть пустым'
        
        name = self.cleaned_data.get('name')
        if len(name) == 0:
            self.add_error('name', msg0)

        name = re.sub(r'\s+', ' ', name)
        
        locality = self.cleaned_data.get('locality')
        if len(locality) != 0:
            locality = re.sub(r'\s+', ' ', locality)
        
        msg1 = 'Название населенного пункта не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|.'
        msg2 = 'Название места не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|.'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'",
                              '.']
        
        for no_valid_char in no_valid_char_list:
            if locality.startswith(no_valid_char) or locality.endswith(no_valid_char):
                self.add_error('locality', msg1)
                break
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class PlaceCoordinatesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['latitude', 'longitude',]
        
    def clean(self):
        msg1 = 'Широта должа быть в пределах от -90 до 90 градусов'
        msg2 = 'Долгота должа быть в пределах от -180 до 180 градусов'
        
        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')
        if latitude < -90 or latitude > 90:
            self.add_error('latitude', msg1)
        if longitude < -180 or longitude > 180:
            self.add_error('longitude', msg2)
        return self.cleaned_data


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
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg)
                break
        return self.cleaned_data


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
        
        msg0 = 'Производитель или название должны быть указаны'
        msg1 = 'Название производителя не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        if not manufacturer and not model_tackle and not length and not casting_weight:
            self.add_error('manufacturer', 'Хотя бы одно поле должно быть заполнено')
        
        if not manufacturer and not model_tackle:
            self.add_error('manufacturer', msg0)
        
        
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if model_tackle.startswith(no_valid_char) or model_tackle.endswith(no_valid_char):
                self.add_error('model_tackle', msg2)
                break
        return self.cleaned_data


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
        plastic = self.cleaned_data.get('plastic')
        lugs = self.cleaned_data.get('lugs')
        feed_capacity = self.cleaned_data.get('feed_capacity')
        weight = self.cleaned_data.get('weight')
        
        msg0 = 'Производитель или модель должны быть указаны'
        msg1 = 'Название производтеля не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        msg2 = 'Название модели не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'"]
        
        if not manufacturer and not model_name:
            self.add_error('manufacturer', msg0)
            
        for no_valid_char in no_valid_char_list:
            if manufacturer.startswith(no_valid_char) or manufacturer.endswith(no_valid_char):
                self.add_error('manufacturer', msg1)
                break
            if model_name.startswith(no_valid_char) or model_name.endswith(no_valid_char):
                self.add_error('model_name', msg1)
                break
        return self.cleaned_data


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ('name', 'category',)
    
    def clean(self):
        name = self.cleaned_data.get('name')
        name = re.sub(r'\s+', ' ', name)
        
        msg2 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|.'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'",
                              '.']
        
        for no_valid_char in no_valid_char_list:
            if name.startswith(no_valid_char) or name.endswith(no_valid_char):
                self.add_error('name', msg2)
                break
        return self.cleaned_data


class WaterCategoryForm(forms.ModelForm):
    class Meta:
        model = WaterCategory
        fields = ('category', 'abbreviation',)
    
    def clean(self):
        category = self.cleaned_data.get('category')
        abbreviation = self.cleaned_data.get('abbreviation')
        
        if len(category) == 0:
            msg0 = 'Название категории не может быть пустым'
            self.add_erorr('category', msg0)
            return self.cleaned_data
        category = re.sub(r'\s+', ' ', category)
        
        msg1 = 'Название не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|,'
        msg2 = 'Аббривиатура не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|,'
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'",
                              ',']
        
        for no_valid_char in no_valid_char_list:
            if category.startswith(no_valid_char) or category.endswith(no_valid_char):
                self.add_error('category', msg1)
                break
            if abbreviation.startswith(no_valid_char) or abbreviation.endswith(no_valid_char):
                self.add_error('abbreviation', msg2)
                break
        return self.cleaned_data


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
            self.add_error('direction_wind', 'Хотя бы одно поле должно иметь значение')
            return self.cleaned_data
        
        if len(direction_wind) != 0:
            direction_wind = re.sub(r'\s+', ' ', direction_wind)
            
        msg = 'Направление ветра не может начинаться и заканчиваться символом !@#$%^&*"№;:?<>/|,'
        
        
        
        no_valid_char_list = ['!', '@', '#', '$', '%', '^', '&', '*', '"',
                              '№', ';', ':', '?', '<', '>', '/', '|', "'",
                              ',']
        for no_valid_char in no_valid_char_list:
            if direction_wind.startswith(no_valid_char) or direction_wind.endswith(no_valid_char):
                self.add_error('direction_wind', msg)
                break
        return self.cleaned_data

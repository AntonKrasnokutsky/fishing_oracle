from .models import Fish
from .models import District, Water, Place
from .models import Priming
from .models import FeedCapacity
from .models import Pace
from .models import FishingPoint
from .models import Tackle, Montage
from .models import Trough
from .models import BottomMap, Point
from .models import Weather, Overcast, Conditions
from .models import Nozzle, NozzleState, NozzleBase
from .models import Lure, LureBase, LureMix
from .models import AromaBase, Aroma
from .models import Crochet, Leash
from .models import Fishing, FishingResult, FishTrophy
from django import forms
import re

# widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'от 0 до 99.9 кг'}),
#         }

class AromaForm(forms.ModelForm):
    class Meta:
        model = Aroma
        fields = ['aroma_volume', ]


class AromaBaseForm(forms.ModelForm):
    class Meta:
        model = AromaBase
        fields = ['aroma_manufacturer', 'aroma_name', ]


class BottomMapForm(forms.ModelForm):
    class Meta:
        model = BottomMap
        fields = ['bottom_map_northern_degree', 'bottom_map_northern_minute',
                  'bottom_map_northern_second', 'bottom_map_easter_degree',
                  'bottom_map_easter_minute', 'bottom_map_easter_second', ]


class CrochetForm(forms.ModelForm):
    class Meta:
        model = Crochet
        fields = ['crochet_manufacturer', 'crochet_model', 'crochet_size', ]


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('district_name',)


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
        })
    )
    time = forms.TimeField(
        input_formats=['%H:%M'],
        widget=forms.TimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )
    
    class Meta:
        model = Fishing
        fields = ['date', 'time', ]


class LureMixForm(forms.ModelForm):
    class Meta:
        model = LureMix
        fields = ('lure_mix_name',)


class MontageForm(forms.ModelForm):
    class Meta:
        model = Montage
        fields = ('montage_name', 'montage_sliding', )


class FishingPointForm(forms.ModelForm):
    class Meta:
        model = FishingPoint
        fields = ['fishing_point_azimuth',
                  'fishing_point_distance',
                  'fishing_poiny_depth',
                  'priming', ]


class FishingResultForm(forms.ModelForm):
    class Meta:
        model = FishingResult
        fields = ['fish', 'number_of_fish', 'fish_weight', ]


class FishTrophyForm(forms.ModelForm):
    class Meta:
        model = FishTrophy
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
        fields = ['lure_weight', ]


class LureBaseForm(forms.ModelForm):
    class Meta:
        model = LureBase
        fields = ('lure_manufacturer', 'lure_name',)


class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = ['nozzle_state', ]


class NozzleBaseForm(forms.ModelForm):
    class Meta:
        model = NozzleBase
        fields = ('bait', 'nozzle_manufacturer',
                  'nozzle_name', 'nozzle_diameter',
                  'nozzle_type')


class NozzleStateForm(forms.ModelForm):
    class Meta:
        model = NozzleState
        fields = ('state',)


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
        fields = ['place_locality', 'place_name', 'place_northern_degree',
                  'place_northern_minute', 'place_northern_second',
                  'place_easter_degree', 'place_easter_minute',
                  'place_easter_second', ]


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['point_azimuth', 'point_distance',
                  'point_depth', 'priming']


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
        fields = ['tackle_manufacturer', 'tackle_name',
                  'tackle_length', 'tackle_casting_weight', ]


class TroughForm(forms.ModelForm):
    class Meta:
        model = Trough
        fields = ('trough_manufacturer', 'model_trough_name',
                  'model_trough_plastic', 'model_trough_lugs',
                  'feed_capacity', 'trough_weight',)


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ('water_name',)


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['date', 'overcast', 'conditions',
                  'weather_temperature', 'pressure',
                  'direction_wind', 'wind_speed',
                  'lunar_day']


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

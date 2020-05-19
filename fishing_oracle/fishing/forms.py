from .models import Fish
from .models import District, Water, Place
from .models import Priming
from .models import FeedCapacity
from .models import Pace
from .models import FishingPoint
from .models import FishingTackle, FishingMontage, ModelTroughName, ModelTrough
from .models import FishingTrough
from .models import BottomMap, Point
from .models import Weather, Overcast, WeatherPhenomena
from .models import NozzleState, Nozzle
from .models import Lure, LureBase, FishingLure
from .models import AromaBase, Aroma
from django import forms

class AromaForm(forms.ModelForm):
    class Meta:
        model=Aroma
        fields=['aroma_base', 'aroma_volume', ]
class AromaBaseForm(forms.ModelForm):
    class Meta:
        model=AromaBase
        fields=['aroma_manufacturer', 'aroma_name', ]


class BottomMapForm(forms.ModelForm):
    class Meta:
        model = BottomMap
        fields = ['bottom_map_northern_degree', 'bottom_map_northern_minute',
                  'bottom_map_northern_second', 'bottom_map_easter_degree',
                  'bottom_map_easter_minute', 'bottom_map_easter_second', ]


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('district_name',)


class FeedCapacityForm(forms.ModelForm):
    class Meta:
        model = FeedCapacity
        fields = ('feed_capacity_name',)


class FishForm(forms.ModelForm):

    class Meta:
        model = Fish
        fields = ('name_of_fish', 'fish_description', )
    #renewal_name_of_fish = forms.CharField(max_length=20, label='Рыба')


class FishingLureForm(forms.ModelForm):
    class Meta:
        model = FishingLure
        fields = ('nozzle', 'nozzle_state',)


class FishingMontageForm(forms.ModelForm):
    class Meta:
        model = FishingMontage
        fields = ('fishing_montage_name', 'fishing_montage_sliding', )


class FishingPointForm(forms.ModelForm):
    class Meta:
        model = FishingPoint
        fields = ['fishing_point_azimuth',
                  'fishing_point_distance',
                  'fishing_poiny_depth',
                  'priming', ]


class FishingTackleForm(forms.ModelForm):
    class Meta:
        model = FishingTackle
        fields = ['fishing_tackle_manufacturer', 'fishing_tackle_name',
                  'fishing_tackle_length', 'fishing_tackle_casting_weight', ]


class FishingTroughForm(forms.ModelForm):
    class Meta:
        model = FishingTrough
        fields = ('fishing_trough_manufacturer', 'model_trough',
                  'feed_capacity', 'fishing_trough_weight',)


class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = ['lure_base', 'lure_weight', ]


class LureBaseForm(forms.ModelForm):
    class Meta:
        model = LureBase
        fields = ('lure_manufacturer', 'lure_name',)


class ModelTroughForm(forms.ModelForm):
    class Meta:
        model = ModelTrough
        fields = ('model_trough_name', 'model_trough_plastic',
                  'model_trough_lugs',)


class ModelTroughNameForm(forms.ModelForm):
    class Meta:
        model = ModelTroughName
        fields = ('model_trough_name',)


class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
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
        fields = ('overcast_name',)


class PaceForm(forms.ModelForm):
    class Meta:
        model = Pace
        fields = ('pace_interval',)


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['place_locality', 'place_northern_degree',
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
        fields = ('priming_name',)


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ('water_name',)


class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = ['date', 'overcast', 'weather_phenomena',
                  'weather_temperature', 'pressure',
                  'direction_wind', 'wind_speed',
                  'lunar_day']


class WeatherPhenomenaForm(forms.ModelForm):
    class Meta:
        model = WeatherPhenomena
        fields = ('weather_phenomena_name',)

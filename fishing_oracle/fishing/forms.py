from .models import Fish
from .models import District, Water, Place
from .models import Priming
from .models import FeedCapacity
from .models import Pace
from .models import FishingPoint
from .models import Tackle, Montage, ModelTroughName, ModelTrough
from .models import Trough
from .models import BottomMap, Point
from .models import Weather, Overcast, WeatherPhenomena
from .models import Nozzle, NozzleState, NozzleBase
from .models import Lure, LureBase, LureMix
from .models import AromaBase, Aroma
from .models import Crochet, Leash
from .models import Fishing, FishingResult, FishTrophy
from django import forms


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
        fields = ('feed_capacity_name',)


class FishForm(forms.ModelForm):

    class Meta:
        model = Fish
        fields = ('name_of_fish', 'fish_description', )
    #renewal_name_of_fish = forms.CharField(max_length=20, label='Рыба')


class FishingForm(forms.ModelForm):
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
        fields = ['leash_material',
                  'leash_diameter', 'leash_length', ]


class LureForm(forms.ModelForm):
    class Meta:
        model = Lure
        fields = ['lure_weight', ]


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
        fields = ['nozzle_state',]

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
        fields = ('overcast_name',)


class PaceForm(forms.ModelForm):
    class Meta:
        model = Pace
        fields = ('pace_interval',)


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
        fields = ('priming_name',)


class TackleForm(forms.ModelForm):
    class Meta:
        model = Tackle
        fields = ['tackle_manufacturer', 'tackle_name',
                  'tackle_length', 'tackle_casting_weight', ]


class TroughForm(forms.ModelForm):
    class Meta:
        model = Trough
        fields = ('trough_manufacturer', 'model_trough',
                  'feed_capacity', 'trough_weight',)


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

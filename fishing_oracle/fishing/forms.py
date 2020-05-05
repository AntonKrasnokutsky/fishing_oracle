from .models import Fish
from .models import District
from .models import Priming
from .models import Overcast
from .models import WeatherPhenomena
from .models import FeedCapacity
from .models import Pace
from .models import Water
from .models import Place
from django import forms


class FishForm(forms.ModelForm):

    class Meta:
        model = Fish
        fields = ('name_of_fish', 'fish_description',)

#    renewal_name_of_fish = forms.CharField(max_length=20, label='Рыба')


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('district_name',)


class PrimingForm(forms.ModelForm):
    class Meta:
        model = Priming
        fields = ('priming_name',)


class OvercastForm(forms.ModelForm):
    class Meta:
        model = Overcast
        fields = ('overcast_name',)


class WeatherPhenomenaForm(forms.ModelForm):
    class Meta:
        model = WeatherPhenomena
        fields = ('weather_phenomena_name',)


class FeedCapacityForm(forms.ModelForm):
    class Meta:
        model = FeedCapacity
        fields = ('feed_capacity_name',)


class PaceForm(forms.ModelForm):
    class Meta:
        model = Pace
        fields = ('pace_interval',)


class WaterForm(forms.ModelForm):
    class Meta:
        model = Water
        fields = ('district', 'water_name',)


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['water', 'place_locality', 'place_northern_degree',
                  'place_northern_minute', 'place_northern_second',
                  'place_easter_degree', 'place_easter_minute',
                  'place_easter_second', ]

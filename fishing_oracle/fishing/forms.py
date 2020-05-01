from .models import Fish, District, Priming, Overcast
from django import forms


class FishRenewalForm(forms.ModelForm):

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

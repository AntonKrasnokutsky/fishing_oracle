from .models import Fish
from django import forms


class FishRenewalForm(forms.ModelForm):

    class Meta:
        model = Fish
        fields = ('name_of_fish', 'fish_description',)

    # class FishRenewalForm(forms.Form):
#    renewal_name_of_fish = forms.CharField(
#        max_length=20)
#    renewal_fish_description = forms.TextField()

#    def clean_renewal_name_of_fish(self):
#        name_of_fish = self.cleaned_data['renewal_name_of_fish']

#        return name_of_fish

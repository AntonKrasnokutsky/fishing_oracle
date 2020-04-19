from django import forms


class FishRenewalForm(forms.Form):
    renewal_name_of_fish = forms.CharField(max_length=20)

    def clean_renewal_name_of_fish(self):
        name_of_fish = self.cleaned_data['renewal_name_of_fish']

        return name_of_fish

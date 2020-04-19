from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Place, Fishing, Fish
from .forms import FishRenewalForm


def index(request):
    return render(request, 'fishing/index.html', {})


def fishing(request):
    fishing_list = Fishing.objects.all()
    return render(request, 'fishing/fishing.html', {'fishing_list': fishing_list, })


def detail(request, fishing_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    return render(request, 'fishing/detail.html', {'fishing': fishing})


def fish(request):
    fish_list = Fish.objects.all()
    return render(request, 'fishing/fish.html', {'fish_list': fish_list})


def fish_details(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    return render(request, 'fishing/fish_details.html', {'fish': fish})


def fishing_add(request):
    # HttpResponse("Добавление рыбаки")
    return render(request, 'fishing/fishing_add.html')


def renewal_fish(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)

    if request.method == 'POST':
        form = FishRenewalForm(request.POST)
        if form.is_valid():
            fish.name_of_fish = form.cleaned_data['name_of_fish']
            fish.fish_description = form.changed_data['fish_description']
            fish.save()
        fish_list = Fish.objects.all()
        return render(request, 'fishing/fish.html', {'fish_list': fish_list})
    else:
        form = FishRenewalForm(
            initial={'name_of_fish': fish.name_of_fish, 'fish_description': fish.fish_description, })

    return render(request, 'fishing/renewal_fish.html', {'form': form, 'fish': fish})


def add_fish(request):
    fish = Fish()

    if request.method == 'POST':
        form = FishRenewalForm(request.POST)
        if form.is_valid():

            fish.name_of_fish = form.cleaned_data['name_of_fish']
            fish.fish_description = form.cleaned_data['fish_description']
            fish.save()
        fish_list = Fish.objects.all()
        return render(request, 'fishing/fish.html', {'fish_list': fish_list})
    else:
        form = FishRenewalForm()

    return render(request, 'fishing/renewal_fish.html', {'form': form, 'fish': fish})

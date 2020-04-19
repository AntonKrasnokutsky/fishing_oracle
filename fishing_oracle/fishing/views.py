from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Place, Fishing, Fish
from .forms import FishRenewalForm


def fishing(request):
    fishing_list = Fishing.objects.all()
    return render(request, 'fishing/fishing.html', {'fishing_list': fishing_list, })


def detail(request, fishing_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    return render(request, 'fishing/detail.html', {'fishing': fishing})


def fishing_add(request):
    # HttpResponse("Добавление рыбаки")
    return render(request, 'fishing/fishing_add.html')


def renewal_name_fish(request, fish_id):
    name_of_fish = get_object_or_404(Fish, pk=fish_id)

    if request.method == 'POST':
        form = FishRenewalForm(request.POST)
        if form.is_valid():
            name_of_fish.name_of_fish = form.cleaned_data['renewal_name_of_fish']
            name_of_fish.save()
        return HttpResponse('Обновили')
    else:
        form = FishRenewalForm()
    return render(request, 'fishing/renewal_fish.html', {'form': form, 'name_of_fish': name_of_fish})

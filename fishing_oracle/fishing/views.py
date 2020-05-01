from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Fishing
from .models import Fish
from .models import District
from .models import Priming
from .forms import FishRenewalForm
from .forms import DistrictForm
from .forms import PrimingForm
from django.contrib.auth.decorators import login_required


def visits(request, inc=0):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + inc
    return num_visits


# @login_required
def index(request):
    num_visits = visits(request, 1)
    return render(request, 'fishing/index.html', {'num_visits': num_visits})


def fishing(request):
    fishing_list = Fishing.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/fishing.html', {'fishing_list': fishing_list, 'num_visits': num_visits})


def fishing_add(request):
    # HttpResponse("Добавление рыбаки")
    num_visits = visits(request)
    return render(request, 'fishing/fishing_add.html', {'num_visits': num_visits})


def detail(request, fishing_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    num_visits = visits(request)
    return render(request, 'fishing/detail.html', {'fishing': fishing, 'num_visits': num_visits})


def fishs(request):
    fish_list = Fish.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/fish.html', {'fish_list': fish_list, 'num_visits': num_visits})


def fish_details(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    num_visits = visits(request)
    return render(request, 'fishing/fish_details.html', {'fish': fish, 'num_visits': num_visits})


def fish_renewal(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)

    if request.method == 'POST':
        form = FishRenewalForm(request.POST)
        if form.is_valid():
            fish.name_of_fish = form.cleaned_data['name_of_fish']
            fish.fish_description = form.cleaned_data['fish_description']
            fish.save()
        return fishs(request)
    else:
        form = FishRenewalForm(
            initial={'name_of_fish': fish.name_of_fish, 'fish_description': fish.fish_description, })

    num_visits = visits(request)
    return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})


def fish_add(request):
    fish = Fish()

    if request.method == 'POST':
        form = FishRenewalForm(request.POST)
        if form.is_valid():

            fish.name_of_fish = form.cleaned_data['name_of_fish']
            fish.fish_description = form.cleaned_data['fish_description']
            fish.save()
        return fishs(request)
    else:
        form = FishRenewalForm()

    num_visits = visits(request)
    return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})


def fish_remove(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    fish.delete()
    return fishs(request)


def districts(request):
    districts_list = District.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/districts.html', {'districts_list': districts_list, 'num_visits': num_visits})


def district_add(request):
    district = District()

    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district.district_name = form.cleaned_data['district_name']
            district.save()
        return districts(request)
    else:
        form = DistrictForm()

    num_visits = visits(request)
    return render(request, 'fishing/district_renewal.html', {'form': form, 'district': district, 'num_visits': num_visits})


def district_renewal(request, district_id):
    district = get_object_or_404(District, pk=district_id)

    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district.district_name = form.cleaned_data['district_name']
            district.save()
        return districts(request)
    else:
        form = DistrictForm(
            initial={'district_name': district.district_name, })

    num_visits = visits(request)
    return render(request, 'fishing/district_renewal.html', {'form': form, 'district': district, 'num_visits': num_visits})


def district_remove(request, district_id):
    district = get_object_or_404(District, pk=district_id)
    district.delete()
    return districts(request)


def primings(request):
    primings_list = Priming.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/primings.html', {'primings_list': primings_list, 'num_visits': num_visits})


def priming_add(request):
    priming = Priming()

    if request.method == 'POST':
        form = PrimingForm(request.POST)
        if form.is_valid():
            priming.priming_name = form.cleaned_data['priming_name']
            priming.save()
        return primings(request)
    else:
        form = PrimingForm()

    num_visits = visits(request)
    return render(request, 'fishing/priming_renewal.html', {'form': form, 'priming': priming, 'num_visits': num_visits})


def priming_renewal(request, priming_id):
    priming = get_object_or_404(Priming, pk=priming_id)

    if request.method == 'POST':
        form = PrimingForm(request.POST)
        if form.is_valid():
            priming.priming_name = form.cleaned_data['priming_name']
            priming.save()
        return primings(request)
    else:
        form = PrimingForm(
            initial={'priming_name': priming.priming_name, })

    num_visits = visits(request)
    return render(request, 'fishing/priming_renewal.html', {'form': form, 'priming': priming, 'num_visits': num_visits})


def priming_remove(request, priming_id):
    priming = get_object_or_404(Priming, pk=priming_id)
    priming.delete()
    return primings(request)

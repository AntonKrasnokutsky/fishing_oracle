from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Fishing
from .models import Fish
from .models import District
from .models import Priming
from .models import Overcast
from .forms import FishRenewalForm
from .forms import DistrictForm
from .forms import PrimingForm
from .forms import OvercastForm
from django.contrib.auth.decorators import login_required


def visits(request, inc=0):
    """
    Счетчик посещения страниц
    """
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + inc
    return num_visits


def index(request):
    """
    Главная страница
    """
    num_visits = visits(request, 1)
    return render(request, 'fishing/index.html', {'num_visits': num_visits})


@login_required
def fishing_list(request):
    """
    Список рыбалок, для сотрудников сисок всех рыбалок
    в базе, для остальных список только своих рыбалок
    """
    if not request.user.is_staff:
        fishings_list = Fishing.objects.filter(
            owner=request.user)
    else:
        fishings_list = Fishing.objects.all()
    num_visits = visits(request)
    return render(
        request, 'fishing/fishing.html',
        {'fishing_list': fishings_list,
         'num_visits': num_visits})


@login_required
def fishing_add(request):
    """
    Добавление рыбалки
    """
    # HttpResponse("Добавление рыбаки")
    num_visits = visits(request)
    return render(request, 'fishing/fishing_add.html', {'num_visits': num_visits})


@login_required
def fishing_detail(request, fishing_id):
    """
    Детальная информация о рыбалке
    """
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    num_visits = visits(request)
    if request.user == fishing.owner or request.user.is_staff:
        return render(request, 'fishing/detail.html', {'fishing': fishing, 'num_visits': num_visits})
    else:
        return redirect('fishing:fishing')


def fish_list(request):
    """
    Список рыб
    """
    fishs_list = Fish.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/fish.html', {'fish_list': fishs_list, 'num_visits': num_visits})


def fish_details(request, fish_id):
    """
    Просмотр описания рыбы
    """
    fish = get_object_or_404(Fish, pk=fish_id)
    num_visits = visits(request)
    return render(request, 'fishing/fish_details.html', {'fish': fish, 'num_visits': num_visits})


@login_required
def fish_renewal(request, fish_id):
    if request.user.is_staff:
        fish = get_object_or_404(Fish, pk=fish_id)
        num_visits = visits(request)
        if request.method == 'POST':
            form = FishRenewalForm(request.POST)
            if form.is_valid():
                fish.name_of_fish = form.cleaned_data['name_of_fish']
                fish.fish_description = form.cleaned_data['fish_description']
                fish.save()
            return redirect('fishing:fish')
        else:
            form = FishRenewalForm(
                initial={'name_of_fish': fish.name_of_fish, 'fish_description': fish.fish_description, })
        return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})
    else:
        return redirect('fishing:fish')


@login_required
def fish_add(request):
    if request.user.is_staff:
        fish = Fish()
        num_visits = visits(request)
        if request.method == 'POST':
            form = FishRenewalForm(request.POST)
            if form.is_valid():

                fish.name_of_fish = form.cleaned_data['name_of_fish']
                fish.fish_description = form.cleaned_data['fish_description']
                fish.save()
            return redirect('fishing:fish')
        else:
            form = FishRenewalForm()
        return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})
    else:
        return redirect('fishing:fish')


@login_required
def fish_remove(request, fish_id):
    if request.user.is_staff:
        fish = get_object_or_404(Fish, pk=fish_id)
        fish.delete()
    return redirect('fishing:fish')


@login_required
def district_list(request):
    """
    Список районов
    """
    if request.user.is_staff:
        districts_list = District.objects.all()
        num_visits = visits(request)
        return render(request, 'fishing/districts.html', {'districts_list': districts_list, 'num_visits': num_visits})
    return redirect('fishing:index')


@login_required
def district_add(request):
    num_visits = visits(request)
    if request.user.is_staff:
        district = District()

        if request.method == 'POST':
            form = DistrictForm(request.POST)
            if form.is_valid():
                district.district_name = form.cleaned_data['district_name']
                district.save()
            return redirect('fishing:districts')
        else:
            form = DistrictForm()
        return render(request, 'fishing/district_renewal.html', {'form': form, 'district': district, 'num_visits': num_visits})
    else:
        return redirect('fishing:districts')


@login_required
def district_renewal(request, district_id):
    """
    Редактирование района
    """
    num_visits = visits(request)
    if request.user.is_staff:
        district = get_object_or_404(District, pk=district_id)

        if request.method == 'POST':
            form = DistrictForm(request.POST)
            if form.is_valid():
                district.district_name = form.cleaned_data['district_name']
                district.save()
            return redirect('fishing:districts')
        else:
            form = DistrictForm(
                initial={'district_name': district.district_name, })

        num_visits = visits(request)
        return render(request, 'fishing/district_renewal.html', {'form': form, 'district': district, 'num_visits': num_visits})
    else:
        return redirect('fishing:districts')


@login_required
def district_remove(request, district_id):
    """
    Удаление района
    """
    if request.user.is_staff:
        district = get_object_or_404(District, pk=district_id)
        district.delete()
    return redirect('fishing:districts')


@login_required
def priming_list(request):
    """
    Список видов грунта
    """
    if request.user.is_staff:
        primings_list = Priming.objects.all()
        num_visits = visits(request)
        return render(request, 'fishing/primings.html',
                      {'primings_list': primings_list,
                       'num_visits': num_visits})
    return redirect('fishing:index')


@login_required
def priming_add(request):
    """
    Добавление вида грунта
    """
    num_visits = visits(request)
    if request.user.is_staff:
        priming = Priming()

        if request.method == 'POST':
            form = PrimingForm(request.POST)
            if form.is_valid():
                priming.priming_name = form.cleaned_data[
                    'priming_name']
                priming.save()
            return redirect('fishing:primings')
        else:
            form = PrimingForm()
            return render(
                request,
                'fishing/priming_renewal.html',
                {'form': form,
                 'priming': priming,
                 'num_visits': num_visits})
    else:
        return redirect('fishing:index')


@login_required
def priming_renewal(request, priming_id):
    """
    Редактирование грунта
    """
    num_visits = visits(request)
    if request.user.is_staff:
        priming = get_object_or_404(Priming, pk=priming_id)

        if request.method == 'POST':
            form = PrimingForm(request.POST)
            if form.is_valid():
                priming.priming_name = form.cleaned_data['priming_name']
                priming.save()
            return redirect('fishing:primings')
        else:
            form = PrimingForm(
                initial={'priming_name': priming.priming_name, })
            return render(request, 'fishing/priming_renewal.html', {'form': form, 'priming': priming, 'num_visits': num_visits})
    else:
        return redirect('fishing:primings')


@login_required
def priming_remove(request, priming_id):
    """
    Удаление грунта
    """
    if request.user.is_staff:
        priming = get_object_or_404(Priming, pk=priming_id)
        priming.delete()
    return redirect('fishing:primings')


@login_required
def overcast_list(request):
    if request.user.is_staff:
        overcasts_list = Overcast.objects.all()
        num_visits = visits(request)
        return render(request, 'fishing/overcast.html',
                      {'overcasts_list': overcasts_list,
                       'num_visits': num_visits})
    return redirect('fishing:index')


@login_required
def overcast_add(request):
    num_visits = visits(request)
    if request.user.is_staff:
        overcast = Overcast()

        if request.method == 'POST':
            form = OvercastForm(request.POST)
            if form.is_valid():
                overcast.overcast_name = form.cleaned_data[
                    'overcast_name']
                overcast.save()
            return redirect('fishing:overcast')
        else:
            form = OvercastForm()
            return render(
                request,
                'fishing/overcast_renewal_add.html',
                {'form': form,
                 'overcast': overcast,
                 'num_visits': num_visits})
    else:
        return redirect('fishing:index')


@login_required
def overcast_renewal(request, overcast_id):
    """
    Редактирование облачности
    """
    num_visits = visits(request)
    if request.user.is_staff:
        overcast = get_object_or_404(Overcast, pk=overcast_id)

        if request.method == 'POST':
            form = OvercastForm(request.POST)
            if form.is_valid():
                overcast.overcast_name = form.cleaned_data['overcast_name']
                overcast.save()
            return redirect('fishing:overcast')
        else:
            form = OvercastForm(
                initial={'overcast_name': overcast.overcast_name, })
            return render(request,
                          'fishing/overcast_renewal_add.html',
                          {'form': form,
                           'overcast': overcast,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:overcast')


@login_required
def overcast_remove(request, overcast_id):
    """
    Удаление облачности
    """
    if request.user.is_staff:
        overcast = get_object_or_404(Overcast, pk=overcast_id)
        overcast.delete()
    return redirect('fishing:overcast')

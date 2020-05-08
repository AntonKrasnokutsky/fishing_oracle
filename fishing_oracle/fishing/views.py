from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Fishing

from .models import Fish
from .forms import FishForm

from .models import District
from .forms import DistrictForm

from .models import Priming
from .forms import PrimingForm

from .models import Overcast
from .forms import OvercastForm

from .models import WeatherPhenomena
from .forms import WeatherPhenomenaForm

from .models import FeedCapacity
from .forms import FeedCapacityForm

from .models import Pace
from .forms import PaceForm

from .models import Water
from .forms import WaterForm

from .models import Place
from .forms import PlaceForm

from .models import FishingPoint
from .forms import FishingPointForm

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
    return render(request,
                  'fishing/fish.html',
                  {'fish_list': fishs_list,
                   'num_visits': num_visits})


def fish_details(request, fish_id):
    """
    Просмотр описания рыбы
    """
    fish = get_object_or_404(Fish, pk=fish_id)
    num_visits = visits(request)
    return render(request,
                  'fishing/fish_details.html',
                  {'fish': fish,
                   'num_visits': num_visits})


@login_required
def fish_renewal(request, fish_id):
    if request.user.is_authenticated:  # is_staff
        fish = get_object_or_404(Fish, pk=fish_id)
        num_visits = visits(request)
        if request.method == 'POST':
            form = FishForm(request.POST)
            if form.is_valid():
                fish.name_of_fish = form.cleaned_data['name_of_fish']
                fish.fish_description = form.cleaned_data['fish_description']
                fish.save()
            return redirect('fishing:fish')
        else:
            form = FishForm(
                initial={'name_of_fish': fish.name_of_fish, 'fish_description': fish.fish_description, })
        return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})
    else:
        return redirect('fishing:fish')


@login_required
def fish_add(request):
    if request.user.is_authenticated:  # is_staff
        fish = Fish()
        num_visits = visits(request)
        if request.method == 'POST':
            form = FishForm(request.POST)
            if form.is_valid():

                fish.name_of_fish = form.cleaned_data['name_of_fish']
                fish.fish_description = form.cleaned_data['fish_description']
                fish.save()
            return redirect('fishing:fish')
        else:
            form = FishForm()
        return render(request, 'fishing/fish_renewal.html', {'form': form, 'fish': fish, 'num_visits': num_visits})
    else:
        return redirect('fishing:fish')


@login_required
def fish_remove(request, fish_id):
    if request.user.is_authenticated:  # is_staff
        fish = get_object_or_404(Fish, pk=fish_id)
        fish.delete()
    return redirect('fishing:fish')


@login_required
def district_list(request):
    """
    Список районов
    """
    districts_list = District.objects.all()
    num_visits = visits(request)
    return render(request,
                  'fishing/districts.html',
                  {'districts_list': districts_list,
                   'num_visits': num_visits})


@login_required
def district_add(request):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
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
    if request.user.is_authenticated:  # is_staff
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
    if request.user.is_authenticated:  # is_staff
        district = get_object_or_404(District, pk=district_id)
        district.delete()
    return redirect('fishing:districts')


@login_required
def priming_list(request):
    """
    Список видов грунта
    """
    primings_list = Priming.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/primings.html',
                  {'primings_list': primings_list,
                   'num_visits': num_visits})


@login_required
def priming_add(request):
    """
    Добавление вида грунта
    """
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
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
    if request.user.is_authenticated:  # is_staff
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
    if request.user.is_authenticated:  # is_staff
        priming = get_object_or_404(Priming, pk=priming_id)
        priming.delete()
    return redirect('fishing:primings')


@login_required
def overcast_list(request):
    overcasts_list = Overcast.objects.all()
    num_visits = visits(request)
    return render(request, 'fishing/overcast.html',
                  {'overcasts_list': overcasts_list,
                   'num_visits': num_visits})


@login_required
def overcast_add(request):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
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
        return redirect('fishing:overcast')


@login_required
def overcast_renewal(request, overcast_id):
    """
    Редактирование облачности
    """
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
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
    if request.user.is_authenticated:  # is_staff
        overcast = get_object_or_404(Overcast, pk=overcast_id)
        overcast.delete()
    return redirect('fishing:overcast')


@login_required
def weather_phenomenas_list(request):
    num_visits = visits(request)
    weather_phenomena_list = WeatherPhenomena.objects.all()
    return render(request, 'fishing/phenomena.html',
                  {'weather_phenomena_list': weather_phenomena_list,
                   'num_visits': num_visits})


@login_required
def weather_phenomenas_add(request):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        weather_phenomena = WeatherPhenomena()

        if request.method == 'POST':
            form = WeatherPhenomenaForm(request.POST)
            if form.is_valid():
                weather_phenomena.weather_phenomena_name = form.cleaned_data[
                    'weather_phenomena_name']
                weather_phenomena.save()
            return redirect('fishing:weatherphenomena')
        else:
            form = WeatherPhenomenaForm()
            return render(
                request,
                'fishing/phenomena_renewal_add.html',
                {'form': form,
                 'weather_penomena': weather_phenomena,
                 'num_visits': num_visits})
    else:
        return redirect('fishing:weatherphenomena')


@login_required
def weather_phenomenas_renewal(request, phenomena_id):
    """
    Редактирование погодного явления
    """
    num_visits = visits(request, phenomena_id)
    if request.user.is_authenticated:  # is_staff
        weather_phenomena = get_object_or_404(
            WeatherPhenomena, pk=phenomena_id)

        if request.method == 'POST':
            form = WeatherPhenomenaForm(request.POST)
            if form.is_valid():
                weather_phenomena.weather_phenomena_name = form.cleaned_data[
                    'weather_phenomena_name']
                weather_phenomena.save()
            return redirect('fishing:weatherphenomena')
        else:
            form = WeatherPhenomenaForm(
                initial={'weather_phenomena_name': weather_phenomena.weather_phenomena_name, })
            return render(request,
                          'fishing/phenomena_renewal_add.html',
                          {'form': form,
                           'phenomena': weather_phenomena,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:weatherphenomena')


@login_required
def weather_phenomenas_remove(request, phenomena_id):
    """
    Удаление явления
    """
    if request.user.is_authenticated:  # is_staff
        weatherphenomena = get_object_or_404(WeatherPhenomena, pk=phenomena_id)
        weatherphenomena.delete()
    return redirect('fishing:weatherphenomena')


@login_required
def feed_capacity_list(request):
    num_visits = visits(request)
    feed_capacity_list = FeedCapacity.objects.all()
    return render(request, 'fishing/feed_capacity.html',
                  {'feed_capacity_list': feed_capacity_list,
                   'nem_visits': num_visits})


@login_required
def feed_capacity_add(request):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        feed_capacity = FeedCapacity()

        if request.method == 'POST':
            form = FeedCapacityForm(request.POST)
            if form.is_valid():
                feed_capacity.feed_capacity_name = form.cleaned_data[
                    'feed_capacity_name']
                feed_capacity.save()
            return redirect('fishing:feed_capacity')
        else:
            form = FeedCapacityForm()
            return render(request,
                          'fishing/feed_capacity_renewal_add.html',
                          {'form': form,
                           'feed_capacity': feed_capacity,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:feed_capacity')


@login_required
def feed_capacity_renewal(request, feed_capacity_id):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        feed_capacity = get_object_or_404(FeedCapacity, pk=feed_capacity_id)

        if request.method == 'POST':
            form = FeedCapacityForm(request.POST)
            if form.is_valid():
                feed_capacity.feed_capacity_name = form.cleaned_data[
                    'feed_capacity_name']
                feed_capacity.save()
            return redirect('fishing:feed_capacity')
        else:
            form = FeedCapacityForm(
                initial={'feed_capacity_name': feed_capacity.feed_capacity_name, })
            return render(request,
                          'fishing/feed_capacity_renewal_add.html',
                          {'form': form,
                           'feed_capacity': feed_capacity,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:feed_capacity')


@login_required
def feed_capacity_remove(request, feed_capacity_id):
    if request.user.is_authenticated:  # is_staff
        feed_capacity = get_object_or_404(FeedCapacity, pk=feed_capacity_id)
        feed_capacity.delete()
    return redirect('fishing:feed_capacity')


@login_required
def pace_list(request):
    num_visits = visits(request)
    pace_list = Pace.objects.all()
    return render(request,
                  'fishing/pace.html',
                  {'pace_list': pace_list,
                   'num_visits': num_visits})


@login_required
def pace_add(request):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        pace = Pace()
        if request.method == 'POST':
            form = PaceForm(request.POST)
            if form.is_valid():
                pace.pace_interval = form.cleaned_data['pace_interval']
                pace.save()
            return redirect('fishing:pace')
        else:
            form = PaceForm()
            return render(request,
                          'fishing/pace_renewal_add.html',
                          {'form': form,
                           'pace': pace,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:pace')


@login_required
def pace_renewal(request, pace_id):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        pace = get_object_or_404(Pace, pk=pace_id)
        if request.method == 'POST':
            form = PaceForm(request.POST)
            if form.is_valid():
                pace.pace_interval = form.cleaned_data['pace_interval']
                pace.save()
            return redirect('fishing:pace')
        else:
            form = PaceForm(initial={'pace_interval': pace.pace_interval, })
            return render(request,
                          'fishing/pace_renewal_add.html',
                          {'form': form,
                           'pace': pace,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:pace')


@login_required
def pace_remove(request, pace_id):
    if request.user.is_authenticated:  # is_staff
        pace = get_object_or_404(Pace, pk=pace_id)
        pace.delete()
    return redirect('fishing:pace')


@login_required
def water_list(request, district_id):
    num_visits = visits(request)
    district_name = get_object_or_404(District, pk=district_id)
    water_list = Water.objects.filter(
        district=district_name)
    return render(request,
                  'fishing/water.html',
                  {'water_list': water_list,
                   'district': district_name,
                   'num_visits': num_visits})


@login_required
def water_add(request, district_id):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        water = Water()
        if request.method == 'POST':
            form = WaterForm(request.POST)
            if form.is_valid():
                water.water_name = form.cleaned_data['water_name']
                disrtict_select = form.cleaned_data['district']
                district = District.objects.filter(
                    district_name=disrtict_select)
                water.district = district[0]
                water.save()
            return redirect('fishing:water', district_id)
        else:
            form = WaterForm(initial={'district': district_id, })
            return render(request,
                          'fishing/water_renewal_add.html',
                          {'form': form,
                           'water': water,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def water_renewal(request, district_id, water_id):
    num_visits = visits(request)
    if request.user.is_authenticated:  # is_staff
        water = get_object_or_404(Water, pk=water_id)
        if request.method == 'POST':
            form = WaterForm(request.POST)
            if form.is_valid():
                water.water_name = form.cleaned_data['water_name']
                disrtict_select = form.cleaned_data['district']
                district = District.objects.filter(
                    district_name=disrtict_select)
                water.district = district[0]
                water.save()
            return redirect('fishing:water', district_id)
        else:
            form = WaterForm(
                initial={'district': water.district,
                         'water_name': water.water_name, })
            return render(request,
                          'fishing/water_renewal_add.html',
                          {'form': form,
                           'water': water,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def water_remove(request, district_id, water_id):
    if request.user.is_authenticated:  # is_staff
        water = get_object_or_404(Water, pk=water_id)
        water.delete()
    return redirect('fishing:water', district_id)


@login_required
def place_list(request, district_id, water_id):
    """
    Список мест, для сотрудников сисок всех мест
    в базе, для остальных список только своих мест
    """
    water = get_object_or_404(Water, pk=water_id)
    if not request.user.is_staff:
        place_list = Place.objects.filter(
            owner=request.user, water=water)
    else:
        place_list = Place.objects.filter(water=water)
    num_visits = visits(request)
    district = get_object_or_404(District, pk=district_id)
    return render(
        request, 'fishing/place.html',
        {'place_list': place_list,
         'district': district,
         'water': water,
         'num_visits': num_visits})


@login_required
def place_detail(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.user.is_staff or place.owner == request.user:
        num_visits = visits(request)
        return render(request,
                      'fishing/place_details.html',
                      {'place': place,
                       'district': district_id,
                       'water': water_id,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:place', district_id, water_id)


@login_required
def place_add(request, district_id, water_id):
    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    place = Place()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place.owner = request.user
            place.water = water
            place.place_locality = form.cleaned_data['place_locality']
            place.place_northern_degree = form.cleaned_data['place_northern_degree']
            place.place_northern_minute = form.cleaned_data['place_northern_minute']
            place.place_northern_second = form.cleaned_data['place_northern_second']
            place.place_easter_degree = form.cleaned_data['place_easter_degree']
            place.place_easter_minute = form.cleaned_data['place_easter_minute']
            place.place_easter_second = form.cleaned_data['place_easter_second']
            place.save()
        return redirect('fishing:place', district_id, water_id)
    else:
        form = PlaceForm()
        return render(request,
                      'fishing/place_renewal_add.html',
                      {'form': form,
                       'place': place,
                       'num_visits': num_visits})


@login_required
def place_renewal(request, district_id, water_id, place_id):
    num_visits = visits(request)
    place = get_object_or_404(Place, pk=place_id)
    if place.owner == request.user:
        if request.method == 'POST':
            form = PlaceForm(request.POST)
            if form.is_valid():
                place.place_locality = form.cleaned_data['place_locality']
                place.place_northern_degree = form.cleaned_data['place_northern_degree']
                place.place_northern_minute = form.cleaned_data['place_northern_minute']
                place.place_northern_second = form.cleaned_data['place_northern_second']
                place.place_easter_degree = form.cleaned_data['place_easter_degree']
                place.place_easter_minute = form.cleaned_data['place_easter_minute']
                place.place_easter_second = form.cleaned_data['place_easter_second']
                place.save()
            return redirect('fishing:place', district_id, water_id)
        else:
            form = PlaceForm(initial={'place_locality': place.place_locality,
                                      'place_northern_degree': place.place_northern_degree,
                                      'place_northern_minute': place.place_northern_minute,
                                      'place_northern_second': place.place_northern_second,
                                      'place_easter_degree': place.place_easter_degree,
                                      'place_easter_minute': place.place_easter_minute,
                                      'place_easter_second': place.place_easter_second})
            return render(request,
                          'fishing/place_renewal_add.html',
                          {'form': form,
                           'place': place,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:place', district_id, water_id)


@login_required
def place_remove(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if place.owner == request.user:
        place.delete()
    return redirect('fishing:place', district_id, water_id)


@login_required
def fishing_point_list(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if not request.user.is_staff:
        fishing_point_list = FishingPoint.objects.filter(
            owner=request.user, place=place)
    else:
        fishing_point_list = FishingPoint.objects.filter(place=place)

    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    district = get_object_or_404(District, pk=district_id)
    return render(
        request, 'fishing/fishing_point.html',
        {'fishing_point_list': fishing_point_list,
         'district': district,
         'water': water,
         'place': place,
         'num_visits': num_visits})


@login_required
def fishing_point_add(request, district_id, water_id, place_id):
    num_visits = visits(request)
    place = get_object_or_404(Place, pk=place_id)
    if place.owner == request.user:
        fishing_point = FishingPoint()
        if request.method == 'POST':
            form = FishingPointForm(request.POST)
            if form.is_valid():
                fishing_point.owner = request.user
                fishing_point.place = place
                fishing_point.fishing_point_azimuth = form.cleaned_data['fishing_point_azimuth']
                fishing_point.fishing_point_distance = form.cleaned_data['fishing_point_distance']
                fishing_point.fishing_poiny_depth = form.cleaned_data['fishing_poiny_depth']
                priming_name = form.cleaned_data['priming']
                priming = Priming.objects.filter(priming_name=priming_name)
                fishing_point.priming = priming[0]
                fishing_point.save()
            return redirect('fishing:fishing_point', district_id, water_id, place_id)
        else:
            form = FishingPointForm()
            return render(request,
                          'fishing/fishing_point_renewal_add.html',
                          {'form': form,
                           'fishing_point': fishing_point,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def fishing_point_renewal(request, district_id, water_id, place_id, fishing_point_id):
    num_visits = visits(request)
    fishing_point = get_object_or_404(FishingPoint, pk=fishing_point_id)
    if fishing_point.owner == request.user:
        if request.method == 'POST':
            form = FishingPointForm(request.POST)
            if form.is_valid():
                fishing_point.fishing_point_azimuth = form.cleaned_data['fishing_point_azimuth']
                fishing_point.fishing_point_distance = form.cleaned_data['fishing_point_distance']
                fishing_point.fishing_poiny_depth = form.cleaned_data['fishing_poiny_depth']
                priming_name = form.cleaned_data['priming']
                priming = Priming.objects.filter(priming_name=priming_name)
                fishing_point.priming = priming[0]
                fishing_point.save()
            return redirect('fishing:fishing_point', district_id, water_id, place_id)
        else:
            form = FishingPointForm(initial={'fishing_point_azimuth': fishing_point.fishing_point_azimuth,
                                             'fishing_point_distance': fishing_point.fishing_point_distance,
                                             'fishing_poiny_depth': fishing_point.fishing_poiny_depth,
                                             'priming': fishing_point.priming, })
            return render(request,
                          'fishing/fishing_point_renewal_add.html',
                          {'form': form,
                           'fishing_point': fishing_point,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def fishing_point_details(request, district_id, water_id, place_id, fishing_point_id):
    fishing_point = get_object_or_404(FishingPoint, pk=fishing_point_id)
    if request.user.is_staff or fishing_point.owner == request.user:
        num_visits = visits(request)
        return render(request,
                      'fishing/fishing_point_details.html',
                      {'fishing_point': fishing_point,
                       'place': place_id,
                       'district': district_id,
                       'water': water_id,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def fishing_point_remove(request, district_id, water_id, place_id, fishing_point_id):
    fishing_point = get_object_or_404(FishingPoint, pk=fishing_point_id)
    if fishing_point.owner == request.user:
        fishing_point.delete()
    return redirect('fishing:water', district_id)

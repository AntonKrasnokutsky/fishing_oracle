from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404

from .models import Fishing

from .models import Fish
from .forms import FishForm

from .models import Weather, Overcast, WeatherPhenomena
from .forms import WeatherForm, OvercastForm, WeatherPhenomenaForm

from .models import FeedCapacity
from .forms import FeedCapacityForm

from .models import Pace
from .forms import PaceForm

from .models import District, Water, Place, FishingPoint, BottomMap, Point, Priming
from .forms import DistrictForm, WaterForm, PlaceForm, FishingPointForm, BottomMapForm, PointForm, PrimingForm

from .models import FishingTackle, FishingMontage, ModelTroughName, ModelTrough
from .forms import FishingTackleForm, FishingMontageForm, ModelTroughNameForm, ModelTroughForm

from .models import FishingTrough
from .forms import FishingTroughForm

from .models import NozzleState, Nozzle, Lure, LureBase, FishingLure
from .forms import NozzleStateForm, NozzleForm, LureForm, LureBaseForm, FishingLureForm

from .models import AromaBase, Aroma
from .forms import AromaBaseForm, AromaForm

from .models import Crochet, FishingLeash
from .forms import CrochetForm, FishingLeashForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Переменные
template_renewal_add_path = 'fishing/renewal_add.html'
template_list_path = 'fishing/list.html'
template_details_path = 'fishing/details.html'


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
def aroma_add(request, fishing_lure_id):
    num_visits = visits(request)
    if request.method == 'POST':
        aroma = Aroma()
        form = AromaForm(request.POST)
        if form.is_valid():
            aroma = form.save(commit=False)
            aroma.owner = request.user
            fishing_lure = get_object_or_404(FishingLure, pk=fishing_lure_id)
            aroma.fishing_lure = fishing_lure
            aroma.save()
            return redirect('fishing:fishing_lure_details', fishing_lure_id)
    else:
        form = AromaForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def aroma_remove(request, fishing_lure_id, aroma_id):
    aroma = get_object_or_404(Aroma, pk=aroma_id)
    if aroma.owner == request.user:
        aroma.delete()
    return redirect('fishing:fishing_lure_details', fishing_lure_id)


@login_required
def aroma_renewal(request, fishing_lure_id, aroma_id):
    num_visits = visits(request)
    aroma = get_object_or_404(Aroma, pk=aroma_id)
    if aroma.owner == request.user:
        if request.method == 'POST':
            form = AromaForm(request.POST, instance=aroma)
            if form.is_valid():
                aroma = form.save(commit=False)
                aroma.owner = request.user
                fishing_lure = get_object_or_404(
                    FishingLure, pk=fishing_lure_id)
                aroma.fishing_lure = fishing_lure
                aroma.save()
                return redirect('fishing:fishing_lure_details', fishing_lure_id)
        else:
            form = AromaForm(initial={
                'aroma_base': aroma.aroma_base,
                'aroma_volume': aroma.aroma_volume})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})


@login_required
def aroma_base_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        aroma_base = AromaBase()
        form = AromaBaseForm(request.POST)
        if form.is_valid():
            aroma_base = form.save(commit=False)
            aroma_base.owner = request.user
            aroma_base.save()
        return redirect('fishing:aroma_base')
    else:
        form = AromaBaseForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def aroma_base_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        aroma_base_list = AromaBase.objects.all()
    else:
        aroma_base_list = AromaBase.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'aroma_base_list': aroma_base_list,
                   'num_visits': num_visits})


@login_required
def aroma_base_remove(request, aroma_base_id):
    aroma_base = get_object_or_404(AromaBase, pk=aroma_base_id)
    if aroma_base.owner == request.user:
        aroma_base.delete()
    return redirect('fishing:aroma_base')


@login_required
def aroma_base_renewal(request, aroma_base_id):
    num_visits = visits(request)
    aroma_base = get_object_or_404(AromaBase, pk=aroma_base_id)
    if aroma_base.owner == request.user:
        if request.method == 'POST':
            form = AromaBaseForm(request.POST, instance=aroma_base)
            if form.is_valid():
                aroma_base = form.save(commit=False)
                aroma_base.owner = request.user
                aroma_base.save()
            return redirect('fishing:aroma_base')
        else:
            form = AromaBaseForm(initial={
                'aroma_manufacturer': aroma_base.aroma_manufacturer,
                'aroma_name': aroma_base.aroma_name,
                'num_visits': num_visits})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:aroma_base')


@login_required
def bottom_map_add(request, district_id, water_id, place_id):
    num_visits = visits(request)
    place = get_object_or_404(Place, pk=place_id)
    if place.owner == request.user:
        bottom_map = BottomMap()
        if request.method == 'POST':
            form = BottomMapForm(request.POST)
            if form.is_valid():
                bottom_map.owner = request.user
                bottom_map.place = place
                bottom_map.bottom_map_northern_degree = form.cleaned_data[
                    'bottom_map_northern_degree']
                bottom_map.bottom_map_northern_minute = form.cleaned_data[
                    'bottom_map_northern_minute']
                bottom_map.bottom_map_northern_second = form.cleaned_data[
                    'bottom_map_northern_second']
                bottom_map.bottom_map_easter_degree = form.cleaned_data['bottom_map_easter_degree']
                bottom_map.bottom_map_easter_minute = form.cleaned_data['bottom_map_easter_minute']
                bottom_map.bottom_map_easter_second = form.cleaned_data['bottom_map_easter_second']
                bottom_map.save()
            return redirect('fishing:bottom_map', district_id, water_id, place_id)
        else:
            form = BottomMapForm()
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'bottom_map': bottom_map,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_details(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if request.user.is_staff or bottom_map.owner == request.user:
        num_visits = visits(request)
        return render(request,
                      template_details_path,
                      {'bottom_map': bottom_map,
                       'place_id': place_id,
                       'district_id': district_id,
                       'water_id': water_id,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_list(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if not request.user.is_staff:
        bottom_map_list = BottomMap.objects.filter(
            owner=request.user, place=place)
    else:
        bottom_map_list = BottomMap.objects.filter(place=place)

    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    district = get_object_or_404(District, pk=district_id)
    return render(request,
                  template_list_path,
                  {'bottom_map_list': bottom_map_list,
                   'district': district,
                   'water': water,
                   'place': place,
                   'num_visits': num_visits})


@login_required
def bottom_map_remove(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if bottom_map.owner == request.user:
        bottom_map.delete()
    return redirect('fishing:bottom_map', district_id, water_id, place_id)


@login_required
def bottom_map_renewal(request, district_id, water_id, place_id, bottom_map_id):
    num_visits = visits(request)
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if bottom_map.owner == request.user:
        if request.method == 'POST':
            form = BottomMapForm(request.POST)
            if form.is_valid():
                bottom_map.bottom_map_northern_degree = form.cleaned_data[
                    'bottom_map_northern_degree']
                bottom_map.bottom_map_northern_minute = form.cleaned_data[
                    'bottom_map_northern_minute']
                bottom_map.bottom_map_northern_second = form.cleaned_data[
                    'bottom_map_northern_second']
                bottom_map.bottom_map_easter_degree = form.cleaned_data['bottom_map_easter_degree']
                bottom_map.bottom_map_easter_minute = form.cleaned_data['bottom_map_easter_minute']
                bottom_map.bottom_map_easter_second = form.cleaned_data['bottom_map_easter_second']
                bottom_map.save()
            return redirect('fishing:bottom_map', district_id, water_id, place_id)
        else:
            form = BottomMapForm(initial={'bottom_map_northern_degree': bottom_map.bottom_map_northern_degree,
                                          'bottom_map_northern_minute': bottom_map.bottom_map_northern_minute,
                                          'bottom_map_northern_second': bottom_map.bottom_map_northern_second,
                                          'bottom_map_easter_degree': bottom_map.bottom_map_easter_degree,
                                          'bottom_map_easter_minute': bottom_map.bottom_map_easter_minute,
                                          'bottom_map_easter_second': bottom_map.bottom_map_easter_second, })
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'bottom_map': bottom_map,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_add(request, district_id, water_id, place_id, bottom_map_id):
    num_visits = visits(request)
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if bottom_map.owner == request.user:
        point = Point()
        if request.method == 'POST':
            form = PointForm(request.POST)
            if form.is_valid():
                point.owner = request.user
                point.bottom_map = bottom_map
                point.point_azimuth = form.cleaned_data['point_azimuth']
                point.point_distance = form.cleaned_data['point_distance']
                point.point_depth = form.cleaned_data['point_depth']
                priming_set = form.cleaned_data['priming']
                priming = Priming.objects.filter(priming_name=priming_set)
                point.priming = priming[0]
                point.save()
            return redirect('fishing:point', district_id, water_id, place_id, bottom_map_id)
        else:
            form = PointForm()
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'point': point,
                           'district': district_id,
                           'water': water_id,
                           'place': place_id,
                           'bottom_map': bottom_map_id,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_details(request, district_id, water_id, place_id, bottom_map_id, point_id):
    point = get_object_or_404(Point, pk=point_id)
    if request.user.is_staff or point.owner == request.user:
        num_visits = visits(request)
        return render(request,
                      template_details_path,
                      {'point': point,
                       'bottom_map': bottom_map_id,
                       'place': place_id,
                       'district': district_id,
                       'water': water_id,
                       'num_visits': num_visits})
    return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_list(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if not request.user.is_staff:
        point_list = Point.objects.filter(
            owner=request.user, bottom_map=bottom_map)
    else:
        point_list = Point.objects.filter(bottom_map=bottom_map)

    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    district = get_object_or_404(District, pk=district_id)
    place = get_object_or_404(Place, pk=place_id)
    return render(request,
                  template_list_path,
                  {'point_list': point_list,
                   'district': district,
                   'water': water,
                   'place': place,
                   'bottom_map': bottom_map,
                   'num_visits': num_visits})


@login_required
def bottom_map_point_remove(request, district_id, water_id, place_id, bottom_map_id, point_id):
    point = get_object_or_404(Point, pk=point_id)
    if point.owner == request.user:
        point.delete()
    return redirect('fishing:point', district_id, water_id, place_id, bottom_map_id)


@login_required
def bottom_map_point_renewal(request, district_id, water_id, place_id, bottom_map_id, point_id):
    num_visits = visits(request)
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if bottom_map.owner == request.user:
        point = get_object_or_404(Point, pk=point_id)
        if request.method == 'POST':
            form = PointForm(request.POST)
            if form.is_valid():
                point.point_azimuth = form.cleaned_data['point_azimuth']
                point.point_distance = form.cleaned_data['point_distance']
                point.point_depth = form.cleaned_data['point_depth']
                priming_set = form.cleaned_data['priming']
                priming = Priming.objects.filter(priming_name=priming_set)
                point.priming = priming[0]
                point.save()
            return redirect('fishing:point', district_id, water_id, place_id, bottom_map_id)
        else:
            form = PointForm(initial={'point_azimuth': point.point_azimuth,
                                      'point_distance': point.point_distance,
                                      'point_depth': point.point_depth,
                                      'priming': point.priming})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'point': point,
                           'district': district_id,
                           'water': water_id,
                           'place': place_id,
                           'bottom_map': bottom_map_id,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def crochet_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        crochet = Crochet()
        form = CrochetForm(request.POST)
        if form.is_valid():
            crochet = form.save(commit=False)
            crochet.owner = request.user
            crochet.save()
        return redirect('fishing:crochet')
    else:
        form = CrochetForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def crochet_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        crochet_list = Crochet.objects.all()
    else:
        crochet_list = Crochet.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'crochet_list': crochet_list,
                   'num_visits': num_visits})


@login_required
def crochet_remove(request, crochet_id):
    crochet = get_object_or_404(Crochet, pk=crochet_id)
    if crochet.owner == request.user:
        crochet.delete()
    return redirect('fishing:crochet')


@login_required
def crochet_renewal(request, crochet_id):
    num_visits = visits(request)
    crochet = get_object_or_404(Crochet, pk=crochet_id)
    if crochet.owner == request.user:
        if request.method == 'POST':
            form = CrochetForm(request.POST, instance=crochet)
            if form.is_valid():
                crochet = form.save(commit=False)
                crochet.owner = request.user
                crochet.save()
            return redirect('fishing:crochet')
        else:
            form = CrochetForm(initial={'crochet_manufacturer': crochet.crochet_manufacturer,
                                        'crochet_model': crochet.crochet_model,
                                        'crochet_size': crochet.crochet_size})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})


@staff_member_required
def district_add(request):
    num_visits = visits(request)
    district = District()
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district.district_name = form.cleaned_data['district_name']
            district.save()
        return redirect('fishing:districts')
    else:
        form = DistrictForm()
    return render(request, template_renewal_add_path,
                  {'form': form,
                   'district': district,
                   'num_visits': num_visits})


@login_required
def district_list(request):
    """
    Список районов
    """
    districts_list = District.objects.all()
    num_visits = visits(request)
    return render(request,
                  template_list_path,
                  {'districts_list': districts_list,
                   'num_visits': num_visits})


@staff_member_required
def district_remove(request, district_id):
    """
    Удаление района
    """
    district = get_object_or_404(District, pk=district_id)
    district.delete()
    return redirect('fishing:districts')


@staff_member_required
def district_renewal(request, district_id):
    """
    Редактирование района
    """
    num_visits = visits(request)
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
    return render(request, template_renewal_add_path,
                  {'form': form,
                   'district': district,
                   'num_visits': num_visits})


@staff_member_required
def feed_capacity_add(request):
    num_visits = visits(request)
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
                      template_renewal_add_path,
                      {'form': form,
                       'feed_capacity': feed_capacity,
                       'num_visits': num_visits})


@login_required
def feed_capacity_list(request):
    num_visits = visits(request)
    feed_capacity_list = FeedCapacity.objects.all()
    return render(request,
                  template_list_path,
                  {'feed_capacity_list': feed_capacity_list,
                   'nem_visits': num_visits})


@staff_member_required
def feed_capacity_remove(request, feed_capacity_id):
    feed_capacity = get_object_or_404(FeedCapacity, pk=feed_capacity_id)
    feed_capacity.delete()
    return redirect('fishing:feed_capacity')


@staff_member_required
def feed_capacity_renewal(request, feed_capacity_id):
    num_visits = visits(request)
    feed_capacity = get_object_or_404(FeedCapacity, pk=feed_capacity_id)
    if request.method == 'POST':
        form = FeedCapacityForm(request.POST, instance=feed_capacity)
        if form.is_valid():
            feed_capacity.feed_capacity_name = form.cleaned_data[
                'feed_capacity_name']
            feed_capacity.save()
        return redirect('fishing:feed_capacity')
    else:
        form = FeedCapacityForm(
            initial={'feed_capacity_name': feed_capacity.feed_capacity_name, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'feed_capacity': feed_capacity,
                       'num_visits': num_visits})


@staff_member_required
def fish_add(request):
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
    return render(request, template_renewal_add_path,
                  {'form': form,
                   'fish': fish,
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


def fish_list(request):
    """
    Список рыб
    """
    fishs_list = Fish.objects.all()
    num_visits = visits(request)
    return render(request,
                  template_list_path,
                  {'fish_list': fishs_list,
                   'num_visits': num_visits})


@staff_member_required
def fish_remove(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    fish.delete()
    return redirect('fishing:fish')


@staff_member_required
def fish_renewal(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    num_visits = visits(request)
    if request.method == 'POST':
        form = FishForm(request.POST, instance=fish)
        if form.is_valid():
            fish.name_of_fish = form.cleaned_data['name_of_fish']
            fish.fish_description = form.cleaned_data['fish_description']
            fish.save()
        return redirect('fishing:fish')
    else:
        form = FishForm(
            initial={'name_of_fish': fish.name_of_fish,
                     'fish_description': fish.fish_description, })
    return render(request, template_renewal_add_path,
                  {'form': form,
                   'fish': fish,
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
        return render(request,
                      template_details_path,
                      {'fishing': fishing,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:fishing')


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
    return render(request,
                  template_list_path,
                  {'fishing_list': fishings_list,
                   'num_visits': num_visits})


@login_required
def fishing_leash_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        fishing_leash = FishingLeash()
        form = FishingLeashForm(request.POST)
        if form.is_valid():
            fishing_leash = form.save(commit=False)
            fishing_leash.owner = request.user
            fishing_leash.save()
        return redirect('fishing:fishing_leash')
    else:
        form = FishingLeashForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_leash_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        fishing_leash_list = FishingLeash.objects.all()
    else:
        fishing_leash_list = FishingLeash.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'fishing_leash_list': fishing_leash_list,
                   'num_visits': num_visits})


@login_required
def fishing_leash_remove(request, fishing_leash_id):
    fishing_leash = get_object_or_404(FishingLeash, pk=fishing_leash_id)
    if fishing_leash.owner == request.user:
        fishing_leash.delete()
    return redirect('fishing:fishing_leash')


@login_required
def fishing_leash_renewal(request, fishing_leash_id):
    num_visits = visits(request)
    fishing_leash = get_object_or_404(FishingLeash, pk=fishing_leash_id)
    if fishing_leash.owner == request.user:
        if request.method == 'POST':
            form = FishingLeashForm(request.POST, instance=fishing_leash)
            if form.is_valid():
                fishing_leash = form.save(commit=False)
                fishing_leash.owner = request.user
                fishing_leash.save()
            return redirect('fishing:fishing_leash')
        else:
            form = FishingLeashForm(initial={'fishing_leash_material': fishing_leash.fishing_leash_material,
                                             'fishing_leash_diameter': fishing_leash.fishing_leash_diameter,
                                             'fishing_leash_length': fishing_leash.fishing_leash_length})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing_leash')


@login_required
def fishing_lure_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        fishing_lure = FishingLure()
        form = FishingLureForm(request.POST)
        if form.is_valid():
            fishing_lure.owner = request.user
            nozzle_select = form.cleaned_data['nozzle']
            nozzle = Nozzle.objects.filter(nozzle_name=nozzle_select)
            fishing_lure.nozzle = nozzle[0]
            nozzle_state_select = form.cleaned_data['nozzle_state']
            nozzle_state = NozzleState.objects.filter(
                state=nozzle_state_select)
            fishing_lure.nozzle_state = nozzle_state[0]
            fishing_lure.save()
            return redirect('fishing:fishing_lure')
    else:
        form = FishingLureForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_lure_details(request, fishing_lure_id):
    num_visits = visits(request)
    fishing_lure = get_object_or_404(FishingLure, pk=fishing_lure_id)
    if request.user.is_staff or fishing_lure.owner == request.user:
        return render(request,
                      template_details_path,
                      {'fishing_lure': fishing_lure,
                       'num_visits': num_visits})
    return redirect('fishing:fishing_lure')


@login_required
def fishing_lure_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        fishing_lure_list = FishingLure.objects.all()
    else:
        fishing_lure_list = FishingLure.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'fishing_lure_list': fishing_lure_list,
                   'num_visits': num_visits})


@login_required
def fishing_lure_remove(request, fishing_lure_id):
    fishing_lure = get_object_or_404(FishingLure, pk=fishing_lure_id)
    if fishing_lure.owner == request.user:
        fishing_lure.delete()
    return redirect('fishing:fishing_lure')


@login_required
def fishing_lure_renewal(request, fishing_lure_id):
    num_visits = visits(request)
    fishing_lure = get_object_or_404(FishingLure, pk=fishing_lure_id)
    if fishing_lure.owner == request.user:
        if request.method == 'POST':
            form = FishingLureForm(request.POST)
            if form.is_valid():
                nozzle_select = form.cleaned_data['nozzle']
                nozzle = Nozzle.objects.filter(nozzle_name=nozzle_select)
                fishing_lure.nozzle = nozzle
                nozzle_state_select = form.cleaned_data['nozzle_state']
                nozzle_state = NozzleState.objects.filter(
                    state=nozzle_state_select)
                fishing_lure.nozzle_state = nozzle_state
                fishing_lure.save()
                return redirect('fishing:fishnig_lure')
        else:
            form = FishingLureForm(initial={'nozzle': fishing_lure.nozzle,
                                            'npzzle_state': fishing_lure.nozzle_state,
                                            'num_visits': num_visits})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing_lure')


@login_required
def fishing_montage_add(request):
    num_visits = visits(request)
    fishing_montage = FishingMontage()
    if request.method == 'POST':
        form = FishingMontageForm(request.POST)
        if form.is_valid():
            fishing_montage.owner = request.user
            fishing_montage.fishing_montage_name = form.cleaned_data['fishing_montage_name']
            fishing_montage.fishing_montage_sliding = form.cleaned_data['fishing_montage_sliding']
            fishing_montage.save()
            return redirect('fishing:fishing_montage')
    else:
        form = FishingMontageForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_montage_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        fishing_montage_list = FishingMontage.objects.all()
    else:
        fishing_montage_list = FishingMontage.objects.filter(
            owner=request.user)
    return render(request,
                  template_list_path,
                  {'fishing_montage_list': fishing_montage_list,
                   'num_visits': num_visits})


@login_required
def fishing_montage_remove(request, fishing_montage_id):
    fishing_montage = get_object_or_404(FishingMontage, pk=fishing_montage_id)
    if fishing_montage.owner == request.user:
        fishing_montage.delete()
    return redirect('fishing:fishing_montage')


@login_required
def fishing_montage_renewal(request, fishing_montage_id):
    num_visits = visits(request)
    fishing_montage = get_object_or_404(FishingMontage, pk=fishing_montage_id)
    if request.method == 'POST':
        form = FishingMontageForm(request.POST)
        if form.is_valid():
            fishing_montage.fishing_montage_name = form.cleaned_data['fishing_montage_name']
            fishing_montage.fishing_montage_sliding = form.cleaned_data['fishing_montage_sliding']
            fishing_montage.save()
            return redirect('fishing:fishing_montage')
    else:
        form = FishingMontageForm(
            initial={'fishing_montage_name': fishing_montage.fishing_montage_name,
                     'fishing_montage_sliding': fishing_montage.fishing_montage_sliding}
        )
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


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
    return render(request,
                  template_list_path,
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
                          template_renewal_add_path,
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
                      template_details_path,
                      {'fishing_point': fishing_point,
                       'place_id': place_id,
                       'district_id': district_id,
                       'water_id': water_id,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def fishing_point_remove(request, district_id, water_id, place_id, fishing_point_id):
    fishing_point = get_object_or_404(FishingPoint, pk=fishing_point_id)
    if fishing_point.owner == request.user:
        fishing_point.delete()
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
                          template_renewal_add_path,
                          {'form': form,
                           'fishing_point': fishing_point,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:water', district_id)


@login_required
def fishing_tackle_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        fishing_tackle = FishingTackle()
        form = FishingTackleForm(request.POST)
        if form.is_valid:
            fishing_tackle.owner = request.user
            fishing_tackle.fishing_tackle_manufacturer = form.cleaned_data[
                'fishing_tackle_manufacturer']
            fishing_tackle.fishing_tackle_name = form.cleaned_data['fishing_tackle_name']
            fishing_tackle.fishing_tackle_length = form.cleaned_data['fishing_tackle_length']
            fishing_tackle.fishing_tackle_casting_weight = form.cleaned_data[
                'fishing_tackle_casting_weight']
            fishing_tackle.save()
        return redirect('fishing:fishing_tackle')
    else:
        form = FishingTackleForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_tackle_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        fishing_tackle_list = FishingTackle.objects.all()
    else:
        fishing_tackle_list = FishingTackle.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'fishing_tackle_list': fishing_tackle_list,
                   'num_visits': num_visits})


@login_required
def fishing_tackle_remove(request, fishing_tackle_id):
    fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
    if fishing_tackle.owner == request.user:
        fishing_tackle.delete()
    return redirect('fishing:fishing_tackle')


@login_required
def fishing_tackle_renewal(request, fishing_tackle_id):
    num_visits = visits(request)
    fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
    if request.method == 'POST':
        form = FishingTackleForm(request.POST)
        if form.is_valid:
            fishing_tackle.fishing_tackle_manufacturer = form.cleaned_data[
                'fishing_tackle_manufacturer']
            fishing_tackle.fishing_tackle_name = form.cleaned_data['fishing_tackle_name']
            fishing_tackle.fishing_tackle_length = form.cleaned_data['fishing_tackle_length']
            fishing_tackle.fishing_tackle_casting_weight = form.cleaned_data[
                'fishing_tackle_casting_weight']
            fishing_tackle.save()
        return redirect('fishing:fishing_tackle')
    else:
        form = FishingTackleForm(
            initial={'fishing_tackle_manufacturer': fishing_tackle.fishing_tackle_manufacturer,
                     'fishing_tackle_name': fishing_tackle.fishing_tackle_name,
                     'fishing_tackle_length': fishing_tackle.fishing_tackle_length,
                     'fishing_tackle_casting_weight': fishing_tackle.fishing_tackle_casting_weight})
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_trough_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        fishing_trough = FishingTrough()
        form = FishingTroughForm(request.POST)
        if form.is_valid():
            fishing_trough.owner = request.user
            fishing_trough.fishing_trough_manufacturer = form.cleaned_data[
                'fishing_trough_manufacturer']
            model_trough_select = form.cleaned_data['model_trough']
            model_trough_name = ModelTroughName.objects.filter(
                model_trough_name=model_trough_select)
            model_trough = ModelTrough.objects.filter(
                model_trough_name=model_trough_name[0])
            fishing_trough.model_trough = model_trough[0]
            feed_capacity_select = form.cleaned_data['feed_capacity']
            feed_capacity = FeedCapacity.objects.filter(
                feed_capacity_name=feed_capacity_select)
            fishing_trough.feed_capacity = feed_capacity[0]
            fishing_trough.fishing_trough_weight = form.cleaned_data['fishing_trough_weight']
            fishing_trough.save()
        return redirect('fishing:fishing_trough')
    else:
        form = FishingTroughForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def fishing_trough_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        fishing_trough_list = FishingTrough.objects.all()
    else:
        fishing_trough_list = FishingTrough.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'fishing_trough_list': fishing_trough_list,
                   'num_visits': num_visits})


@login_required
def fishing_trough_remove(request, fishing_trough_id):
    fishing_trough = get_object_or_404(FishingTrough, pk=fishing_trough_id)
    if fishing_trough.owner == request.user:
        fishing_trough.delete()
    return redirect('fishing:fishing_trough')


@login_required
def fishing_trough_renewal(request, fishing_trough_id):
    num_visits = visits(request)
    fishing_trough = get_object_or_404(FishingTrough, pk=fishing_trough_id)
    if fishing_trough.owner == request.user:
        if request.method == 'POST':
            form = FishingTroughForm(request.POST)
            if form.is_valid():
                fishing_trough.fishing_trough_manufacturer = form.cleaned_data[
                    'fishing_trough_manufacturer']
                model_trough_select = form.cleaned_data['model_trough']
                model_trough_name = ModelTroughName.objects.filter(
                    model_trough_name=model_trough_select)
                model_trough = ModelTrough.objects.filter(
                    model_trough_name=model_trough_name[0])
                fishing_trough.model_trough = model_trough[0]
                feed_capacity_select = form.cleaned_data['feed_capacity']
                feed_capacity = FeedCapacity.objects.filter(
                    feed_capacity_name=feed_capacity_select)
                fishing_trough.feed_capacity = feed_capacity[0]
                fishing_trough.fishing_trough_weight = form.cleaned_data['fishing_trough_weight']
                fishing_trough.save()
            return redirect('fishing:fishing_trough')
        else:
            form = FishingTroughForm(
                initial={'fishing_trough_manufacturer': fishing_trough.fishing_trough_manufacturer,
                         'model_trough': fishing_trough.model_trough,
                         'feed_capacity': fishing_trough.feed_capacity,
                         'fishing_trough_weight': fishing_trough.fishing_trough_weight}
            )
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing_trough')


@login_required
def lure_add(request, fishing_lure_id):
    num_visits = visits(request)
    if request.method == 'POST':
        lure = Lure()
        form = LureForm(request.POST)
        if form.is_valid():
            fishing_lure = get_object_or_404(FishingLure, pk=fishing_lure_id)
            lure = form.save(commit=False)
            lure.owner = request.user
            lure.fishing_lure = fishing_lure
            lure.save()
            return redirect('fishing:fishing_lure_details',
                            fishing_lure_id)
    else:
        form = LureForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def lure_remove(request, fishing_lure_id, lure_id):
    lure = get_object_or_404(Lure, pk=lure_id)
    if lure.owner == request.user:
        lure.delete()
    return redirect('fishing:fishing_lure_details', fishing_lure_id)


@login_required
def lure_renewal(request, fishing_lure_id, lure_id):
    num_visits = visits(request)
    lure = get_object_or_404(Lure, pk=lure_id)
    if lure.owner == request.user:
        if request.method == 'POST':
            form = LureForm(request.POST, instance=lure)
            if form.is_valid():
                fishing_lure = get_object_or_404(
                    FishingLure, pk=fishing_lure_id)
                lure = form.save(commit=False)
                lure.owner = request.user
                lure.fishing_lure = fishing_lure
                lure.save()
                return redirect('fishing:fishing_lure_details',
                                fishing_lure_id)
        else:
            form = LureForm(initial={'lure_base': lure.lure_base,
                                     'lure_weight': lure.lure_weight})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})


@login_required
def lure_base_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        lure_base_list = LureBase.objects.all()
    else:
        lure_base_list = LureBase.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'lure_base_list': lure_base_list,
                   'num_visits': num_visits})


@login_required
def lure_base_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        lure_base = LureBase()
        form = LureBaseForm(request.POST)
        if form.is_valid():
            lure_base.owner = request.user
            lure_base.lure_manufacturer = form.cleaned_data['lure_manufacturer']
            lure_base.lure_name = form.cleaned_data['lure_name']
            lure_base.save()
            return redirect('fishing:lure_base')
    else:
        form = LureBaseForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def lure_base_remove(request, lure_base_id):
    lure_base = get_object_or_404(LureBase, pk=lure_base_id)
    if lure_base.owner == request.user:
        lure_base.delete()
    return redirect('fishing:lure_base')


@login_required
def lure_base_renewal(request, lure_base_id):
    num_visits = visits(request)
    lure_base = get_object_or_404(LureBase, pk=lure_base_id)
    if lure_base.owner == request.user:
        if request.method == 'POST':
            form = LureBaseForm(request.POST)
            if form.is_valid():
                lure_base.lure_manufacturer = form.cleaned_data['lure_manufacturer']
                lure_base.lure_name = form.cleaned_data['lure_name']
                lure_base.save()
                return redirect('fishing:lure_base')
        else:
            form = LureBaseForm()
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:lure_base')


@login_required
def model_trough_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        model_trough = ModelTrough()
        form = ModelTroughForm(request.POST)
        if form.is_valid():
            model_trough.owner = request.user
            model_trough.model_trough_name = form.cleaned_data['model_trough_name']
            model_trough.model_trough_plastic = form.cleaned_data['model_trough_plastic']
            model_trough.model_trough_lugs = form.cleaned_data['model_trough_lugs']
            model_trough.save()
            return redirect('fishing:model_trough')
    else:
        form = ModelTroughForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def model_trough_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        model_trough_list = ModelTrough.objects.all()
    else:
        model_trough_list = ModelTrough.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'model_trough_list': model_trough_list,
                   'num_visits': num_visits})


@login_required
def model_trough_remove(request, model_trough_id):
    model_trough = get_object_or_404(ModelTrough, pk=model_trough_id)
    if model_trough.owner == request.user:
        model_trough.delete()
    return redirect('fishing:model_trough')


@login_required
def model_trough_renewal(request, model_trough_id):
    num_visits = visits(request)
    model_trough = get_object_or_404(ModelTrough, pk=model_trough_id)
    if request.method == 'POST':
        form = ModelTroughForm(request.POST)
        if form.is_valid():
            model_trough.model_trough_name = form.cleaned_data['model_trough_name']
            model_trough.model_trough_plastic = form.cleaned_data['model_trough_plastic']
            model_trough.model_trough_lugs = form.cleaned_data['model_trough_lugs']
            model_trough.save()
            return redirect('fishing:model_trough')
    else:
        form = ModelTroughForm(
            initial={'model_trough_name': model_trough.model_trough_name,
                     'model_trough_plastic': model_trough.model_trough_plastic,
                     'model_trough_lugs': model_trough.model_trough_lugs, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def model_trough_name_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        model_trough_name = ModelTroughName()
        form = ModelTroughNameForm(request.POST)
        if form.is_valid():
            model_trough_name.owner = request.user
            model_trough_name.model_trough_name = form.cleaned_data['model_trough_name']
            model_trough_name.save()
            return redirect('fishing:model_trough_name')
    else:
        form = ModelTroughNameForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def model_trough_name_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        model_trough_name_list = ModelTroughName.objects.all()
    else:
        model_trough_name_list = ModelTroughName.objects.filter(
            owner=request.user)
    return render(request,
                  template_list_path,
                  {'model_trough_name_list': model_trough_name_list,
                   'num_visits': num_visits})


@login_required
def model_trough_name_remove(request, model_trough_name_id):
    model_trough_name = get_object_or_404(
        ModelTroughName, pk=model_trough_name_id)
    if model_trough_name.owner == request.user:
        model_trough_name.delete()
    return redirect('fishing:model_trough_name')


@login_required
def model_trough_name_renewal(request, model_trough_name_id):
    num_visits = visits(request)
    model_trough_name = get_object_or_404(
        ModelTroughName, pk=model_trough_name_id)
    if request.method == 'POST':
        form = ModelTroughNameForm(request.POST)
        if form.is_valid():
            model_trough_name.model_trough_name = form.cleaned_data['model_trough_name']
            model_trough_name.save()
            return redirect('fishing:model_trough_name')
    else:
        form = ModelTroughNameForm(
            initial={'model_trough_name': model_trough_name.model_trough_name, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def nozzle_add(request):
    num_visits = visits(request)
    if request.method == "POST":
        nozzle = Nozzle()
        form = NozzleForm(request.POST)
        if form.is_valid():
            nozzle.owner = request.user
            nozzle.bait = form.cleaned_data['bait']
            nozzle.nozzle_manufacturer = form.cleaned_data['nozzle_manufacturer']
            nozzle.nozzle_name = form.cleaned_data['nozzle_name']
            nozzle.nozzle_diameter = form.cleaned_data['nozzle_diameter']
            nozzle.nozzle_type = form.cleaned_data['nozzle_type']
            nozzle.save()
        return redirect('fishing:nozzle')
    else:
        form = NozzleForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def nozzle_details(request, nozzle_id):
    num_visits = visits(request)
    nozzle = get_object_or_404(Nozzle, pk=nozzle_id)
    if nozzle.owner == request.user or request.user.is_staff:
        return render(request,
                      template_details_path,
                      {'nozzle': nozzle,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:nozzle')


@login_required
def nozzle_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        nozzle_list = Nozzle.objects.all()
    else:
        nozzle_list = Nozzle.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'nozzle_list': nozzle_list,
                   'num_visits': num_visits})


@login_required
def nozzle_remove(request, nozzle_id):
    nozzle = get_object_or_404(Nozzle, pk=nozzle_id)
    if nozzle.owner == request.user:
        nozzle.delete()
    return redirect('fishing:nozzle')


@login_required
def nozzle_renewal(request, nozzle_id):
    num_visits = visits(request)
    nozzle = get_object_or_404(Nozzle, pk=nozzle_id)
    if nozzle.owner == request.user:
        if request.method == "POST":
            form = NozzleForm(request.POST)
            if form.is_valid():
                nozzle.bait = form.cleaned_data['bait']
                nozzle.nozzle_manufacturer = form.cleaned_data['nozzle_manufacturer']
                nozzle.nozzle_name = form.cleaned_data['nozzle_name']
                nozzle.nozzle_diameter = form.cleaned_data['nozzle_diameter']
                nozzle.nozzle_type = form.cleaned_data['nozzle_type']
                nozzle.save()
            return redirect('fishing:nozzle')
        else:
            form = NozzleForm(initial={'bait': nozzle.bait,
                                       'nozzle_manufacturer': nozzle.nozzle_manufacturer,
                                       'nozzle_name': nozzle.nozzle_name,
                                       'nozzle_diameter': nozzle.nozzle_diameter,
                                       'nozzle_type': nozzle.nozzle_type, })
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})


@login_required
def nozzle_state_add(request):
    num_visits = visits(request)
    if request.method == 'POST':
        nozzle_state = NozzleState()
        form = NozzleStateForm(request.POST)
        if form.is_valid():
            nozzle_state.owner = request.user
            nozzle_state.state = form.cleaned_data['state']
            nozzle_state.save()
            return redirect('fishing:nozzle_state')
    else:
        form = NozzleStateForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})


@login_required
def nozzle_state_list(request):
    num_visits = visits(request)
    if request.user.is_staff:
        nozzle_state_list = NozzleState.objects.all()
    else:
        nozzle_state_list = NozzleState.objects.filter(owner=request.user)
    return render(request,
                  template_list_path,
                  {'nozzle_state_list': nozzle_state_list,
                   'num_visits': num_visits})


@login_required
def nozzle_state_remove(request, nozzle_state_id):
    nozzle_state = get_object_or_404(NozzleState, pk=nozzle_state_id)
    if nozzle_state.owner == request.user:
        nozzle_state.delete()
    return redirect('fishing:nozzle_state')


@login_required
def nozzle_state_renewal(request, nozzle_state_id):
    num_visits = visits(request)
    nozzle_state = get_object_or_404(NozzleState, pk=nozzle_state_id)
    if nozzle_state.owner == request.user:
        if request.method == 'POST':
            form = NozzleStateForm(request.POST)
            if form.is_valid():
                nozzle_state.state = form.cleaned_data['state']
                nozzle_state.save()
                return redirect('fishing:nozzle_state')
        else:
            form = NozzleStateForm(
                initial={'state': nozzle_state.state})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:nozzle_state')


@staff_member_required
def overcast_add(request):
    num_visits = visits(request)
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
            template_renewal_add_path,
            {'form': form,
             'overcast': overcast,
             'num_visits': num_visits})


@login_required
def overcast_list(request):
    overcasts_list = Overcast.objects.all()
    num_visits = visits(request)
    return render(request,
                  template_list_path,
                  {'overcasts_list': overcasts_list,
                   'num_visits': num_visits})


@staff_member_required
def overcast_remove(request, overcast_id):
    """
    Удаление облачности
    """
    overcast = get_object_or_404(Overcast, pk=overcast_id)
    overcast.delete()
    return redirect('fishing:overcast')


@staff_member_required
def overcast_renewal(request, overcast_id):
    """
    Редактирование облачности
    """
    num_visits = visits(request)
    overcast = get_object_or_404(Overcast, pk=overcast_id)
    if request.method == 'POST':
        form = OvercastForm(request.POST, instance=overcast)
        if form.is_valid():
            overcast.overcast_name = form.cleaned_data['overcast_name']
            overcast.save()
        return redirect('fishing:overcast')
    else:
        form = OvercastForm(
            initial={'overcast_name': overcast.overcast_name, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'overcast': overcast,
                       'num_visits': num_visits})


@staff_member_required
def pace_add(request):
    num_visits = visits(request)
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
                      template_renewal_add_path,
                      {'form': form,
                       'pace': pace,
                       'num_visits': num_visits})


@login_required
def pace_list(request):
    num_visits = visits(request)
    pace_list = Pace.objects.all()
    return render(request,
                  template_list_path,
                  {'pace_list': pace_list,
                   'num_visits': num_visits})


@staff_member_required
def pace_remove(request, pace_id):
    pace = get_object_or_404(Pace, pk=pace_id)
    pace.delete()
    return redirect('fishing:pace')


@staff_member_required
def pace_renewal(request, pace_id):
    num_visits = visits(request)
    pace = get_object_or_404(Pace, pk=pace_id)
    if request.method == 'POST':
        form = PaceForm(request.POST, instance=pace)
        if form.is_valid():
            pace.pace_interval = form.cleaned_data['pace_interval']
            pace.save()
        return redirect('fishing:pace')
    else:
        form = PaceForm(initial={'pace_interval': pace.pace_interval, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'pace': pace,
                       'num_visits': num_visits})


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
                      template_renewal_add_path,
                      {'form': form,
                       'place': place,
                       'district': district_id,
                       'water': water_id,
                       'num_visits': num_visits})


@login_required
def place_detail(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if request.user.is_staff or place.owner == request.user:
        num_visits = visits(request)
        return render(request,
                      template_details_path,
                      {'place': place,
                       'district_id': district_id,
                       'water_id': water_id,
                       'num_visits': num_visits})
    else:
        return redirect('fishing:place', district_id, water_id)


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
    return render(request,
                  template_list_path,
                  {'place_list': place_list,
                   'district': district,
                   'water': water,
                   'num_visits': num_visits})


@login_required
def place_remove(request, district_id, water_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if place.owner == request.user:
        place.delete()
    return redirect('fishing:place', district_id, water_id)


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
                          template_renewal_add_path,
                          {'form': form,
                           'place': place,
                           'district': district_id,
                           'water': water_id,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:place', district_id, water_id)


@staff_member_required
def priming_add(request):
    """
    Добавление вида грунта
    """
    num_visits = visits(request)
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
            template_renewal_add_path,
            {'form': form,
             'priming': priming,
             'num_visits': num_visits})


@login_required
def priming_list(request):
    """
    Список видов грунта
    """
    primings_list = Priming.objects.all()
    num_visits = visits(request)
    return render(request,
                  template_list_path,
                  {'primings_list': primings_list,
                   'num_visits': num_visits})


@staff_member_required
def priming_remove(request, priming_id):
    """
    Удаление грунта
    """
    priming = get_object_or_404(Priming, pk=priming_id)
    priming.delete()
    return redirect('fishing:primings')


@staff_member_required
def priming_renewal(request, priming_id):
    """
    Редактирование грунта
    """
    num_visits = visits(request)
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
        return render(request, template_renewal_add_path,
                      {'form': form,
                       'priming': priming,
                       'num_visits': num_visits})


@staff_member_required
def water_add(request, district_id):
    num_visits = visits(request)
    water = Water()
    if request.method == 'POST':
        form = WaterForm(request.POST)
        if form.is_valid():
            water.water_name = form.cleaned_data['water_name']
            district = get_object_or_404(District, pk=district_id)
            water.district = district
            water.save()
        return redirect('fishing:water', district_id)
    else:
        form = WaterForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'water': water,
                       'district': district_id,
                       'num_visits': num_visits})


@login_required
def water_list(request, district_id):
    num_visits = visits(request)
    district_name = get_object_or_404(District, pk=district_id)
    water_list = Water.objects.filter(
        district=district_name)
    return render(request,
                  template_list_path,
                  {'water_list': water_list,
                   'district': district_name,
                   'num_visits': num_visits})


@staff_member_required
def water_remove(request, district_id, water_id):
    water = get_object_or_404(Water, pk=water_id)
    water.delete()
    return redirect('fishing:water', district_id)


@staff_member_required
def water_renewal(request, district_id, water_id):
    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    if request.method == 'POST':
        form = WaterForm(request.POST)
        if form.is_valid():
            water.water_name = form.cleaned_data['water_name']
            district = get_object_or_404(District, pk=district_id)
            water.district = district
            water.save()
        return redirect('fishing:water', district_id)
    else:
        form = WaterForm(
            initial={'district': water.district,
                     'water_name': water.water_name, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'water': water,
                       'district': district_id,
                       'num_visits': num_visits})


@login_required
def weather_add(request, district_id, water_id, place_id):
    num_visits = visits(request)
    weather = Weather()
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            place = Place.objects.filter(id=place_id)
            weather.place = place[0]
            weather.date = form.cleaned_data['date']
            overcast_select = form.cleaned_data['overcast']
            overcast = Overcast.objects.filter(overcast_name=overcast_select)
            weather.overcast = overcast[0]
            weather_phenomena_select = form.cleaned_data['weather_phenomena']
            weather_phenomena = WeatherPhenomena.objects.filter(
                weather_phenomena_name=weather_phenomena_select)
            weather.weather_phenomena = weather_phenomena[0]
            weather.weather_temperature = form.cleaned_data['weather_temperature']
            weather.pressure = form.cleaned_data['pressure']
            weather.direction_wind = form.cleaned_data['direction_wind']
            weather.wind_speed = form.cleaned_data['wind_speed']
            weather.lunar_day = form.cleaned_data['lunar_day']
            weather.save()
        return redirect('fishing:weather', district_id, water_id, place_id)
    else:
        form = WeatherForm()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'weather': weather,
                       'district': district_id,
                       'water': water_id,
                       'place': place_id,
                       'num_visits': num_visits})


@login_required
def weather_details(request, district_id, water_id, place_id, weather_id):
    weather = get_object_or_404(Weather, pk=weather_id)
    num_visits = visits(request)
    return render(request,
                  template_details_path,
                  {'weather': weather,
                   'place_id': place_id,
                   'district_id': district_id,
                   'water_id': water_id,
                   'num_visits': num_visits})


@login_required
def weather_list(request, district_id, water_id, place_id):
    num_visits = visits(request)
    place = get_object_or_404(Place, pk=place_id)
    weather_list = Weather.objects.filter(
        place=place)
    return render(request,
                  template_list_path,
                  {'weather_list': weather_list,
                   'district': district_id,
                   'water': water_id,
                   'place': place_id,
                   'num_visits': num_visits})


@login_required
def weather_remove(request, district_id, water_id, place_id, weather_id):
    weather = get_object_or_404(Weather, pk=weather_id)
    weather.delete()
    return redirect('fishing:weather', district_id, water_id, place_id)


@login_required
def weather_renewal(request, district_id, water_id, place_id, weather_id):
    num_visits = visits(request)
    weather = get_object_or_404(Weather, pk=weather_id)
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            weather.date = form.cleaned_data['date']
            overcast_select = form.cleaned_data['overcast']
            overcast = Overcast.objects.filter(overcast_name=overcast_select)
            weather.overcast = overcast[0]
            weather_phenomena_select = form.cleaned_data['weather_phenomena']
            weather_phenomena = WeatherPhenomena.objects.filter(
                weather_phenomena_name=weather_phenomena_select)
            weather.weather_phenomena = weather_phenomena[0]
            weather.weather_temperature = form.cleaned_data['weather_temperature']
            weather.pressure = form.cleaned_data['pressure']
            weather.direction_wind = form.cleaned_data['direction_wind']
            weather.wind_speed = form.cleaned_data['wind_speed']
            weather.lunar_day = form.cleaned_data['lunar_day']
            weather.save()
        return redirect('fishing:weather', district_id, water_id, place_id)
    else:
        form = WeatherForm(
            initial={'date': weather.date,
                     'overcast': weather.overcast,
                     'weather_phenomena': weather.weather_phenomena,
                     'weather_temperature': weather.weather_temperature,
                     'pressure': weather.pressure,
                     'direction_wind': weather.direction_wind,
                     'wind_speed': weather.wind_speed,
                     'lunar_day': weather.lunar_day, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'weather': weather,
                       'district': district_id,
                       'water': water_id,
                       'place': place_id,
                       'num_visits': num_visits})


@staff_member_required
def weather_phenomenas_add(request):
    num_visits = visits(request)
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
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'weather_penomena': weather_phenomena,
                       'num_visits': num_visits})


@login_required
def weather_phenomenas_list(request):
    num_visits = visits(request)
    weather_phenomena_list = WeatherPhenomena.objects.all()
    return render(request, template_list_path,
                  {'weather_phenomena_list': weather_phenomena_list,
                   'num_visits': num_visits})


@staff_member_required
def weather_phenomenas_remove(request, phenomena_id):
    """
    Удаление явления
    """
    weatherphenomena = get_object_or_404(WeatherPhenomena, pk=phenomena_id)
    weatherphenomena.delete()
    return redirect('fishing:weatherphenomena')


@staff_member_required
def weather_phenomenas_renewal(request, phenomena_id):
    """
    Редактирование погодного явления
    """
    num_visits = visits(request, phenomena_id)
    weather_phenomena = get_object_or_404(WeatherPhenomena, pk=phenomena_id)
    if request.method == 'POST':
        form = WeatherPhenomenaForm(
            request.POST, instance=weather_phenomena)
        if form.is_valid():
            weather_phenomena.weather_phenomena_name = form.cleaned_data[
                'weather_phenomena_name']
            weather_phenomena.save()
        return redirect('fishing:weatherphenomena')
    else:
        form = WeatherPhenomenaForm(
            initial={'weather_phenomena_name': weather_phenomena.weather_phenomena_name, })
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'phenomena': weather_phenomena,
                       'num_visits': num_visits})

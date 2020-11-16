from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from .models import Fishing
from .models import Fish
from .models import Weather
from .models import Overcast
from .models import Conditions
from .models import FeedCapacity
from .models import Pace
from .models import District
from .models import Water
from .models import Place
from .models import FishingPoint
from .models import BottomMap
from .models import Point
from .models import Priming
from .models import Tackle
from .models import Montage
from .models import Trough
from .models import FishingTrough
from .models import Nozzle
from .models import NozzleState
from .models import NozzleType
from .models import NozzleBase
from .models import Lure
from .models import LureBase
from .models import LureMix
from .models import AromaBase
from .models import Aroma
from .models import Crochet
from .models import Leash
from .models import FishingLeash
from .models import FishingCrochet
from .models import Fishing
from .models import FishingResult
from .models import FishTrophy
from .models import FishingTackle
from .models import PlaceFishing
from .models import FishingMontage
from .models import FishingNozzle
from .models import FishingPace
from .models import FishingWeather
from .models import FishingLure
from .forms import FishForm
from .forms import WeatherForm
from .forms import OvercastForm
from .forms import ConditionsForm
from .forms import FeedCapacityForm
from .forms import PaceForm
from .forms import DistrictForm
from .forms import WaterForm
from .forms import PlaceForm
from .forms import FishingPointForm
from .forms import BottomMapForm
from .forms import PointForm
from .forms import PrimingForm
from .forms import TackleForm
from .forms import MontageForm
from .forms import TroughForm
from .forms import NozzleForm
from .forms import NozzleStateForm
from .forms import NozzleTypeForm
from .forms import NozzleBaseForm
from .forms import BaitBaseForm
from .forms import LureForm
from .forms import LureBaseForm
from .forms import LureMixForm
from .forms import AromaBaseForm
from .forms import AromaForm
from .forms import CrochetForm
from .forms import LeashForm
from .forms import FishingForm
from .forms import FishingResultForm
from .forms import FishTrophyForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

# Переменные
template_renewal_add_path = 'fishing/renewal_add.html'
template_renewal_add_fishing_path = 'fishing/fishing_add.html'
template_renewal_add_class_path = 'fishing/edit.html'
template_list_path = 'fishing/list.html'
template_details_path = 'fishing/details.html'
template_select_path = 'fishing/select.html'

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


class AromaBaseAdd(View):
    """
    Добавление аромы
    """
    template = 'fishing/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = AromaBaseForm(request.POST)
        aroma_base = AromaBase()
        if form.is_valid():
            aroma_base = form.save(commit=False)
            aroma_base.owner = request.user
            if aroma_base.unique():
                aroma_base.first_upper()
                aroma_base.save()
                return redirect('fishing:aroma_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая арома уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = AromaBaseForm()
        return render(request,
                      self.template,
                      {'form': form})


class AromaBaseList(View):
    """
    Возвращает список аром
    """

    template = 'fishing/aromabase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            aroma_base_list = AromaBase.objects.all()
        else:
            aroma_base_list = AromaBase.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'aroma_base_list': aroma_base_list})


class AromaBaseDelete(View):
    """
    Удаление аромы
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        aroma = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma.owner == request.user:
            aroma.delete()
        return redirect('fishing:aroma_base')


class AromaBaseEdit(View):
    """
    Изменение аромы
    """
    template = 'fishing/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma_base.owner == request.user:
            form = AromaBaseForm(request.POST, instance=aroma_base)
            if form.is_valid():
                aroma_base = form.save(commit=False)
                aroma_base.owner = request.user
                if aroma_base.unique():
                    aroma_base.first_upper()
                    aroma_base.save()
                    return redirect('fishing:aroma_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'aroma_base': aroma_base,
                                'errors': 'Такая арома уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'aroma_base': aroma_base})

    def get(self, request, *args, **kwargs):
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma_base.owner == request.user:
            form = AromaBaseForm(instance=aroma_base)
            return render(request,
                        self.template,
                        {'form': form,
                        'aroma_base': aroma_base})
        return redirect('fishing:aroma_base')


class AromaInLureMixDelete(View):
    model = Aroma

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaInLureMixDelete, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        aroma = get_object_or_404(self.model, pk=kwargs['aroma_id'])
        if aroma.owner == request.user:
            aroma.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class AromaInLureMixSelect(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaInLureMixSelect, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        aroma_base_list = AromaBase.objects.filter(owner=request.user)
        return render(request,
                      template_select_path,
                      {'aroma_base_list': aroma_base_list,
                       'fishing_id': kwargs['fishing_id'],
                       'lure_mix_id': kwargs['lure_mix_id'],
                       'num_visits': num_visits})


class AromaInLureMixViews(View):
    model = Aroma
    form = AromaForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaInLureMixViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        form = self.form()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            aroma_base = get_object_or_404(
                AromaBase, pk=kwargs['aroma_base_id'])
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.lure_mix = lure_mix
            entry.aroma_base = aroma_base
            entry.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


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


class CrochetAdd(View):
    """
    Добавление крючка
    """
    template = 'fishing/crochet/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrochetAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CrochetForm(request.POST)
        crochet = Crochet()
        if form.is_valid():
            crochet = form.save(commit=False)
            crochet.owner = request.user
            if crochet.unique():
                crochet.first_upper()
                crochet.save()
                return redirect('fishing:crochet')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой крючок уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = CrochetForm()
        return render(request,
                      self.template,
                      {'form': form})


class CrochetList(View):
    """
    Возвращает список крючков
    """

    template = 'fishing/crochet/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrochetList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            crochet_list = Crochet.objects.all()
        else:
            crochet_list = Crochet.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'crochet_list': crochet_list})


class CrochetDelete(View):
    """
    Удаление крючка
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrochetDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if crochet.owner == request.user:
            crochet.delete()
        return redirect('fishing:crochet')


class CrochetEdit(View):
    """
    Изменение крючка
    """
    template = 'fishing/crochet/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CrochetEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if crochet.owner == request.user:
            form = CrochetForm(request.POST, instance=crochet)
            if form.is_valid():
                crochet = form.save(commit=False)
                crochet.owner = request.user
                if crochet.unique():
                    crochet.first_upper()
                    crochet.save()
                    return redirect('fishing:crochet')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'crochet': crochet,
                                'errors': 'Такой крючок уже добавлен'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'crochet': crochet})

    def get(self, request, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if crochet.owner == request.user:
            form = CrochetForm(instance=crochet)
            return render(request,
                        self.template,
                        {'form': form,
                        'crochet': crochet})
        return redirect('fishing:crochet')


@staff_member_required
def district_add(request):
    num_visits = visits(request)
    district = District()
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district = form.save(commit=False)
            district.save()
        return redirect('fishing:water', district.id)
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
        form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            district = form.save(commit=False)
            district.save()
        return redirect('fishing:districts')
    else:
        form = DistrictForm(instance=district)
        return render(request, template_renewal_add_path,
                      {'form': form,
                       'district': district,
                       'num_visits': num_visits})


@login_required
def fish_trophy_add(request, fishing_id):
    num_visits = visits(request)
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    if fishing.owner == request.user:
        if request.method == 'POST':
            fish_trophy = FishTrophy()
            form = FishTrophyForm(request.POST)
            if form.is_valid():
                fish_trophy = form.save(commit=False)
                fish_trophy.owner = request.user
                fish_trophy.fishing = fishing
                fish_trophy.save()
            return redirect('fishing:fishing_details', fishing_id)
        else:
            form = FishTrophyForm()
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fish_trophy_remove(request, fishing_id, fish_trophy_id):
    fish_trophy = get_object_or_404(FishTrophy, pk=fish_trophy_id)
    if fish_trophy.owner == request.user:
        fish_trophy.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fish_trophy_renewal(request, fishing_id, fish_trophy_id):
    num_visits = visits(request)
    fish_trophy = get_object_or_404(FishTrophy, pk=fish_trophy_id)
    if fish_trophy.owner == request.user:
        if request.method == 'POST':
            form = FishTrophyForm(request.POST, instance=fish_trophy)
            if form.is_valid():
                fish_trophy = form.save(commit=False)
                fish_trophy.owner = request.user
                fishing = get_object_or_404(Fishing, pk=fishing_id)
                fish_trophy.fishing = fishing
                fish_trophy.save()
            return redirect('fishing:fishing_details', fishing_id)
        else:
            form = FishTrophyForm(instance=fish_trophy)
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    return redirect('fishing:fishing_details', fishing_id)


class FishingViews(View):
    model = Fishing
    form = FishingForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        form = self.form()
        return render(request,
                      template_renewal_add_fishing_path,
                      {'form': form,
                       'renewal_add_model': "Добавление рыбалки",
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            entry.date = form.cleaned_data['date']
            entry.time = form.cleaned_data['time']
            entry.owner = request.user
            entry.set_planned()
            print (entry.planned)
            entry.save()
        else:
            print(form.errors)
        return redirect('fishing:fishing_details', entry.id)


@login_required
def fishing_details(request, fishing_id):
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
def fishing_remove(request, fishing_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    if fishing.owner == request.user:
        fishing.delete()
    return redirect('fishing:fishing')


@login_required
def fishing_renewal(request, fishing_id):
    """
    Редактирование рыбалки
    """
    num_visits = visits(request)
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    if fishing.owner == request.user:
        if request.method == 'POST':
            form = FishingForm(request.POST)
            if form.is_valid():
                fishing.date = form.cleaned_data['date']
                fishing.time = form.cleaned_data['time']
                fishing.set_planned()
                fishing.save()
            else:
                form = FishingForm(request.POST)
                return render(request,
                        template_renewal_add_fishing_path,
                        {'form': form,
                        'num_visits': num_visits})
            return redirect('fishing:fishing_details', fishing.id)
        else:
            form = FishingForm(initial={'date': fishing.date,
                                        'time': fishing.time})
            return render(request,
                          template_renewal_add_fishing_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing')


class FishingCrochetDelete(View):
    model = FishingCrochet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingCrochetDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fishing_crochet = get_object_or_404(
            self.model, pk=kwargs['fishing_crochet_id'])
        if fishing_crochet.owner == request.user:
            fishing_crochet.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingCrochetViews(View):
    model = FishingCrochet

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingCrochetViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        crochet_list = Crochet.objects.filter(owner=request.user)
        return render(request,
                      template_select_path,
                      {'crochet_list': crochet_list,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_tackle_id': kwargs['fishing_tackle_id'],
                       'fishing_crochet_id': kwargs['fishing_crochet_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if kwargs['fishing_crochet_id'] != 0:
            fishing_crochet = get_object_or_404(
                self.model, pk=kwargs['fishing_crochet_id'])
            if fishing_crochet.owner == request.user:
                fishing_crochet.crochet = crochet
                fishing_crochet.save()
        else:
            fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
            if fishing_tackle.owner == request.user:
                fishing_crochet = self.model()
                fishing_crochet.owner = request.user
                fishing_crochet.fishing_tackle = fishing_tackle
                fishing_crochet.crochet = crochet
                fishing_crochet.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


@login_required
def fishing_leash_add(request, fishing_id, fishing_tackle_id, leash_id, fishing_leash_id):
    leash = get_object_or_404(Leash, pk=leash_id)
    if fishing_leash_id != 0:
        fishing_leash = get_object_or_404(FishingLeash, pk=fishing_leash_id)
        fishing_leash.leash = leash
        fishing_leash.save()
    else:
        fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
        fishing_leash = FishingLeash()
        fishing_leash.owner = request.user
        fishing_leash.fishing_tackle = fishing_tackle
        fishing_leash.leash = leash
        fishing_leash.save()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_leash_remove(request, fishing_id, fishing_leash_id):
    fishing_leash = get_object_or_404(FishingLeash, pk=fishing_leash_id)
    if fishing_leash.owner == request.user:
        fishing_leash.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_leash_select(request, fishing_id, fishing_tackle_id, fishing_leash_id):
    num_visits = visits(request)
    leash_list = Leash.objects.filter(owner=request.user)
    return render(request,
                  template_select_path,
                  {'leash_list': leash_list,
                   'fishing_id': fishing_id,
                   'fishing_tackle_id':fishing_tackle_id,
                   'fishing_leash_id': fishing_leash_id,
                   'num_visits': num_visits})


@login_required
def fishing_montage_add(request, fishing_id, fishing_tackle_id, montage_id, fishing_montage_id):
    fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
    montage = get_object_or_404(Montage, pk=montage_id)
    if fishing_montage_id != 0:
        fishing_montage = get_object_or_404(
            FishingMontage, pk=fishing_montage_id)
        fishing_montage.montage = montage
        fishing_montage.save()
    else:
        fishing_montage = FishingMontage()
        fishing_montage.owner = request.user
        fishing_montage.fishing_tackle = fishing_tackle
        fishing_montage.montage = montage
        fishing_montage.save()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_montage_remove(request, fishing_id, fishing_montage_id):
    fishing_montage = get_object_or_404(FishingMontage, pk=fishing_montage_id)
    if fishing_montage.owner == request.user:
        fishing_montage.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_montage_select(request, fishing_id, fishing_tackle_id, fishing_montage_id):
    num_visits = visits(request)
    montage_list = Montage.objects.filter(owner=request.user)
    return render(request,
                  template_select_path,
                  {'montage_list': montage_list,
                   'fishing_id': fishing_id,
                   'fishing_tackle_id': fishing_tackle_id,
                   'fishing_montage_id': fishing_montage_id,
                   'num_visits': num_visits})


class FishingNozzleDelete(View):
    model = FishingNozzle

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingNozzleDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fishing_nozzle = get_object_or_404(
            self.model, pk=kwargs['fishing_nozzle_id'])
        if fishing_nozzle.owner == request.user:
            fishing_nozzle.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingNozzleViews(View):
    model_base = NozzleBase
    model = FishingNozzle

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingNozzleViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        nozzle_list = self.model_base.objects.filter(owner=request.user)
        return render(request,
                      template_select_path,
                      {'nozzle_list': nozzle_list,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_tackle_id': kwargs['fishing_tackle_id'],
                       'fishing_nozzle_id': kwargs['fishing_nozzle_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        nozzle = get_object_or_404(self.model_base, pk=kwargs['nozzle_id'])
        if kwargs['fishing_nozzle_id'] != 0:
            fishing_nozzle = get_object_or_404(self.model, pk=kwargs['fishing_nozzle_id'])
            if fishing_nozzle.owner == request.user:
                fishing_nozzle.nozzle_base = nozzle
                fishing_nozzle.save()
        else:
            fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
            if fishing_tackle.owner == request.user:
                fishing_nozzle = self.model()
                fishing_nozzle.owner = request.user
                fishing_nozzle.fishing_tackle = fishing_tackle
                fishing_nozzle.nozzle_base = nozzle
                fishing_nozzle.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingPaceDelete(View):
    model = FishingPace

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPaceDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fishing_pace = get_object_or_404(
            self.model, pk=kwargs['fishing_pace_id'])
        if fishing_pace.owner == request.user:
            fishing_pace.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingPaceViews(View):
    model_base = Pace
    model = FishingPace

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPaceViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        pace_list = self.model_base.objects.all()
        return render(request,
                      template_select_path,
                      {'pace_list': pace_list,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_tackle_id': kwargs['fishing_tackle_id'],
                       'fishing_pace_id': kwargs['fishing_pace_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        pace = get_object_or_404(self.model_base, pk=kwargs['pace_id'])
        if kwargs['fishing_pace_id'] != 0:
            fishing_pace = get_object_or_404(
                self.model, pk=kwargs['fishing_pace_id'])
            if fishing_pace.owner == request.user:
                fishing_pace.pace = pace
                fishing_pace.save()
        else:
            fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
            if fishing_tackle.owner == request.user:
                fishing_pace = self.model()
                fishing_pace.owner = request.user
                fishing_pace.fishing_tackle = fishing_tackle
                fishing_pace.pace = pace
                fishing_pace.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


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
def fishing_result_add(request, fishing_id):
    num_visits = visits(request)
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    if fishing.owner == request.user:
        if request.method == 'POST':
            fishing_result = FishingResult()
            form = FishingResultForm(request.POST)
            if form.is_valid():
                fishing_result = form.save(commit=False)
                fishing_result.owner = request.user
                fishing_result.fishing = fishing
                fishing_result.save()
            return redirect('fishing:fishing_details', fishing_id)
        else:
            form = FishingResultForm()
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_result_remove(request, fishing_id, fishing_result_id):
    fishing_result = get_object_or_404(FishingResult, pk=fishing_result_id)
    if fishing_result.owner == request.user:
        fishing_result.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_result_renewal(request, fishing_id, fishing_result_id):
    num_visits = visits(request)
    fishing_result = get_object_or_404(FishingResult, pk=fishing_result_id)
    if fishing_result.owner == request.user:
        if request.method == 'POST':
            form = FishingResultForm(request.POST, instance=fishing_result)
            if form.is_valid():
                fishing_result = form.save(commit=False)
                fishing_result.owner = request.user
                fishing = get_object_or_404(Fishing, pk=fishing_id)
                fishing_result.fishing = fishing
                fishing_result.save()
            return redirect('fishing:fishing_details', fishing_id)
        else:
            form = FishingResultForm(instance=fishing_result)
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_tackle_add(request, fishing_id, tackle_id, fishing_tackle_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    tackle = get_object_or_404(Tackle, pk=tackle_id)
    if fishing_tackle_id != 0:
        fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
        fishing_tackle.fishing = fishing
        fishing_tackle.tackle = tackle
        fishing_tackle.save()
    else:
        fishing_tackle = FishingTackle()
        fishing_tackle.owner = request.user
        fishing_tackle.fishing = fishing
        fishing_tackle.tackle = tackle
        fishing_tackle.save()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_tackle_remove(request, fishing_id, fishing_tackle_id):
    fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
    if fishing_tackle.owner == request.user:
        fishing_tackle.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_tackle_select(request, fishing_id, fishing_tackle_id):
    num_visits = visits(request)
    tackle_list = Tackle.objects.filter(owner=request.user)
    return render(request,
                  template_select_path,
                  {'tackle_list': tackle_list,
                   'fishing_id': fishing_id,
                   'fishing_tackle_id': fishing_tackle_id,
                   'num_visits': num_visits})


@login_required
def fishing_trough_add(request, fishing_id, fishing_tackle_id, trough_id, fishing_trough_id):
    fishing_tackle = get_object_or_404(FishingTackle, pk=fishing_tackle_id)
    trough = get_object_or_404(Trough, pk=trough_id)
    if fishing_trough_id != 0:
        fishing_trough = get_object_or_404(FishingTrough, pk=fishing_trough_id)
        fishing_trough.trough = trough
        fishing_trough.save()
    else:
        fishing_trough = FishingTrough()
        fishing_trough.owner = request.user
        fishing_trough.fishing_tackle = fishing_tackle
        fishing_trough.trough = trough
        fishing_trough.save()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_trough_remove(request, fishing_id, fishing_trough_id):
    fishing_trough = get_object_or_404(FishingTrough, pk=fishing_trough_id)
    if fishing_trough.owner == request.user:
        fishing_trough.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def fishing_trough_select(request, fishing_id, fishing_tackle_id, fishing_trough_id):
    num_visits = visits(request)
    trough_list = Trough.objects.filter(owner=request.user)
    return render(request,
                  template_select_path,
                  {'trough_list': trough_list,
                   'fishing_id': fishing_id,
                   'fishing_tackle_id':fishing_tackle_id,
                   'fishing_trough_id': fishing_trough_id,
                   'num_visits': num_visits, })


class FishingLureDelete(View):
    model = FishingLure

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLureDelete, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        fishing_lure = get_object_or_404(
            self.model, pk=kwargs['fishing_lure_id'])
        if fishing_lure.owner == request.user:
            fishing_lure.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingLureViews(View):
    model_base = LureMix
    model = FishingLure

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLureViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        lure_mix_list = self.model_base.objects.all()
        return render(request,
                      template_select_path,
                      {'lure_mix_list': lure_mix_list,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_lure_id': kwargs['fishing_lure_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(self.model_base, pk=kwargs['lure_mix_id'])
        if kwargs['fishing_lure_id'] != 0:
            fishing_lure = get_object_or_404(
                self.model, pk=kwargs['fishing_lure_id'])
            if fishing_lure.owner == request.user:
                fishing_lure.lure_mix = lure_mix
                fishing_lure.save()
        else:
            fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
            if fishing.owner == request.user:
                fishing_lure = self.model()
                fishing_lure.owner = request.user
                fishing_lure.fishing = fishing
                fishing_lure.lure_mix = lure_mix
                fishing_lure.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingWeatherDelete(View):
    model = FishingWeather

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingWeatherDelete, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        fishing_weather = get_object_or_404(
            self.model, pk=kwargs['fishing_weather_id'])
        if fishing_weather.owner == request.user:
            fishing_weather.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingWeatherViews(View):
    model_base = Weather
    model = FishingWeather

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingWeatherViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        weather_list = self.model_base.objects.all()
        return render(request,
                      template_select_path,
                      {'weather_list': weather_list,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_weather_id': kwargs['fishing_weather_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        weather = get_object_or_404(self.model_base, pk=kwargs['weather_id'])
        if kwargs['fishing_weather_id'] != 0:
            fishing_weather = get_object_or_404(
                self.model, pk=kwargs['fishing_weather_id'])
            if fishing_weather.owner == request.user:
                fishing_weather.weather = weather
                fishing_weather.save()
        else:
            fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
            if fishing.owner == request.user:
                fishing_weather = self.model()
                fishing_weather.owner = request.user
                fishing_weather.fishing = fishing
                fishing_weather.weather = weather
                fishing_weather.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class LeashAdd(View):
    """
    Добавление поводка
    """
    template = 'fishing/leash/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LeashForm(request.POST)
        leash = Leash()
        if form.is_valid():
            leash = form.save(commit=False)
            leash.owner = request.user
            if leash.unique():
                leash.first_upper()
                leash.save()
                return redirect('fishing:leash')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой поводок уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = LeashForm()
        return render(request,
                      self.template,
                      {'form': form})


class LeashList(View):
    """
    Возвращает список поводков
    """

    template = 'fishing/leash/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            leash_list = Leash.objects.all()
        else:
            leash_list = Leash.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'leash_list': leash_list})


class LeashDelete(View):
    """
    Удаление поводка
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            leash.delete()
        return redirect('fishing:leash')


class LeashEdit(View):
    """
    Изменение поводка
    """
    template = 'fishing/leash/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            form = LeashForm(request.POST, instance=leash)
            if form.is_valid():
                leash = form.save(commit=False)
                leash.owner = request.user
                if leash.unique():
                    leash.first_upper()
                    leash.save()
                    return redirect('fishing:leash')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'leash': leash,
                                'errors': 'Такой поводок уже добавлен'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'leash': leash})
        else:
            return redirect('fishing:leash')

    def get(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            form = LeashForm(instance=leash)
            return render(request,
                        self.template,
                        {'form': form,
                        'leash': leash})
        return redirect('fishing:leash')


class LureBaseAdd(View):
    """
    Добавление прикорма
    """
    template = 'fishing/lurebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureBaseAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LureBaseForm(request.POST)
        lure_base = LureBase()
        if form.is_valid():
            lure_base = form.save(commit=False)
            lure_base.owner = request.user
            if lure_base.unique():
                lure_base.first_upper()
                lure_base.save()
                return redirect('fishing:lure_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой прикорм уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = LureBaseForm()
        return render(request,
                      self.template,
                      {'form': form})


class LureBaseList(View):
    """
    Возвращает список прикормов
    """

    template = 'fishing/lurebase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureBaseList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            lure_base_list = LureBase.objects.all()
        else:
            lure_base_list = LureBase.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'lure_base_list': lure_base_list})


class LureBaseDelete(View):
    """
    Удаление прикорма
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureBaseDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure.owner == request.user:
            lure.delete()
        return redirect('fishing:lure_base')


class LureBaseEdit(View):
    """
    Изменение прикорма
    """
    template = 'fishing/lurebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureBaseEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_base.owner == request.user:
            form = LureBaseForm(request.POST, instance=lure_base)
            if form.is_valid():
                lure_base = form.save(commit=False)
                lure_base.owner = request.user
                if lure_base.unique():
                    lure_base.first_upper()
                    lure_base.save()
                    return redirect('fishing:lure_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'lure_base': lure_base,
                                'errors': 'Такой прикорм уже добавлен'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'lure_base': lure_base})

    def get(self, request, *args, **kwargs):
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_base.owner == request.user:
            form = LureBaseForm(instance=lure_base)
            return render(request,
                        self.template,
                        {'form': form,
                        'lure_base': lure_base})
        return redirect('fishing:lure_base')


class LureInLureMixDelete(View):
    model = Lure

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureInLureMixDelete, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        lure = get_object_or_404(self.model, pk=kwargs['lure_id'])
        if lure.owner == request.user:
            lure.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class LureInLureMixSelect(View):
    model = LureBase

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureInLureMixSelect, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        lure_base_list = LureBase.objects.filter(owner=request.user)
        return render(request,
                      template_select_path,
                      {'lure_base_list': lure_base_list,
                       'fishing_id': kwargs['fishing_id'],
                       'lure_mix_id': kwargs['lure_mix_id'],
                       'num_visits': num_visits})


class LureInLureMixViews(View):
    model = Lure
    form = LureForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureInLureMixViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        form = self.form()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.lure_mix = lure_mix
            entry.lure_base = lure_base
            entry.save()
        else:
            form = self.form(request.POST)
            return render(request,
                      template_renewal_add_path,
                      {'form': form})
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class LureMixNewAddInFishingLure(View):
    model = LureMix
    form = LureMixForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixNewAddInFishingLure, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        form = self.form()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'fishing_id': kwargs['fishing_id'],
                       'fishing_lure_id': kwargs['fishing_lure_id'],
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            if kwargs['fishing_lure_id'] != 0:
                fishing_lure = get_object_or_404(
                    FishingLure, pk=kwargs['fishing_lure_id'])
                fishing_lure = FishingLure()
                fishing_lure.lure_mix = entry
                fishing_lure.save()
            else:
                fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
                fishing_lure = FishingLure()
                fishing_lure.owner = request.user
                fishing_lure.fishing = fishing
                fishing_lure.lure_mix = entry
                fishing_lure.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class MontageAdd(View):
    """
    Добавление монтажа
    """
    template = 'fishing/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = MontageForm(request.POST)
        montage = Montage()
        if form.is_valid():
            montage = form.save(commit=False)
            montage.owner = request.user
            if montage.unique():
                montage.first_upper()
                montage.save()
                return redirect('fishing:montage')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой монтаж уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = MontageForm()
        return render(request,
                      self.template,
                      {'form': form})


class MontageList(View):
    """
    Возвращает монтажей
    """

    template = 'fishing/montage/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            montage_list = Montage.objects.all()
        else:
            montage_list = Montage.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'montage_list': montage_list})


class MontageDelete(View):
    """
    Удаление монтажа
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            montage.delete()
        return redirect('fishing:montage')


class MontageEdit(View):
    """
    Изменение монтажа
    """
    template = 'fishing/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            form = MontageForm(request.POST, instance=montage)
            if form.is_valid():
                montage = form.save(commit=False)
                montage.owner = request.user
                if montage.unique():
                    montage.first_upper()
                    montage.save()
                    return redirect('fishing:montage')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'montage': montage,
                                'errors': 'Такой монтаж уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'montage': montage})
        return redirect('fishing:montage')

    def get(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            form = NozzleBaseForm(instance=montage)
            return render(request,
                        self.template,
                        {'form': form,
                        'montage': montage})
        return redirect('fishing:montage')


class NozzleBaseAdd(View):
    """
    Добавление насадки
    """
    template = 'fishing/nozzlebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleBaseAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = NozzleBaseForm(request.POST)
        nozzle_base = NozzleBase()
        if form.is_valid():
            nozzle_base = form.save(commit=False)
            nozzle_base.owner = request.user
            nozzle_base.bait = False
            if nozzle_base.unique():
                nozzle_base.first_upper()
                nozzle_base.save()
                return redirect('fishing:nozzle_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая насадка уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = NozzleBaseForm()
        return render(request,
                      self.template,
                      {'form': form})


class NozzleBaseList(View):
    """
    Возвращает список наживок/насадок
    """

    template = 'fishing/nozzlebase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleBaseList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            nozzle_base_list = NozzleBase.objects.all()
            nozzle_state_list = NozzleState.objects.all()
        else:
            nozzle_base_list = NozzleBase.objects.filter(owner=request.user)
            nozzle_state_list = NozzleState.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'nozzle_base_list': nozzle_base_list,
                     'nozzle_state_list':nozzle_state_list})


class NozzleBaseDelete(View):
    """
    Удаление наживки/насадки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleBaseDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle.owner == request.user:
            nozzle.delete()
        return redirect('fishing:nozzle_base')


class NozzleBaseEdit(View):
    """
    Изменение насадки
    """
    template = 'fishing/nozzlebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleBaseEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle_base.owner == request.user:
            form = NozzleBaseForm(request.POST, instance=nozzle_base)
            if form.is_valid():
                nozzle_base = form.save(commit=False)
                nozzle_base.owner = request.user
                if nozzle_base.unique():
                    nozzle_base.first_upper()
                    nozzle_base.save()
                    return redirect('fishing:nozzle_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'nozzle_base': nozzle_base,
                                'errors': 'Такая насадка уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'nozle_base': nozzle_base})

    def get(self, request, *args, **kwargs):
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle_base.owner == request.user:
            form = NozzleBaseForm(instance=nozzle_base)
            return render(request,
                        self.template,
                        {'form': form,
                        'nozzle_base': nozzle_base})
        return redirect('fishing:nozzle_base')


class BaitBaseAdd(View):
    """
    Добавление насадки
    """
    template = 'fishing/nozzlebase/bait_edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BaitBaseAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = BaitBaseForm(request.POST)
        nozzle_base = NozzleBase()
        if form.is_valid():
            nozzle_base = form.save(commit=False)
            nozzle_base.owner = request.user
            nozzle_base.bait = True
            if nozzle_base.unique():
                nozzle_base.first_upper()
                nozzle_base.save()
                return redirect('fishing:nozzle_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая наживка уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = BaitBaseForm()
        return render(request,
                      self.template,
                      {'form': form})


class BaitBaseEdit(View):
    """
    Изменение наживки
    """
    template = 'fishing/nozzlebase/bait_edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BaitBaseEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        bait_base = get_object_or_404(NozzleBase, pk=kwargs['bait_base_id'])
        if bait_base.owner == request.user:
            form = BaitBaseForm(request.POST, instance=bait_base)
            if form.is_valid():
                bait_base = form.save(commit=False)
                bait_base.owner = request.user
                if bait_base.unique():
                    bait_base.first_upper()
                    bait_base.save()
                    return redirect('fishing:nozzle_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'bait_base': bait_base,
                                'errors': 'Такая наживка уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'bait_base': bait_base})

    def get(self, request, *args, **kwargs):
        bait_base = get_object_or_404(NozzleBase, pk=kwargs['bait_base_id'])
        if bait_base.owner == request.user:
            form = BaitBaseForm(instance=bait_base)
            return render(request,
                        self.template,
                        {'form': form,
                        'bait_base': bait_base})
        return redirect('fishing:nozzle_base')


class NozzleStateAdd(View):
    """
    Добавление состояния насадки или наживки
    """
    template = 'fishing/nozzlestate/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleStateAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = NozzleStateForm(request.POST)
        nozzle_state = NozzleState()
        if form.is_valid():
            nozzle_state = form.save(commit=False)
            nozzle_state.owner = request.user
            if nozzle_state.unique():
                nozzle_state.first_upper()
                nozzle_state.save()
                return redirect('fishing:nozzle_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такое состояние уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = NozzleStateForm()
        return render(request,
                      self.template,
                      {'form': form})


class NozzleStateEdit(View):
    """
    Изменение состояния насадки или наживки
    """
    template = 'fishing/nozzlestate/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleStateEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == request.user:
            form = NozzleStateForm(request.POST, instance=nozzle_state)
            if form.is_valid():
                nozzle_state = form.save(commit=False)
                nozzle_state.owner = request.user
                if nozzle_state.unique():
                    nozzle_state.first_upper()
                    nozzle_state.save()
                    return redirect('fishing:nozzle_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'nozzle_state': nozzle_state,
                                'errors': 'Такое сосотояние наживки или насадки уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'nozzle_state': nozzle_state})

    def get(self, request, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == request.user:
            form = NozzleStateForm(instance=nozzle_state)
            return render(request,
                        self.template,
                        {'form': form,
                        'nozzle_state': nozzle_state})
        return redirect('fishing:nozzle_base')


class NozzleStateDelete(View):
    """
    Удаление состояния наживки/насадки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleStateDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == request.user:
            nozzle_state.delete()
        return redirect('fishing:nozzle_base')


class NozzleInLureMixDelete(View):
    model = Nozzle

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleInLureMixDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle = get_object_or_404(self.model, pk=kwargs['nozzle_id'])
        if nozzle.owner == request.user:
            nozzle.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class NozzleInLureMixSelect(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleInLureMixSelect, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        nozzle_base_list = NozzleBase.objects.filter(owner=request.user)
        return render(request,
                      template_select_path,
                      {'nozzle_base_list': nozzle_base_list,
                       'fishing_id': kwargs['fishing_id'],
                       'lure_mix_id': kwargs['lure_mix_id'],
                       'num_visits': num_visits})


class NozzleInLureMixViews(View):
    model = Nozzle
    form = NozzleForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NozzleInLureMixViews, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        num_visits = visits(request)
        form = self.form()
        return render(request,
                      template_renewal_add_path,
                      {'form': form,
                       'num_visits': num_visits})

    def post(self, request, *args, **kwargs):
        entry = self.model()
        form = self.form(request.POST)
        if form.is_valid():
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            nozzle_base = get_object_or_404(
                NozzleBase, pk=kwargs['nozzle_base_id'])
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.lure_mix = lure_mix
            entry.nozzle_base = nozzle_base
            entry.save()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


@login_required
def place_add(request, district_id, water_id):
    num_visits = visits(request)
    water = get_object_or_404(Water, pk=water_id)
    place = Place()
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.owner = request.user
            place.water = water
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
            form = PlaceForm(request.POST, instance=place)
            if form.is_valid():
                place = form.save(commit=False)
                place.owner = request.user
                water = get_object_or_404(Water, pk=water_id)
                place.water = water
                place.save()
            return redirect('fishing:place', district_id, water_id)
        else:
            form = PlaceForm(instance=place)
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'place': place,
                           'district': district_id,
                           'water': water_id,
                           'num_visits': num_visits})
    else:
        return redirect('fishing:place', district_id, water_id)


@login_required
def place_fishing_add(request, fishing_id, place_id):
    place = get_object_or_404(Place, pk=place_id)
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    if place.owner == request.user and fishing.owner == request.user:
        try:
            place_fishing = PlaceFishing.objects.get(fishing=fishing)
        except PlaceFishing.DoesNotExist:
            place_fishing = PlaceFishing()
        place_fishing.owner = request.user
        place_fishing.fishing = fishing
        place_fishing.place = place
        place_fishing.save()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def place_fishing_remove(request, fishing_id, place_fishing_id):
    place_fishing = get_object_or_404(PlaceFishing, pk=place_fishing_id)
    if place_fishing.owner == request.user:
        place_fishing.delete()
    return redirect('fishing:fishing_details', fishing_id)


@login_required
def place_fishing_select(request, fishing_id):
    num_visits = visits(request)
    place_list = Place.objects.filter(owner=request.user)
    return render(request,
                  template_select_path,
                  {'place_list': place_list,
                   'fishing_id': fishing_id,
                   'num_visits': num_visits})


class TackleAdd(View):
    """
    Добавление снастей
    """
    template = 'fishing/tackle/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = TackleForm(request.POST)
        if form.is_valid():
            tackle = form.save(commit=False)
            tackle.owner = request.user
            if tackle.unique():
                tackle.first_upper()
                tackle.save()
                return redirect('fishing:tackle')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая снасть уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = TackleForm()
        return render(request,
                      self.template,
                      {'form': form})


class TackleList(View):
    """
    Возвращает список снастей
    """

    template = 'fishing/tackle/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            tackle_list = Tackle.objects.all()
        else:
            tackle_list = Tackle.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'tackle_list': tackle_list})


class TackleDelete(View):
    """
    Удаление снасти
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        if tackle.owner == request.user:
            tackle.delete()
        return redirect('fishing:tackle')


class TackleEdit(View):
    """
    Изменение снасти
    """
    template = 'fishing/tackle/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        if tackle.owner == request.user:
            form = TackleForm(request.POST, instance=tackle)
            if form.is_valid():
                tackle = form.save(commit=False)
                tackle.owner = request.user
                if tackle.unique():
                    tackle.first_upper()
                    tackle.save()
                    return redirect('fishing:tackle')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'tackle': tackle,
                                'errors': 'Такая снасть уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'tackle': tackle})
        return redirect('fishing:tackle')

    def get(self, request, *args, **kwargs):
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        if tackle.owner == request.user:
            form = TackleForm(instance=tackle)
            return render(request,
                        self.template,
                        {'form': form,
                        'tackle': tackle})
        return redirect('fishing:tackle')


class TroughAdd(View):
    """
    Добавление кормушек
    """
    template = 'fishing/trough/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = TroughForm(request.POST)
        trough = Trough()
        if form.is_valid():
            trough = form.save(commit=False)
            trough.owner = request.user
            if trough.unique():
                trough.first_upper()
                trough.save()
                return redirect('fishing:trough')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая кормушка уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = TroughForm()
        return render(request,
                      self.template,
                      {'form': form})


class TroughList(View):
    """
    Возвращает список кормушек
    """

    template = 'fishing/trough/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            trough_list = Trough.objects.all()
        else:
            trough_list = Trough.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'trough_list': trough_list})


class TroughDelete(View):
    """
    Удаление кормушки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            trough.delete()
        return redirect('fishing:trough')


class TroughEdit(View):
    """
    Изменение кормушки
    """
    template = 'fishing/trough/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            form = TroughForm(request.POST, instance=trough)
            if form.is_valid():
                trough = form.save(commit=False)
                trough.owner = request.user
                if trough.unique():
                    trough.first_upper()
                    trough.save()
                    return redirect('fishing:trough')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'trough': trough,
                                'errors': 'Такая кормушка уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'trough': trough})

    def get(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            form = TroughForm(instance=trough)
            return render(request,
                        self.template,
                        {'form': form,
                        'trough': trough})
        return redirect('fishing:trough')


# @login_required
# def water_add(request, district_id):
#     num_visits = visits(request)
#     water = Water()
#     if request.method == 'POST':
#         form = WaterForm(request.POST)
#         if form.is_valid():
#             water = form.save(commit=False)
#             district = get_object_or_404(District, pk=district_id)
#             water.district = district
#             water.save()
#         return redirect('fishing:place', district.id, water.id)
#     else:
#         form = WaterForm()
#         return render(request,
#                       template_renewal_add_path,
#                       {'form': form,
#                        'water': water,
#                        'district': district_id,
#                        'num_visits': num_visits})


# @login_required
# def water_list(request, district_id):
#     num_visits = visits(request)
#     district_name = get_object_or_404(District, pk=district_id)
#     water_list = Water.objects.filter(
#         district=district_name)
#     return render(request,
#                   template_list_path,
#                   {'water_list': water_list,
#                    'district': district_name,
#                    'num_visits': num_visits})


# @staff_member_required
# def water_remove(request, district_id, water_id):
#     water = get_object_or_404(Water, pk=water_id)
#     water.delete()
#     return redirect('fishing:water', district_id)


# @staff_member_required
# def water_renewal(request, district_id, water_id):
#     num_visits = visits(request)
#     water = get_object_or_404(Water, pk=water_id)
#     if request.method == 'POST':
#         form = WaterForm(request.POST, instance=water)
#         if form.is_valid():
#             water = form.save(commit=False)
#             district = get_object_or_404(District, pk=district_id)
#             water.district = district
#             water.save()
#         return redirect('fishing:water', district_id)
#     else:
#         form = WaterForm(instance=water)
#         return render(request,
#                       template_renewal_add_path,
#                       {'form': form,
#                        'water': water,
#                        'district': district_id,
#                        'num_visits': num_visits})


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



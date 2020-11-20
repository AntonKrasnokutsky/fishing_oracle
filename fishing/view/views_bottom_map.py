from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from fishing.models import Point
from fishing.models import BottomMap
from fishing.models import Priming
from fishing.models import Place
from fishing.models import Water
from fishing.forms import BottomMapForm
from fishing.forms import PointForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def bottom_map_add(request, district_id, water_id, place_id):
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
                           'bottom_map': bottom_map})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_details(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if request.user.is_staff or bottom_map.owner == request.user:
        return render(request,
                      template_details_path,
                      {'bottom_map': bottom_map,
                       'place_id': place_id,
                       'district_id': district_id,
                       'water_id': water_id})
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

    water = get_object_or_404(Water, pk=water_id)
    return render(request,
                  template_list_path,
                  {'bottom_map_list': bottom_map_list,
                   'water': water,
                   'place': place})


@login_required
def bottom_map_remove(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if bottom_map.owner == request.user:
        bottom_map.delete()
    return redirect('fishing:bottom_map', water_id, place_id)


@login_required
def bottom_map_renewal(request, district_id, water_id, place_id, bottom_map_id):
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
                           'bottom_map': bottom_map})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_add(request, district_id, water_id, place_id, bottom_map_id):
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
                           'bottom_map': bottom_map_id})
    else:
        return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_details(request, district_id, water_id, place_id, bottom_map_id, point_id):
    point = get_object_or_404(Point, pk=point_id)
    if request.user.is_staff or point.owner == request.user:
        return render(request,
                      template_details_path,
                      {'point': point,
                       'bottom_map': bottom_map_id,
                       'place': place_id,
                       'district': district_id,
                       'water': water_id})
    return redirect('fishing:water', district_id)


@login_required
def bottom_map_point_list(request, district_id, water_id, place_id, bottom_map_id):
    bottom_map = get_object_or_404(BottomMap, pk=bottom_map_id)
    if not request.user.is_staff:
        point_list = Point.objects.filter(
            owner=request.user, bottom_map=bottom_map)
    else:
        point_list = Point.objects.filter(bottom_map=bottom_map)

    water = get_object_or_404(Water, pk=water_id)
    place = get_object_or_404(Place, pk=place_id)
    return render(request,
                  template_list_path,
                  {'point_list': point_list,
                   'water': water,
                   'place': place,
                   'bottom_map': bottom_map})


@login_required
def bottom_map_point_remove(request, water_id, place_id, bottom_map_id, point_id):
    point = get_object_or_404(Point, pk=point_id)
    if point.owner == request.user:
        point.delete()
    return redirect('fishing:point', water_id, place_id, bottom_map_id)


@login_required
def bottom_map_point_renewal(request,water_id, place_id, bottom_map_id, point_id):
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
            return redirect('fishing:point', water_id, place_id, bottom_map_id)
        else:
            form = PointForm(initial={'point_azimuth': point.point_azimuth,
                                      'point_distance': point.point_distance,
                                      'point_depth': point.point_depth,
                                      'priming': point.priming})
            return render(request,
                          template_renewal_add_path,
                          {'form': form,
                           'point': point,
                           'water': water_id,
                           'place': place_id,
                           'bottom_map': bottom_map_id})
    else:
        return redirect('fishing:water')

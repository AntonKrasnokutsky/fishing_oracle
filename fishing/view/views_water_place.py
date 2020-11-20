from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from fishing.models import Water
from fishing.models import Place
from fishing.forms import WaterForm
from fishing.forms import PlaceForm
from fishing.forms import PlaceCoordinatesForm


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class WaterList(View):
    """
    Список водоёмов
    """

    template = 'fishing/water/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WaterList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        water_list = Water.objects.filter(owner=request.user)
        return render(request,
                self.template,
                {'water_list': water_list})


class WaterAdd(View):
    """
    Добавляет водоем
    """
    
    template = 'fishing/water/edit_add.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WaterAdd, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = WaterForm(request.POST)
        if form.is_valid():
            water = form.save(commit=False)
            water.owner = request.user
            if water.unique():
                water.first_upper()
                water.save()
                return redirect('fishing:water')
            else:
                return render(request,
                              self.template,
                              {'erorrs': 'Водоём с таким названием и категорией уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = WaterForm()
        return render(request,
                      self.template,
                      {'form': form})


class WaterDelete(View):
    """
    Удаляет водоём
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WaterDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if water.owner == request.user:
            water.delete()
        return redirect('fishing:water')


class WaterEdit(View):
    """
    Редактирует водоем
    """
    
    template = 'fishing/water/edit_add.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WaterEdit, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        form = WaterForm(request.POST, instance=water)
        if water.owner == request.user:
            if form.is_valid():
                water = form.save(commit=False)
                if water.unique():
                    water.first_upper()
                    water.save()
                    return redirect('fishing:water')
                else:
                    return render(request,
                                  self.template,
                                  {'form': form,
                                   'errors': 'Водоём с таким названием и категорией уже добавлен'})
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'water': water})
        else:
            return redirect('fishing:water')
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if water.owner == request.user:
            form = WaterForm(instance=water)
            return render(request,
                          self.template,
                          {'form': form,
                           "water": water})
        return redirect('fishing:water')


class PlaceList(View):
    """
    Список мест на водоёме
    """
    
    template = 'fishing/place/list.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceList, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        places_list = Place.objects.filter(owner=request.user, water=water)
        return render(request,
                      self.template,
                      {'water': water,
                       'places_list': places_list})


class PlaceAdd(View):
    """
    Добавление места на водоеме
    """
    
    template = 'fishing/place/edit_add.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceAdd, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if water.owner == request.user:
            form = PlaceForm(request.POST)
            if form.is_valid():
                place = form.save(commit=False)
                place.owner = request.user
                place.water = water
                if place.unique():
                    place.first_upper()
                    place.save()
                    return redirect('fishing:places', kwargs['water_id'])
                else:
                    return render(request,
                                  self.template,
                                  {'form': form,
                                   'water': water,
                                   'errors': 'Место с таким названием на этом водоеме уже добавлено'})
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'water': water})
        return redirect('fishing:places', kwargs['water_id'])
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if water.owner == request.user:
            form = PlaceForm()
            return render(request,
                          self.template,
                          {'form': form,
                           'water': water})
        return redirect('fishing:places', kwargs['water_id'])


class PlaceDelete(View):
    """
    Удаление места на водоеме
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if place.owner == water.owner and place.owner == request.user:
            place.delete()
        return redirect('fishing:places', kwargs['water_id'])


class PlaceEdit(View):
    """
    Редактирование места на водоеме
    """
    
    template = 'fishing/place/edit_add.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceEdit, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if water.owner == request.user and water.owner == place.owner:
            form = PlaceForm(request.POST, instance=place)
            if form.is_valid():
                place = form.save(commit=False)
                if place.unique():
                    place.first_upper()
                    place.save()
                    return redirect('fishing:places', kwargs['water_id'])
                else:
                    return render(request,
                                  self.template,
                                  {'form': form,
                                   'place': place,
                                   'water': water,
                                   'errors': 'Место с таким названием на этом водоеме уже добавлено'})
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'place': place,
                               'water': water})
        return redirect('fishing:places', kwargs['water_id'])
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if water.owner == request.user and water.owner == place.owner:
            form = PlaceForm(instance=place)
            return render(request,
                          self.template,
                          {'form': form,
                           'place': place,
                           'water': water})
        return redirect('fishing:places', kwargs['water_id'])


class PlaceCoordinatesAdd(View):
    """
    Добавление координат места на водоеме
    """
    
    template = 'fishing/place/edit_add_coordinates.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceCoordinatesAdd, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if water.owner == request.user and place.owner == water.owner:
            form = PlaceCoordinatesForm(request.POST, instance=place)
            if form.is_valid():
                place = form.save(commit=False)
                if place.unique_coordinates():
                    place.save()
                    return redirect('fishing:places', kwargs['water_id'])
                else:
                    return render(request,
                                  self.template,
                                  {'form': form,
                                   'water': water,
                                   'errors': 'Место с такими координатами уже добавлено'})
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'place': place,
                               'water': water})
        return redirect('fishing:places', kwargs['water_id'])
    
    def get(self, request, *args, **kwargs):
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if water.owner == request.user:
            form = PlaceCoordinatesForm(instance=place)
            return render(request,
                          self.template,
                          {'form': form,
                           'place': place,
                           'water': water})
        return redirect('fishing:places', kwargs['water_id'])

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from fishing.models import Water
from fishing.forms import WaterForm

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


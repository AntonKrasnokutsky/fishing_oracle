from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from fishing.models import Aroma
from fishing.models import AromaBase
from fishing.models import Lure
from fishing.models import LureBase
from fishing.models import LureMix
from fishing.models import Nozzle
from fishing.models import NozzleBase
from fishing.models import NozzleState
from fishing.forms import AromaForm
from fishing.forms import LureForm
from fishing.forms import LureMixForm
from fishing.forms import NozzleForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SelectAromaForMix(View):
    """
    Список прикормов для выбора в прикормочную смесь
    """

    template = 'fishing/luremix/select_aroma.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SelectAromaForMix, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            aroma_base_list = AromaBase.objects.filter(owner=request.user)
            return render(request,
                    self.template,
                    {'lure_mix': lure_mix,
                     'aroma_base_list': aroma_base_list})
        return redirect('fishing:lure_mix')


class AddAromaToMix(View):
    """
    Добавление выбранной аромы в смесь
    """
    template = 'fishing/luremix/edit_add_aroma.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddAromaToMix, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if lure_mix.owner == request.user and lure_mix.owner == aroma_base.owner:
            form = AromaForm(request.POST)
            if form.is_valid():
                aroma = form.save(commit=False)
                aroma.owner = request.user
                aroma.mix = lure_mix
                aroma.base = aroma_base
                aroma.save()
                return redirect('fishing:lure_mix_details', lure_mix.id)
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if lure_mix.owner == request.user and lure_mix.owner == aroma_base.owner:
            form = AromaForm()
            return render(request,
                          self.template,
                          {'form': form,
                           'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')


class DeleteAromaOfMix(View):
    """
    Удаляет аромы из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteAromaOfMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if aroma.owner == request.user:
            aroma.delete()
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            return redirect ('fishing:lure_mix_details', lure_mix.id)
        return redirect('fishing:index')


class EditAromaToMix(View):
    """
    Редактиорвание выбраннй аромы в смеси
    """
    template = 'fishing/luremix/edit_add_aroma.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditAromaToMix, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if lure_mix.owner == request.user and aroma.mix == lure_mix:
            form = AromaForm(request.POST, instance=aroma)
            if form.is_valid():
                aroma = form.save(commit=False)
                aroma.save()
                return redirect('fishing:lure_mix_details', lure_mix.id)
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'lure_mix': lure_mix,
                               'aroma': aroma})
        return redirect('fishing:lure_mix')
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if lure_mix.owner == request.user and aroma.mix == lure_mix:
            form = AromaForm(instance=aroma)
            return render(request,
                          self.template,
                          {'form': form,
                           'lure_mix': lure_mix,
                           'aroma': aroma})
        return redirect('fishing:lure_mix')


class LureMixAdd(View):
    """
    Добавление прикормочных смесей
    """
    template = 'fishing/luremix/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LureMixForm(request.POST)
        if form.is_valid():
            lure_mix = form.save(commit=False)
            lure_mix.owner = request.user
            if lure_mix.unique():
                lure_mix.first_upper()
                lure_mix.save()
                return redirect('fishing:lure_mix')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая прикормочная смесь уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = LureMixForm()
        return render(request,
                      self.template,
                      {'form': form})


class LureMixList(View):
    """
    Возвращает список прикормочных смесей
    """

    template = 'fishing/luremix/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            lure_mix_list = LureMix.objects.all()
        else:
            lure_mix_list = LureMix.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'lure_mix_list': lure_mix_list})


class LureMixDelete(View):
    """
    Удаление прикормочной смеси
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            lure_mix.delete()
        return redirect('fishing:lure_mix')


class LureMixEdit(View):
    """
    Изменение названия прикормочной смеси
    """
    template = 'fishing/luremix/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            form = LureMixForm(request.POST, instance=lure_mix)
            if form.is_valid():
                lure_mix = form.save(commit=False)
                lure_mix.owner = request.user
                if lure_mix.unique():
                    lure_mix.first_upper()
                    lure_mix.save()
                    return redirect('fishing:lure_mix')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'lure_mix': lure_mix,
                                 'errors': 'Такая прикормочная смесь уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            form = LureMixForm(instance=lure_mix)
            return render(request,
                        self.template,
                        {'form': form,
                        'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')


class LureMixDetails(View):
    """
    Подробности о прикормочной смеси
    """

    template = 'fishing/luremix/details.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixDetails, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            return render(request,
                    self.template,
                    {'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')


class SelectLureForMix(View):
    """
    Список прикормов для выбора в прикормочную смесь
    """

    template = 'fishing/luremix/select_lure.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SelectLureForMix, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            lure_base_list = LureBase.objects.filter(owner=request.user)
            return render(request,
                    self.template,
                    {'lure_mix': lure_mix,
                     'lure_base_list': lure_base_list})
        return redirect('fishing:lure_mix')


class AddLureToMix(View):
    """
    Добавление выбранного прикорма в смесь
    """
    template = 'fishing/luremix/edit_add_lure.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddLureToMix, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_mix.owner == request.user and lure_mix.owner == lure_base.owner:
            form = LureForm(request.POST)
            if form.is_valid():
                lure = form.save(commit=False)
                lure.owner = request.user
                lure.mix = lure_mix
                lure.base = lure_base
                lure.save()
                return redirect('fishing:lure_mix_details', lure_mix.id)
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'lure_mix': lure_mix,
                               'lure_base': lure_base})
        return redirect('fishing:lure_mix')
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_mix.owner == request.user and lure_mix.owner == lure_base.owner:
            form = LureForm()
            return render(request,
                          self.template,
                          {'form': form,
                           'lure_mix': lure_mix})
        return redirect('fishing:lure_mix')


class DeleteLureOfMix(View):
    """
    Удаляет прикорм из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteLureOfMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        if lure.owner == request.user:
            lure.delete()
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            return redirect ('fishing:lure_mix_details', lure_mix.id)
        return redirect('fishing:index')


class EditLureToMix(View):
    """
    Редактиорвание выбранного прикорма в смеси
    """
    template = 'fishing/luremix/edit_add_lure.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditLureToMix, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        if lure_mix.owner == request.user and lure.mix == lure_mix:
            form = LureForm(request.POST, instance=lure)
            if form.is_valid():
                lure = form.save(commit=False)
                lure.save()
                return redirect('fishing:lure_mix_details', lure_mix.id)
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'lure_mix': lure_mix,
                               'lure': lure})
        return redirect('fishing:lure_mix')
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        if lure_mix.owner == request.user and lure.mix == lure_mix:
            form = LureForm(instance=lure)
            return render(request,
                          self.template,
                          {'form': form,
                           'lure_mix': lure_mix,
                           'lure': lure})
        return redirect('fishing:lure_mix')


class SelectNozzleForMix(View):
    """
    Возвращает список наживок/насадок для добавления в прикормочную смесь
    """
    
    template = 'fishing/luremix/select_nozzle.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SelectNozzleForMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            nozzle_base_list = NozzleBase.objects.filter(owner=request.user)
            return render(request,
                    self.template,
                    {'lure_mix': lure_mix,
                     'nozzle_base_list': nozzle_base_list})
        return redirect('fishing:lure_mix')


class SelectNozzleStateForMix(View):
    """
    Возвращает список состояний наживок/насадок для добавления в прикормочную смесь
    """
    
    template = 'fishing/luremix/select_nozzle_state.html'
    
    def dispatch(self, *args, **kwargs):
        return super(SelectNozzleStateForMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle_base.owner == request.user and lure_mix.owner == request.user:
            nozzle_state_list = NozzleState.objects.filter(owner=request.user)
            return render(request,
                          self.template,
                          {'lure_mix': lure_mix,
                           'nozzle_base': nozzle_base,
                           'nozzle_state_list': nozzle_state_list})
        return redirect('fishing:lure_mix')

class AddNozzleToMix(View):
    """
    Добавление выбранной насдки/каживки в смесь
    """
    template = 'fishing/luremix/edit_add_nozzle.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddNozzleToMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if (lure_mix.owner == request.user and lure_mix.owner == nozzle_base.owner and
            lure_mix.owner == nozzle_state.owner):
            nozzle = Nozzle()
            nozzle.owner = request.user
            nozzle.mix = lure_mix
            nozzle.base = nozzle_base
            nozzle.state = nozzle_state
            nozzle.save()
            return redirect('fishing:lure_mix_details', lure_mix.id)
        return redirect('fishing:lure_mix')


class DeleteNozzleOfMix(View):
    """
    Удаляет насадку или наживку из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DeleteNozzleOfMix, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        nozzle = get_object_or_404(Nozzle, pk=kwargs['nozzle_id'])
        if nozzle.owner == request.user:
            nozzle.delete()
            lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
            return redirect ('fishing:lure_mix_details', lure_mix.id)
        return redirect('fishing:index')


class EditNozzleToMix(View):
    """
    Редактиорвание выбранной насадки или наживки в смеси
    """
    template = 'fishing/luremix/edit_add_nozzle.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditNozzleToMix, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        nozzle = get_object_or_404(Nozzle, pk=kwargs['nozzle_id'])
        if lure_mix.owner == request.user and nozzle.mix == lure_mix:
            form = NozzleForm(request.POST, instance=nozzle)
            if form.is_valid():
                nozzle = form.save(commit=False)
                nozzle.save()
                return redirect('fishing:lure_mix_details', lure_mix.id)
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'lure_mix': lure_mix,
                               'nozzle': nozzle})
        return redirect('fishing:lure_mix')
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        nozzle = get_object_or_404(Nozzle, pk=kwargs['nozzle_id'])
        if lure_mix.owner == request.user and nozzle.mix == lure_mix:
            form = NozzleForm(instance=nozzle)
            return render(request,
                          self.template,
                          {'form': form,
                           'lure_mix': lure_mix,
                           'nozzle': nozzle})
        return redirect('fishing:lure_mix')

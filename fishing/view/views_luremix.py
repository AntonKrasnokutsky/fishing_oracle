from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

from fishing.models import Aroma, NozzleType
from fishing.models import AromaBase
from fishing.models import Lure
from fishing.models import LureBase
from fishing.models import LureMix
from fishing.models import Nozzle
from fishing.models import NozzleBase
from fishing.models import NozzleState
from fishing.forms import AromaBaseForm, AromaForm, BaitBaseForm, LureBaseForm, NozzleBaseForm, NozzleStateForm
from fishing.forms import LureForm
from fishing.forms import LureMixForm
from fishing.forms import NozzleForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SelectAromaForMix(View):
    """
    Список прикормов для выбора в прикормочную смесь
    """

    template = 'fishing/notes/feeds/luremix/select_aroma.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'lure_mix_id': lure_mix.id}
            param.update(lure_mix.aroma_for_add())
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:lure_mix')


class AddAromaToMix(View):
    """
    Добавление выбранной аромы в смесь
    """
    template = 'fishing/notes/feeds/luremix/edit_add_aroma.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = AromaForm.save_me(self.request, lure_mix_id=kwargs['lure_mix_id'], aroma_base_id=kwargs['aroma_base_id'])            
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result,
                       'lure_mix': kwargs['lure_mix_id']})
    
    def get(self, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            form = AromaForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'lure_mix_id': lure_mix.id})
        return redirect('fishing:lure_mix')


class DeleteAromaOfMix(View):
    """
    Удаляет аромы из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if aroma.owner == request.user:
            aroma.delete()
            return redirect ('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return redirect('fishing:index')


class EditAromaToMix(View):
    """
    Редактиорвание выбраннй аромы в смеси
    """
    template = 'fishing/notes/feeds/luremix/edit_add_aroma.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        result = AromaForm.save_me(self.request, lure_mix_id=kwargs['lure_mix_id'], aroma_base_id=kwargs['aroma_base_id'], aroma_id=kwargs['aroma_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result,
                       'edit': True,
                       'lure_mix': kwargs['lure_mix_id']})
    
    def get(self, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if aroma.owner == self.request.user:
            form = AromaForm(instance=aroma)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'edit': True,
                           'lure_mix_id': kwargs['lure_mix_id']})
        return redirect('fishing:lure_mix')


class AromaBaseAddFromLureMix(View):
    template = 'fishing/notes/feeds/luremix/aroma_base_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = AromaBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:add_aroma_to_mix', kwargs['lure_mix_id'], result)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': result})

    def get(self, *args, **kwargs):
        form = AromaBaseForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': form})


class LureMixAdd(View):
    """
    Добавление прикормочных смесей
    """
    template = 'fishing/notes/feeds/luremix/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LureMixAdd, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = LureMixForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix_details', result)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        form = LureMixForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class LureMixList(View):
    """
    Возвращает список прикормочных смесей
    """

    template = 'fishing/notes/feeds/luremix/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix_list = LureMix.objects.filter(owner=self.request.user)
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'lure_mix_list': lure_mix_list})


class LureMixDelete(View):
    """
    Удаление прикормочной смеси
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user and lure_mix.removable():
            lure_mix.delete()
        return redirect('fishing:lure_mix')


class LureMixEdit(View):
    """
    Изменение названия прикормочной смеси
    """
    template = 'fishing/notes/feeds/luremix/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = LureMixForm.save_me(self.request, lure_mix_id=kwargs['lure_mix_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            form = LureMixForm(instance=lure_mix)
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'form': form})
        return redirect('fishing:lure_mix')


class LureMixDetails(View):
    """
    Подробности о прикормочной смеси
    """

    template = 'fishing/notes/feeds/luremix/details.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'lure_mix': lure_mix,
                     'editable': lure_mix.editable()})
        return redirect('fishing:lure_mix')


class SelectLureForMix(View):
    """
    Список прикормов для выбора в прикормочную смесь
    """

    template = 'fishing/notes/feeds/luremix/select_lure.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'lure_mix': lure_mix}
            param.update(lure_mix.lure_for_add())
            return render(request,
                        self.template,
                        param)
        return redirect('fishing:lure_mix')


class AddLureToMix(View):
    """
    Добавление выбранного прикорма в смесь
    """
    template = 'fishing/notes/feeds/luremix/edit_add_lure.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        result = LureForm.save_me(self.request, lure_mix_id=kwargs['lure_mix_id'], lure_base_id=kwargs['lure_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'form': result,
                        'lure_mix_id': kwargs['lure_mix_id']})
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_mix.owner == self.request.user and lure_mix.owner == lure_base.owner:
            form = LureForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'lure_mix_id': kwargs['lure_mix_id']})
        return redirect('fishing:lure_mix')


class DeleteLureOfMix(View):
    """
    Удаляет прикорм из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure.owner == request.user:
            lure.delete()
            return redirect ('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return redirect('fishing:index')


class EditLureToMix(View):
    """
    Редактиорвание выбранного прикорма в смеси
    """
    template = 'fishing/notes/feeds/luremix/edit_add_lure.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        result = LureForm.save_me(self.request, lure_mix_id=kwargs['lure_mix_id'], lure_id=kwargs['lure_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                        'siteinfo': siteinfo(),
                        'form': result,
                        'edit': True,
                        'lure_mix_id': kwargs['lure_mix_id']})
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        if lure_mix.owner == request.user and lure.mix == lure_mix:
            form = LureForm(instance=lure)
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'edit': True,
                           'lure_mix_id': kwargs['lure_mix_id']})
        return redirect('fishing:lure_mix')


class LureBaseAddFromLureMix(View):
    template = 'fishing/notes/feeds/luremix/lure_base_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        result = LureBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:add_lure_to_mix', kwargs['lure_mix_id'], result)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': result})

    def get(self, request, *args, **kwargs):
        form = LureBaseForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': form})


class SelectNozzleForMix(View):
    """
    Возвращает список наживок/насадок для добавления в прикормочную смесь
    """
    
    template = 'fishing/notes/feeds/luremix/nozzle/select.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure_mix.owner == request.user:
            nozzle_base_list = NozzleBase.objects.filter(owner=request.user)
            return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'luremix_id': kwargs['lure_mix_id'],
                     'nozzle_base_list': nozzle_base_list})
        return redirect('fishing:lure_mix')


class NozzleBaseAddFromLureMix(View):
    template = 'fishing/notes/feeds/luremix/nozzle/nozzle_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = NozzleBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:select_nozzle_state_for_mix', kwargs['lure_mix_id'], result)
        nozzletypes = NozzleType.objects.all()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': result,
                       'nozzletypes': nozzletypes})

    def get(self, *args, **kwargs):
        form = NozzleBaseForm()
        nozzletypes = NozzleType.objects.all()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': form,
                       'nozzletypes': nozzletypes})


class BaitBaseAddFromLureMix(View):
    template = 'fishing/notes/feeds/luremix/nozzle/bait_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = BaitBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:select_nozzle_state_for_mix', kwargs['lure_mix_id'], result)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': result})

    def get(self, *args, **kwargs):
        form = BaitBaseForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': form})


class SelectNozzleStateForMix(View):
    """
    Возвращает список состояний наживок/насадок для добавления в прикормочную смесь
    """
    
    template = 'fishing/notes/feeds/luremix/nozzle/state/select.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'luremix_id': lure_mix.id,
                     'nozzlebase_id': kwargs['nozzle_base_id']}
            param.update(lure_mix.state_for_select(nozzle_base_id=kwargs['nozzle_base_id']))
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:lure_mix')


class NozzleStateAddFromLureMix(View):
    template = 'fishing/notes/feeds/luremix/nozzle/state/add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        result = NozzleStateForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:add_nozzle_to_mix', kwargs['lure_mix_id'], kwargs['nozzle_base_id'], result)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'lure_mix_id': kwargs['lure_mix_id'],
                       'nozzle_base_id': kwargs['nozzle_base_id'],
                       'form': result})

    def get(self, *args, **kwargs):
        form = NozzleStateForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'lure_mix_id': kwargs['lure_mix_id'],
                       'nozzle_base_id': kwargs['nozzle_base_id'],
                       'form': form})


class AddNozzleToMix(View):
    """
    Добавление выбранной насдки/каживки в смесь
    """
    template = 'fishing/notes/feeds/luremix/edit_add_nozzle.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        result = Nozzle.save_me(user=self.request.user, **kwargs)
        if result:
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return redirect('fishing:lure_mix')


class DeleteNozzleOfMix(View):
    """
    Удаляет насадку или наживку из прикормочной смеси
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        lure_mix = get_object_or_404(LureMix, pk=kwargs['lure_mix_id'])
        if not lure_mix.editable():
            return redirect('fishing:lure_mix_details', kwargs['lure_mix_id'])
        nozzle = get_object_or_404(Nozzle, pk=kwargs['nozzle_id'])
        if nozzle.owner == request.user:
            nozzle.delete()
            return redirect ('fishing:lure_mix_details', kwargs['lure_mix_id'])
        return redirect('fishing:index')

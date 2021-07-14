from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import NozzleBase
from fishing.models import NozzleState
from fishing.models import NozzleType
from fishing.forms import NozzleBaseForm
from fishing.forms import NozzleStateForm
from fishing.forms import BaitBaseForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class NozzleStateAdd(View):
    """
    Добавление состояния насадки или наживки
    """
    template = 'fishing/notes/feeds/nozzlestate/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = NozzleStateForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        form = NozzleStateForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class NozzleStateEdit(View):
    """
    Изменение состояния насадки или наживки
    """
    template = 'fishing/notes/feeds/nozzlestate/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = NozzleStateForm.save_me(self.request, nozzle_state_id=kwargs['nozzle_state_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == self.request.user:
            form = NozzleStateForm(instance=nozzle_state)
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'form': form})
        return redirect('fishing:nozzle_base')


class NozzleStateDelete(View):
    """
    Удаление состояния наживки/насадки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == request.user:
            nozzle_state.delete()
        return redirect('fishing:nozzle_base')


class NozzleBaseAdd(View):
    """
    Добавление насадки
    """
    template = 'fishing/notes/feeds/nozzlebase/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = NozzleBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        nozzletypes = NozzleType.objects.all()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'nozzletypes': nozzletypes,
                       'form': result})

    def get(self, request, *args, **kwargs):
        form = NozzleBaseForm()
        nozzletypes = NozzleType.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'nozzletypes': nozzletypes,
                       'form': form})


class NozzleBaseList(View):
    """
    Возвращает список наживок/насадок
    """

    template = 'fishing/notes/feeds/nozzlebase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            nozzle_base_list = NozzleBase.objects.all()
            nozzle_state_list = NozzleState.objects.all()
        else:
            nozzle_base_list = NozzleBase.objects.filter(owner=request.user)
            nozzle_state_list = NozzleState.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'nozzle_base_list': nozzle_base_list,
                     'nozzle_state_list':nozzle_state_list})


class NozzleBaseDelete(View):
    """
    Удаление наживки/насадки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle.owner == request.user:
            nozzle.delete()
        return redirect('fishing:nozzle_base')


class NozzleBaseEdit(View):
    """
    Изменение насадки
    """
    template = 'fishing/notes/feeds/nozzlebase/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = NozzleBaseForm.save_me(self.request, nozzle_id=kwargs['nozzle_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        nozzletypes = NozzleType.objects.all()
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                    'siteinfo': siteinfo(),
                    'nozzletypes': nozzletypes,
                    'form': result})

    def get(self, *args, **kwargs):
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle_base.owner == self.request.user:
            form = NozzleBaseForm(instance=nozzle_base)
            nozzletypes = NozzleType.objects.all()
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'nozzletypes': nozzletypes,
                         'form': form})
        return redirect('fishing:nozzle_base')


class BaitBaseAdd(View):
    """
    Добавление насадки
    """
    template = 'fishing/notes/feeds/nozzlebase/bait_edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = BaitBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                    'siteinfo': siteinfo(),
                    'form': result})

    def get(self, *args, **kwargs):
        form = BaitBaseForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class BaitBaseEdit(View):
    """
    Изменение наживки
    """
    template = 'fishing/notes/feeds/nozzlebase/bait_edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        result = BaitBaseForm.save_me(self.request, bait_id=kwargs['bait_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:nozzle_base')
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                    'siteinfo': siteinfo(),
                    'form': result})

    def get(self, *args, **kwargs):
        bait_base = get_object_or_404(NozzleBase, pk=kwargs['bait_base_id'])
        if bait_base.owner == self.request.user:
            form = BaitBaseForm(instance=bait_base)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form})
        return redirect('fishing:nozzle_base')

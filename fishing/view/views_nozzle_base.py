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
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Такое состояние уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = NozzleStateForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
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
                                {'fisherman': getuserinfo(request),
                                 'siteinfo': siteinfo(),
                                 'form': form,
                                 'nozzle_state': nozzle_state,
                                 'errors': 'Такое сосотояние наживки или насадки уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'fisherman': getuserinfo(request),
                             'siteinfo': siteinfo(),
                             'form': form,
                             'nozzle_state': nozzle_state})

    def get(self, request, *args, **kwargs):
        nozzle_state = get_object_or_404(NozzleState, pk=kwargs['nozzle_state_id'])
        if nozzle_state.owner == request.user:
            form = NozzleStateForm(instance=nozzle_state)
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'form': form,
                         'nozzle_state': nozzle_state})
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
    template = 'fishing/notes/feeds/nozzlebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
                nozzletypes = NozzleType.objects.all()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'nozzletypes': nozzletypes,
                               'form': form,
                               'errors': 'Такая насадка уже добавлена'})
        else:
            nozzletypes = NozzleType.objects.all()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'nozzletypes': nozzletypes,
                           'form': form})

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
    template = 'fishing/notes/feeds/nozzlebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
                    nozzletypes = NozzleType.objects.all()
                    return render(request,
                                self.template,
                                {'fisherman': getuserinfo(request),
                                 'siteinfo': siteinfo(),
                                 'nozzletypes': nozzletypes,
                                 'form': form,
                                 'nozzle_base': nozzle_base,
                                 'errors': 'Такая насадка уже добавлена'})
            else:
                nozzletypes = NozzleType.objects.all()
                return render(request,
                            self.template,
                            {'fisherman': getuserinfo(request),
                             'siteinfo': siteinfo(),
                             'nozzletypes': nozzletypes,
                             'form': form,
                             'nozle_base': nozzle_base})

    def get(self, request, *args, **kwargs):
        nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_base_id'])
        if nozzle_base.owner == request.user:
            form = NozzleBaseForm(instance=nozzle_base)
            nozzletypes = NozzleType.objects.all()
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'nozzletypes': nozzletypes,
                         'form': form,
                         'nozzle_base': nozzle_base})
        return redirect('fishing:nozzle_base')


class BaitBaseAdd(View):
    """
    Добавление насадки
    """
    template = 'fishing/notes/feeds/nozzlebase/bait_edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Такая наживка уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = BaitBaseForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
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
                                {'fisherman': getuserinfo(request),
                                 'siteinfo': siteinfo(),
                                 'form': form,
                                 'bait_base': bait_base,
                                 'errors': 'Такая наживка уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'fisherman': getuserinfo(request),
                             'siteinfo': siteinfo(),
                             'form': form,
                             'bait_base': bait_base})

    def get(self, request, *args, **kwargs):
        bait_base = get_object_or_404(NozzleBase, pk=kwargs['bait_base_id'])
        if bait_base.owner == request.user:
            form = BaitBaseForm(instance=bait_base)
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'form': form,
                         'bait_base': bait_base})
        return redirect('fishing:nozzle_base')

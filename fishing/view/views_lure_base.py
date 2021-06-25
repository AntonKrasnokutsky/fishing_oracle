from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import LureBase
from fishing.forms import LureBaseForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LureBaseAdd(View):
    """
    Добавление прикорма
    """
    template = 'fishing/notes/feeds/lurebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Такой прикорм уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = LureBaseForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class LureBaseList(View):
    """
    Возвращает список прикормов
    """

    template = 'fishing/notes/feeds/lurebase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            lure_base_list = LureBase.objects.all()
        else:
            lure_base_list = LureBase.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'lure_base_list': lure_base_list})


class LureBaseDelete(View):
    """
    Удаление прикорма
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        lure = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure.owner == request.user:
            lure.delete()
        return redirect('fishing:lure_base')


class LureBaseEdit(View):
    """
    Изменение прикорма
    """
    template = 'fishing/notes/feeds/lurebase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

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
                                {'fisherman': getuserinfo(request),
                                 'siteinfo': siteinfo(),
                                 'form': form,
                                 'lure_base': lure_base,
                                 'errors': 'Такой прикорм уже добавлен'})
            else:
                return render(request,
                            self.template,
                            {'fisherman': getuserinfo(request),
                             'siteinfo': siteinfo(),
                             'form': form,
                             'lure_base': lure_base})

    def get(self, request, *args, **kwargs):
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_base.owner == request.user:
            form = LureBaseForm(instance=lure_base)
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'form': form,
                         'lure_base': lure_base})
        return redirect('fishing:lure_base')


class LureBaseAddFromLureMix(View):
    template = 'fishing/luremix/lure_base_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        form = LureBaseForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'luremix_id': kwargs['lure_mix_id'],
                       'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LureBaseForm(request.POST)
        lure_base = LureBase()
        if form.is_valid():
            lure_base = form.save(commit=False)
            lure_base.owner = request.user
            if lure_base.unique():
                lure_base.first_upper()
                lure_base.save()
                return redirect('fishing:add_lure_to_mix', kwargs['lure_mix_id'], lure_base.id)
            else:
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'luremix_id': kwargs['lure_mix_id'],
                               'form': form,
                               'errors': 'Такой прикорм уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'luremix_id': kwargs['lure_mix_id'],
                           'form': form})

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

    def post(self, *args, **kwargs):
        result = LureBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        form = LureBaseForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
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

    def get(self, *args, **kwargs):
        lure_base_list = LureBase.objects.filter(owner=self.request.user)
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'lure_base_list': lure_base_list})


class LureBaseDelete(View):
    """
    Удаление прикорма
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure.owner == self.request.user:
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

    def post(self, *args, **kwargs):
        result = LureBaseForm.save_me(self.request, lure_id=kwargs['lure_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:lure_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
        if lure_base.owner == self.request.user:
            form = LureBaseForm(instance=lure_base)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                          'siteinfo': siteinfo(),
                          'form': form})
        return redirect('fishing:lure_base')


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

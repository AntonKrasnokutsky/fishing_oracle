from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import AromaBase
from fishing.forms import AromaBaseForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AromaBaseAdd(View):
    """
    Добавление аромы
    """
    template = 'fishing/notes/feeds/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = AromaBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:aroma_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        form = AromaBaseForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class AromaBaseList(View):
    """
    Возвращает список аром
    """

    template = 'fishing/notes/feeds/aromabase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        aroma_base_list = AromaBase.objects.filter(owner=self.request.user)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'aroma_base_list': aroma_base_list})


class AromaBaseDelete(View):
    """
    Удаление аромы
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        aroma = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma.owner == request.user:
            aroma.delete()
        return redirect('fishing:aroma_base')


class AromaBaseEdit(View):
    """
    Изменение аромы
    """
    template = 'fishing/notes/feeds/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = AromaBaseForm.save_me(self.request, aroma_id=kwargs['aroma_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:aroma_base')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma_base.owner == self.request.user:
            form = AromaBaseForm(instance=aroma_base)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form})
        return redirect('fishing:aroma_base')

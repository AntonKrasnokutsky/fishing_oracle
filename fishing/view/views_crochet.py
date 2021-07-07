from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Crochet
from fishing.forms import CrochetForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CrochetAdd(View):
    """
    Добавление крючка
    """
    template = 'fishing/notes/gears/crochet/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = CrochetForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:crochet')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        form = CrochetForm()
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class CrochetList(View):
    """
    Возвращает список крючков
    """

    template = 'fishing/notes/gears/crochet/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            crochet_list = Crochet.objects.all()
        else:
            crochet_list = Crochet.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'crochet_list': crochet_list})


class CrochetDelete(View):
    """
    Удаление крючка
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if crochet.owner == request.user:
            crochet.delete()
        return redirect('fishing:crochet')


class CrochetEdit(View):
    """
    Изменение крючка
    """
    template = 'fishing/notes/gears/crochet/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = CrochetForm.save_me(self.request, crochet_id=kwargs['crochet_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:crochet')
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': result})

    def get(self, *args, **kwargs):
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        if crochet.owner == self.request.user:
            form = CrochetForm(instance=crochet)
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'form': form})
        return redirect('fishing:crochet')

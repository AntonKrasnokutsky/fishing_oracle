from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Montage
from fishing.forms import MontageForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MontageAdd(View):
    """
    Добавление монтажа
    """
    template = 'fishing/notes/gears/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageAdd, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = MontageForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:montage')
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': result})

    def get(self, request, *args, **kwargs):
        form = MontageForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class MontageList(View):
    """
    Возвращает монтажей
    """

    template = 'fishing/notes/gears/montage/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            montage_list = Montage.objects.all()
        else:
            montage_list = Montage.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'montage_list': montage_list})


class MontageDelete(View):
    """
    Удаление монтажа
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            montage.delete()
        return redirect('fishing:montage')


class MontageEdit(View):
    """
    Изменение монтажа
    """
    template = 'fishing/notes/gears/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageEdit, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = MontageForm.save_me(self.request, montage_id=kwargs['montage_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:montage')
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': result})

    def get(self, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == self.request.user:
            form = MontageForm(instance=montage)
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'form': form})
        return redirect('fishing:montage')

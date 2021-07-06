from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Tackle
from fishing.forms import TackleForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TackleAdd(View):
    """
    Добавление снастей
    """
    template = 'fishing/notes/gears/tackle/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleAdd, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = TackleForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:tackle')
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': result})

    def get(self, request, *args, **kwargs):
        form = TackleForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class TackleList(View):
    """
    Возвращает список снастей
    """

    template = 'fishing/notes/gears/tackle/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            tackle_list = Tackle.objects.all()
        else:
            tackle_list = Tackle.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                      'siteinfo': siteinfo(),
                      'tackle_list': tackle_list})


class TackleDelete(View):
    """
    Удаление снасти
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        if tackle.owner == request.user:
            tackle.delete()
        return redirect('fishing:tackle')


class TackleEdit(View):
    """
    Изменение снасти
    """
    template = 'fishing/notes/gears/tackle/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TackleEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        result = TackleForm.save_me(self.request, tackle_id=kwargs['tackle_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:tackle')
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': result})

    def get(self, request, *args, **kwargs):
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        if tackle.owner == request.user:
            form = TackleForm(instance=tackle)
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'form': form,
                         'tackle': tackle})
        return redirect('fishing:tackle')

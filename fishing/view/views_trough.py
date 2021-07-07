from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Trough
from fishing.forms import TroughForm
from fishing.models import FeedCapacity

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TroughAdd(View):
    """
    Добавление кормушек
    """
    template = 'fishing/notes/gears/trough/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        result = TroughForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:trough')
        feedcapacitys = FeedCapacity.objects.all()
        return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                        'siteinfo': siteinfo(),
                        'feedcapacitys': feedcapacitys,
                        'form': result})

    def get(self, request, *args, **kwargs):
        form = TroughForm()
        feedcapacitys = FeedCapacity.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'feedcapacitys': feedcapacitys,
                       'form': form})


class TroughList(View):
    """
    Возвращает список кормушек
    """

    template = 'fishing/notes/gears/trough/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            trough_list = Trough.objects.all()
        else:
            trough_list = Trough.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'fisherman': getuserinfo(request),
                     'siteinfo': siteinfo(),
                     'trough_list': trough_list})


class TroughDelete(View):
    """
    Удаление кормушки
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            trough.delete()
        return redirect('fishing:trough')


class TroughEdit(View):
    """
    Изменение кормушки
    """
    template = 'fishing/notes/gears/trough/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TroughEdit, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = TroughForm.save_me(self.request, trough_id=kwargs['trough_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:trough')
        feedcapacitys = FeedCapacity.objects.all()
        return render(self.request,
                    self.template,
                    {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'feedcapacitys': feedcapacitys,
                        'form': result})

    def get(self, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == self.request.user:
            form = TroughForm(instance=trough)
            feedcapacitys = FeedCapacity.objects.all()
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'feedcapacitys': feedcapacitys,
                         'form': form})
        return redirect('fishing:trough')

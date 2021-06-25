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
        form = TroughForm(request.POST)
        trough = Trough()
        if form.is_valid():
            trough = form.save(commit=False)
            trough.owner = request.user
            if trough.unique():
                trough.first_upper()
                trough.save()
                return redirect('fishing:trough')
            else:
                feedcapacitys = FeedCapacity.objects.all()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'feedcapacitys': feedcapacitys,
                               'form': form,
                               'errors': 'Такая кормушка уже добавлена'})
        else:
            feedcapacitys = FeedCapacity.objects.all()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'feedcapacitys': feedcapacitys,
                           'form': form})

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

    def post(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            form = TroughForm(request.POST, instance=trough)
            if form.is_valid():
                trough = form.save(commit=False)
                trough.owner = request.user
                if trough.unique():
                    trough.first_upper()
                    trough.save()
                    return redirect('fishing:trough')
                else:
                    feedcapacitys = FeedCapacity.objects.all()
                    return render(request,
                                self.template,
                                {'fisherman': getuserinfo(request),
                                 'siteinfo': siteinfo(),
                                 'feedcapacitys': feedcapacitys,
                                 'form': form,
                                 'trough': trough,
                                 'errors': 'Такая кормушка уже добавлена'})
            else:
                feedcapacitys = FeedCapacity.objects.all()
                return render(request,
                            self.template,
                            {'fisherman': getuserinfo(request),
                             'siteinfo': siteinfo(),
                             'feedcapacitys': feedcapacitys,
                             'form': form,
                             'trough': trough})

    def get(self, request, *args, **kwargs):
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        if trough.owner == request.user:
            form = TroughForm(instance=trough)
            feedcapacitys = FeedCapacity.objects.all()
            return render(request,
                        self.template,
                        {'fisherman': getuserinfo(request),
                         'siteinfo': siteinfo(),
                         'feedcapacitys': feedcapacitys,
                         'form': form,
                         'trough': trough})
        return redirect('fishing:trough')

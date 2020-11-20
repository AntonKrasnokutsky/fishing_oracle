from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Leash
from fishing.forms import LeashForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LeashAdd(View):
    """
    Добавление поводка
    """
    template = 'fishing/leash/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LeashForm(request.POST)
        leash = Leash()
        if form.is_valid():
            leash = form.save(commit=False)
            leash.owner = request.user
            if leash.unique():
                leash.first_upper()
                leash.save()
                return redirect('fishing:leash')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой поводок уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = LeashForm()
        return render(request,
                      self.template,
                      {'form': form})


class LeashList(View):
    """
    Возвращает список поводков
    """

    template = 'fishing/leash/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            leash_list = Leash.objects.all()
        else:
            leash_list = Leash.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'leash_list': leash_list})


class LeashDelete(View):
    """
    Удаление поводка
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            leash.delete()
        return redirect('fishing:leash')


class LeashEdit(View):
    """
    Изменение поводка
    """
    template = 'fishing/leash/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LeashEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            form = LeashForm(request.POST, instance=leash)
            if form.is_valid():
                leash = form.save(commit=False)
                leash.owner = request.user
                if leash.unique():
                    leash.first_upper()
                    leash.save()
                    return redirect('fishing:leash')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'leash': leash,
                                'errors': 'Такой поводок уже добавлен'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'leash': leash})
        else:
            return redirect('fishing:leash')

    def get(self, request, *args, **kwargs):
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        if leash.owner == request.user:
            form = LeashForm(instance=leash)
            return render(request,
                        self.template,
                        {'form': form,
                        'leash': leash})
        return redirect('fishing:leash')

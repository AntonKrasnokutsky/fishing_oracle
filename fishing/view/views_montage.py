from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import Montage
from fishing.forms import MontageForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class MontageAdd(View):
    """
    Добавление монтажа
    """
    template = 'fishing/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = MontageForm(request.POST)
        montage = Montage()
        if form.is_valid():
            montage = form.save(commit=False)
            montage.owner = request.user
            if montage.unique():
                montage.first_upper()
                montage.save()
                return redirect('fishing:montage')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такой монтаж уже добавлен'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = MontageForm()
        return render(request,
                      self.template,
                      {'form': form})


class MontageList(View):
    """
    Возвращает монтажей
    """

    template = 'fishing/montage/list.html'

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
                    {'montage_list': montage_list})


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
    template = 'fishing/montage/edit_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MontageEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            form = MontageForm(request.POST, instance=montage)
            if form.is_valid():
                montage = form.save(commit=False)
                montage.owner = request.user
                if montage.unique():
                    montage.first_upper()
                    montage.save()
                    return redirect('fishing:montage')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'montage': montage,
                                'errors': 'Такой монтаж уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'montage': montage})
        return redirect('fishing:montage')

    def get(self, request, *args, **kwargs):
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        if montage.owner == request.user:
            form = NozzleBaseForm(instance=montage)
            return render(request,
                        self.template,
                        {'form': form,
                        'montage': montage})
        return redirect('fishing:montage')

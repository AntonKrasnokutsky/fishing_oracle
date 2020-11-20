from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from fishing.models import AromaBase
from fishing.forms import AromaBaseForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AromaBaseAdd(View):
    """
    Добавление аромы
    """
    template = 'fishing/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseAdd, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = AromaBaseForm(request.POST)
        aroma_base = AromaBase()
        if form.is_valid():
            aroma_base = form.save(commit=False)
            aroma_base.owner = request.user
            if aroma_base.unique():
                aroma_base.first_upper()
                aroma_base.save()
                return redirect('fishing:aroma_base')
            else:
                return render(request,
                              self.template,
                              {'form': form,
                               'errors': 'Такая арома уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'form': form})

    def get(self, request, *args, **kwargs):
        form = AromaBaseForm()
        return render(request,
                      self.template,
                      {'form': form})


class AromaBaseList(View):
    """
    Возвращает список аром
    """

    template = 'fishing/aromabase/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseList, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            aroma_base_list = AromaBase.objects.all()
        else:
            aroma_base_list = AromaBase.objects.filter(owner=request.user)
        return render(request,
                    self.template,
                    {'aroma_base_list': aroma_base_list})


class AromaBaseDelete(View):
    """
    Удаление аромы
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseDelete, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        aroma = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma.owner == request.user:
            aroma.delete()
        return redirect('fishing:aroma_base')


class AromaBaseEdit(View):
    """
    Изменение аромы
    """
    template = 'fishing/aromabase/renewal_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AromaBaseEdit, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma_base.owner == request.user:
            form = AromaBaseForm(request.POST, instance=aroma_base)
            if form.is_valid():
                aroma_base = form.save(commit=False)
                aroma_base.owner = request.user
                if aroma_base.unique():
                    aroma_base.first_upper()
                    aroma_base.save()
                    return redirect('fishing:aroma_base')
                else:
                    return render(request,
                                self.template,
                                {'form': form,
                                 'aroma_base': aroma_base,
                                'errors': 'Такая арома уже добавлена'})
            else:
                return render(request,
                            self.template,
                            {'form': form,
                            'aroma_base': aroma_base})

    def get(self, request, *args, **kwargs):
        aroma_base = get_object_or_404(AromaBase, pk=kwargs['aroma_base_id'])
        if aroma_base.owner == request.user:
            form = AromaBaseForm(instance=aroma_base)
            return render(request,
                        self.template,
                        {'form': form,
                        'aroma_base': aroma_base})
        return redirect('fishing:aroma_base')

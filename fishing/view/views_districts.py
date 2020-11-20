from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from fishing.models import District
from fishing.forms import DistrictForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def district_add(request):
    num_visits = visits(request)
    district = District()
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            district = form.save(commit=False)
            district.save()
        return redirect('fishing:water', district.id)
    else:
        form = DistrictForm()
    return render(request, template_renewal_add_path,
                  {'form': form,
                   'district': district,
                   'num_visits': num_visits})


@login_required
def district_list(request):
    """
    Список районов
    """
    districts_list = District.objects.all()
    num_visits = visits(request)
    return render(request,
                  template_list_path,
                  {'districts_list': districts_list,
                   'num_visits': num_visits})



def district_remove(request, district_id):
    """
    Удаление района
    """
    district = get_object_or_404(District, pk=district_id)
    district.delete()
    return redirect('fishing:districts')



def district_renewal(request, district_id):
    """
    Редактирование района
    """
    num_visits = visits(request)
    district = get_object_or_404(District, pk=district_id)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            district = form.save(commit=False)
            district.save()
        return redirect('fishing:districts')
    else:
        form = DistrictForm(instance=district)
        return render(request, template_renewal_add_path,
                      {'form': form,
                       'district': district,
                       'num_visits': num_visits})


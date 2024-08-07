from users.models import CustomUser
from fishing_oracle.settings import DEFAULT_FROM_EMAIL, EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT, EMAIL_USE_TLS
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from fishing.models import Fishing, Priming
from fishing.models import Conditions
from fishing.models import Overcast
from fishing.models import Pace
from fishing.models import NozzleType
from fishing.models import FeedCapacity
from fishing.models import Fish
from fishing.models import WaterCategory
from fishing.forms import PrimingForm
from fishing.forms import ConditionsForm
from fishing.forms import OvercastForm
from fishing.forms import PaceForm
from fishing.forms import NozzleTypeForm
from fishing.forms import FeedCapacityForm
from fishing.forms import FishForm
from fishing.forms import WaterCategoryForm

from fishing.getinfo import siteinfo, getuserinfo

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

class Settings(View):
    """
    Страница администратора
    """
    template = 'fishing/settings/settings.html'
    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),})


class PrimingAdd(View):
    """
    Добавление варианта покрытия дна
    """
    template = 'fishing/settings/priming/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PrimingForm(request.POST)
        priming = Priming()
        if form.is_valid():
            priming = form.save(commit=False)
            priming.first_upper()
            priming.save()
            return redirect('fishing:primings')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = PrimingForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class PrimingList(View):
    """
    Возвращает список варинатов покрытия дна
    """

    template = 'fishing/settings/priming/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        primings_list = Priming.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'primings_list': primings_list})


class PrimingDelete(View):
    """
    Удаление варианта покрытия дна
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        priming = get_object_or_404(Priming, pk=kwargs['priming_id'])
        priming.delete()
        return redirect('fishing:primings')


class PrimingEdit(View):
    """
    Изменение варианта покрытия дна
    """
    template = 'fishing/settings/priming/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        priming = get_object_or_404(Priming, pk=kwargs['priming_id'])
        form = PrimingForm(request.POST, instance=priming)
        if form.is_valid():
            priming = form.save(commit=False)
            priming.first_upper()
            priming.save()
            return redirect('fishing:primings')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'priming': priming})

    def get(self, request, *args, **kwargs):
        priming = get_object_or_404(Priming, pk=kwargs['priming_id'])
        form = PrimingForm(instance=priming)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'priming': priming})


class ConditionsAdd(View):
    """
    Добавление варианта погодного явления
    """
    template = 'fishing/settings/conditions/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ConditionsForm(request.POST)
        conditions = Conditions()
        if form.is_valid():
            conditions = form.save(commit=False)
            conditions.first_upper()
            conditions.save()
            return redirect('fishing:conditions')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = ConditionsForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class ConditionsList(View):
    """
    Возвращает список варинатов погодных явлений
    """

    template = 'fishing/settings/conditions/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        conditions_list = Conditions.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'conditions_list': conditions_list})


class ConditionsDelete(View):
    """
    Удаление варианта погодного явления
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        conditions = get_object_or_404(Conditions, pk=kwargs['conditions_id'])
        conditions.delete()
        return redirect('fishing:conditions')


class ConditionsEdit(View):
    """
    Изменение варианта погодного явления
    """
    template = 'fishing/settings/conditions/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        conditions = get_object_or_404(Conditions, pk=kwargs['conditions_id'])
        form = ConditionsForm(request.POST, instance=conditions)
        if form.is_valid():
            conditions = form.save(commit=False)
            conditions.first_upper()
            conditions.save()
            return redirect('fishing:conditions')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'conditions': conditions})

    def get(self, request, *args, **kwargs):
        conditions = get_object_or_404(Conditions, pk=kwargs['conditions_id'])
        form = ConditionsForm(instance=conditions)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'conditions': conditions})


class OvercastAdd(View):
    """
    Добавление варианта облачности
    """
    template = 'fishing/settings/overcast/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = OvercastForm(request.POST)
        overcast = Overcast()
        if form.is_valid():
            overcast = form.save(commit=False)
            overcast.first_upper()
            overcast.save()
            return redirect('fishing:overcast')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = OvercastForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class OvercastList(View):
    """
    Возвращает список варинатов облачности
    """

    template = 'fishing/settings/overcast/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        overcast_list = Overcast.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'overcast_list': overcast_list})


class OvercastDelete(View):
    """
    Удаление варианта облачности
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        overcast = get_object_or_404(Overcast, pk=kwargs['overcast_id'])
        overcast.delete()
        return redirect('fishing:overcast')


class OvercastEdit(View):
    """
    Изменение варианта облачности
    """
    template = 'fishing/settings/overcast/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        overcast = get_object_or_404(Overcast, pk=kwargs['overcast_id'])
        form = OvercastForm(request.POST, instance=overcast)
        if form.is_valid():
            overcast = form.save(commit=False)
            overcast.save()
            return redirect('fishing:overcast')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'overcast': overcast})

    def get(self, request, *args, **kwargs):
        overcast = get_object_or_404(Overcast, pk=kwargs['overcast_id'])
        form = OvercastForm(instance=overcast)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'overcast': overcast})


class PaceAdd(View):
    """
    Добавление варианта темпа
    """
    template = 'fishing/settings/pace/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PaceForm(request.POST)
        pace = Pace()
        if form.is_valid():
            pace = form.save(commit=False)
            pace.first_upper()
            pace.save()
            return redirect('fishing:pace')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = PaceForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class PaceList(View):
    """
    Возвращает список варинатов темпа ловли
    """

    template = 'fishing/settings/pace/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pace_list = Pace.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'pace_list': pace_list})


class PaceDelete(View):
    """
    Удаление варианта темпа ловли
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        pace = get_object_or_404(Pace, pk=kwargs['pace_id'])
        pace.delete()
        return redirect('fishing:pace')


class PaceEdit(View):
    """
    Изменение варианта темпа ловли
    """
    template = 'fishing/settings/pace/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        pace = get_object_or_404(Pace, pk=kwargs['pace_id'])
        form = PaceForm(request.POST, instance=pace)
        if form.is_valid():
            pace = form.save(commit=False)
            pace.first_upper()
            pace.save()
            return redirect('fishing:pace')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'pace': pace})

    def get(self, request, *args, **kwargs):
        pace = get_object_or_404(Pace, pk=kwargs['pace_id'])
        form = PaceForm(instance=pace)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'pace': pace})


class NozzleTypeAdd(View):
    """
    Добавление типа насадки
    """
    template = 'fishing/settings/nozzletype/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = NozzleTypeForm(request.POST)
        nozzle_type = NozzleType()
        if form.is_valid():
            nozzle_type = form.save(commit=False)
            nozzle_type.first_upper()
            nozzle_type.save()
            return redirect('fishing:nozzle_type')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = NozzleTypeForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class NozzleTypeList(View):
    """
    Возвращает список типов насадок
    """

    template = 'fishing/settings/nozzletype/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle_type_list = NozzleType.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'nozzle_type_list': nozzle_type_list})


class NozzleTypeDelete(View):
    """
    Удаление типа насадки
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        nozzle_type = get_object_or_404(NozzleType, pk=kwargs['type_id'])
        nozzle_type.delete()
        return redirect('fishing:nozzle_type')


class NozzleTypeEdit(View):
    """
    Изменение типа насадки
    """
    template = 'fishing/settings/nozzletype/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        nozzle_type = get_object_or_404(NozzleType, pk=kwargs['type_id'])
        form = NozzleTypeForm(request.POST, instance=nozzle_type)
        if form.is_valid():
            nozzle_type = form.save(commit=False)
            nozzle_type.first_upper()
            nozzle_type.save()
            return redirect('fishing:nozzle_type')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'nozzle_type': nozzle_type})

    def get(self, request, *args, **kwargs):
        nozzle_type = get_object_or_404(NozzleType, pk=kwargs['type_id'])
        form = NozzleTypeForm(instance=nozzle_type)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'nozzle_type': nozzle_type})


class CapacityAdd(View):
    """
    Добавление варианта темпа
    """
    template = 'fishing/settings/capacity/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = FeedCapacityForm(request.POST)
        capacity = FeedCapacity()
        if form.is_valid():
            capacity = form.save(commit=False)
            capacity.first_upper()
            capacity.save()
            return redirect('fishing:feed_capacity')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = FeedCapacityForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class CapacityList(View):
    """
    Возвращает список варинатов кормоемкости
    """

    template = 'fishing/settings/capacity/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        capacity_list = FeedCapacity.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'capacity_list': capacity_list})


class CapacityDelete(View):
    """
    Удаление варианта кормоёмкости
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        capacity = get_object_or_404(FeedCapacity, pk=kwargs['capacity_id'])
        capacity.delete()
        return redirect('fishing:feed_capacity')


class CapacityEdit(View):
    """
    Изменение варианта кормоёмкости
    """
    template = 'fishing/settings/capacity/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        capacity = get_object_or_404(FeedCapacity, pk=kwargs['capacity_id'])
        form = FeedCapacityForm(request.POST, instance=capacity)
        if form.is_valid():
            capacity = form.save(commit=False)
            capacity.first_upper()
            capacity.save()
            return redirect('fishing:feed_capacity')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'capacity': capacity})

    def get(self, request, *args, **kwargs):
        capacity = get_object_or_404(FeedCapacity, pk=kwargs['capacity_id'])
        form = FeedCapacityForm(instance=capacity)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'capacity': capacity})


class FishAdd(View):
    """
    Добавление рыб
    """
    template = 'fishing/settings/fish/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form_fish = FishForm(request.POST)
        fish = Fish()
        if form_fish.is_valid():
            fish = form_fish.save(commit=False)
            fish.first_upper()
            fish.save()
            return redirect('fishing:settings_fish_list')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form_fish': form_fish,
                           'fish': fish})

    def get(self, request, *args, **kwargs):
        form_fish = FishForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form_fish': form_fish})


class FishList(View):
    """
    Возвращает список рыб
    """

    template = 'fishing/settings/fish/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fish_list = Fish.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'fish_list': fish_list})


class FishDelete(View):
    """
    Удаление рыбы
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fish = get_object_or_404(Fish, pk=kwargs['fish_id'])
        fish.delete()
        return redirect('fishing:settings_fish_list')


class FishEdit(View):
    """
    Изменение рыбы
    """
    
    template = 'fishing/settings/fish/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        fish = get_object_or_404(Fish, pk=kwargs['fish_id'])
        form_fish = FishForm(request.POST, instance=fish)
        if form_fish.is_valid():
            fish = form_fish.save(commit=False)
            fish.first_upper()
            fish.save()
            return redirect('fishing:settings_fish_list')
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form_fish': form_fish,
                           'fish': fish})

    def get(self, request, *args, **kwargs):
        fish = get_object_or_404(Fish, pk=kwargs['fish_id'])
        form_fish = FishForm(instance=fish)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form_fish': form_fish,
                       'fish': fish})


class FishDetails(View):
    """
    Возвращает подробную нинформацию о рыбе
    """

    template = 'fishing/settings/fish/details.html'

    def get(self, request, *args, **kwargs):
        fish_details = get_object_or_404(Fish, pk=kwargs['fish_id'])
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'fish': fish_details})


class WaterCategoryAdd(View):
    """
    Добавление категории водоема
    """
    template = 'fishing/settings/watercategory/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = WaterCategoryForm(request.POST)
        if form.is_valid():
            water_category = form.save(commit=False)
            if water_category.unique():
                water_category.first_upper()
                water_category.getabbreviation()
                if water_category.unique():
                    water_category.save()
                    return redirect('fishing:water_category')
                else:
                    return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Укажите аббревиатуру'})
            else:
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Такая категория водоёма или аббревиатура уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form})

    def get(self, request, *args, **kwargs):
        form = WaterCategoryForm()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form})


class WaterCategoryList(View):
    """
    Возвращает список категорий водоемов
    """

    template = 'fishing/settings/watercategory/list.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        water_category_list = WaterCategory.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'water_category_list': water_category_list})


class WaterCategoryDelete(View):
    """
    Удаление категории водоема
    """

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        water_category = get_object_or_404(WaterCategory, pk=kwargs['water_category_id'])
        water_category.delete()
        return redirect('fishing:water_category')


class WaterCategoryEdit(View):
    """
    Изменение катеогории водоёма
    """
    template = 'fishing/settings/watercategory/renewal_add.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        water_category = get_object_or_404(WaterCategory, pk=kwargs['water_category_id'])
        form = WaterCategoryForm(request.POST, instance=water_category)
        if form.is_valid():
            water_category = form.save(commit=False)
            if water_category.unique():
                water_category.first_upper()
                water_category.getabbreviation()
                water_category.save()
                return redirect('fishing:water_category')
            return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'water_category': water_category,
                               'errors': 'Такая категория водоёма или аббревиатура уже добавлена'})
        else:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'water_category': water_category})

    def get(self, request, *args, **kwargs):
        water_category = get_object_or_404(WaterCategory, pk=kwargs['water_category_id'])
        form = WaterCategoryForm(instance=water_category)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'form': form,
                       'water_category': water_category})


class EnvironmentVariables(View):
    
    template = 'fishing/settings/environment.html'
    
    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        result = {'result': []}
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'environments': result})


class UsersList(View):
    """
    Описание класса
    """

    template = 'fishing/settings/users.html'

    @method_decorator(staff_member_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        result = {'nick': [],
                  'email': [],
                  'date_joined':[],
                  'fishings': []}
        users = CustomUser.objects.all()
        for user in users:
            if not user.is_staff:
                result['nick'].append(str(user.nick))
                result['email'].append(str(user.email))
                result['date_joined'].append(user.date_joined)
                fishings = Fishing.objects.filter(owner=user)
                result['fishings'].append(len(fishings))
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'users': result})

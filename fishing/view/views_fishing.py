import fishing
from django.shortcuts import get_object_or_404, resolve_url
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from random import randint
import datetime

from fishing.models import Aroma, FeedCapacity, Fishing, Lure, Nozzle, NozzleType, Water, WaterCategory
from fishing.models import Place
from fishing.models import FishingPlace
from fishing.models import Weather
from fishing.models import FishingWeather
from fishing.models import Overcast
from fishing.models import Conditions
from fishing.models import Tackle
from fishing.models import FishingTackle
from fishing.models import Montage
from fishing.models import FishingMontage
from fishing.models import Trough
from fishing.models import FishingTrough
from fishing.models import Leash
from fishing.models import FishingLeash
from fishing.models import Crochet
from fishing.models import FishingCrochet
from fishing.models import NozzleBase
from fishing.models import FishingNozzle
from fishing.models import Pace
from fishing.models import FishingPace
from fishing.models import LureMix
from fishing.models import LureBase
from fishing.models import FishingLureMix
from fishing.models import FishingResult
from fishing.models import FishingTrophy
from fishing.models import FishingLure
from fishing.models import Fish
from fishing.models import FishingReportsSettings

from fishing.forms import AromaBaseForm, AromaForm, BaitBaseForm, CrochetForm, FishingForm, FishingNozzleForm, LeashForm, LureBaseForm, LureForm, LureMixForm, MontageForm, NozzleBaseForm, NozzleStateForm, PlaceFullForm, TackleForm, TroughForm, WaterForm
from fishing.forms import WeatherForm
from fishing.forms import FishingResultForm
from fishing.forms import FishingTrophyForm
from fishing.forms import FishingLureForm
from fishing.forms import FishingNoteForm
from fishing.forms import FishingReportsSettingsForm

from fishing.getinfo import siteinfo, getuserinfo

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class FishingList(View):
    """
    Возвращает список рыбалок пользователя
    """
    
    template = 'fishing/notes/fishing/list.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing_list = Fishing.objects.filter(owner=request.user)
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'fishing_list': fishing_list})


class FishingAdd(View):
    """
    Добавляет рыбалку пользователю
    """
    
    template = 'fishing/notes/fishing/edit_add.html'
    
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(FishingAdd, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = FishingForm(request.POST)
        if form.is_valid():
            fishing = form.save(commit=False)
            fishing.owner = request.user
            fishing.set_planned()
            if fishing.unique():
                fishing.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                return render(self.request,
                              self.template,
                              {'fisherman': getuserinfo(self.request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'errors': 'Рыбалка на эти дату и время уже добавлена'})
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form})
    
    def get(self, request, *args, **kwargs):
        fishing = Fishing()
        fishing.date = datetime.date.today()
        time = datetime.datetime.now()
        fishing.time_start = time.strftime("%H:%M")
        fishing.time_end = time.strftime("%H:%M")
        form = FishingForm(instance=fishing)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'form': form})


class FishingDelete(View):
    """
    Удаляет рыбалку
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            if fishing.report:
                fishint_report_settings = FishingReportsSettings.objects.get(fishing=fishing.id)
                fishint_report_settings.delete()
            fishing.delete()
        return redirect('fishing:fishing')


class FishingEdit(View):
    """
    Редактирует дату и время рыбалки
    """
    template = 'fishing/notes/fishing/edit_add.html'
    
    def dispatch(self, *args, **kwargs):
        return super(FishingEdit, self).dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = FishingForm(self.request.POST, instance=fishing)
            if form.is_valid():
                fishing = form.save(commit=False)
                fishing.set_planned()
                if fishing.unique():
                    fishing.save()
                    return redirect('fishing:fishing')
                else:
                    return render(self.request,
                                self.template,
                                {'fisherman': getuserinfo(self.request),
                                 'siteinfo': siteinfo(),
                                 'form': form,
                                 'fishing': fishing,
                                 'errors': 'Рыбалка на эти дату и время уже добавлена'})
            else:
                return render(self.request,
                            self.template,
                            {'fisherman': getuserinfo(self.request),
                             'siteinfo': siteinfo(),
                             'form': form,
                             'fishing': fishing})
        else:
            return redirect('fishing:fishing')
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = FishingForm(instance=fishing)
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                         'siteinfo': siteinfo(),
                         'form': form,
                         'fishing': fishing})
        else:
            return redirect('fishing:fishing')


class FishingDetails(View):
    """
    Возвращает подробное описание рыбалки
    """
    
    template = 'fishing/notes/fishing/details.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingDetails, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            try:
                fishing_report_settings = FishingReportsSettings.objects.get(fishing_id=fishing.id)
                fishing_report_settings = True
            except:
                fishing_report_settings = False
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishing_trophy': fishing.get_trophy(),
                           'fishing_report_settings': fishing_report_settings,
                           'fishing': fishing,
                           'details': fishing.get_details()})
        else:
            return redirect('fishing:fishing')


class FishingReportSetingsView(View):
    """
    Настройка отчета, изменение отображаемых элементов
    """
    
    template = 'fishing/notes/fishing/report_settings.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_self_id(self, *args, **kwargs):
        while (True):
            self_id = FishingReportsSettings.generate_self_id()
            try:
                FishingReportsSettings.objects.get(self_id=self_id)
            except:
                break
        return self_id
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            try:
                fishing_report_settings = FishingReportsSettings.objects.get(fishing_id=fishing.id)
                form = FishingReportsSettingsForm(instance=fishing_report_settings)
            except:
                form = FishingReportsSettingsForm()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'fishing': fishing})
        return redirect('fishing:fishing')
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            try:
                fishing_report_settings = FishingReportsSettings.objects.get(fishing_id=fishing.id)
                form = FishingReportsSettingsForm(request.POST, instance=fishing_report_settings)
            except:
                fishing_report_settings = FishingReportsSettings()
                form = FishingReportsSettingsForm(request.POST)
            if form.is_valid():
                fishing_report_settings = form.save(commit=False)
                if not fishing_report_settings.fishing_id:
                    fishing_report_settings.fishing_id = fishing.id
                    fishing_report_settings.self_id = FishingReportsSettings.get_self_id()
                    fishing.report = request.build_absolute_uri(reverse('fishing:fishing_report', args=(fishing_report_settings.self_id, )))
                    fishing.save()
                fishing_report_settings.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'fishing': fishing})
        return redirect('fishing:fishing')


class FishingReportsSettingsDelete(View):
    """
    Удаляет отчет по рыбалке рыбалку
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            fishing_report_settings = get_object_or_404(FishingReportsSettings, fishing_id=fishing.id)
            fishing_report_settings.delete()
            fishing.report = ''
            fishing.save()
        return redirect('fishing:fishing_details', fishing.id)


class FishingPlaceSelect(View):
    """
    Возвращает страницу выбора со списком мест
    """
    template = 'fishing/notes/fishing/place/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPlaceSelect, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        place_list = Place.objects.filter(owner=self.request.user)
        if fishing.owner == self.request.user:
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'place_list': place_list})
        return redirect('fishing:fishing')


class FishingPlaceAdd(View):
    """
    Добавляет выбранное место в рыбалке
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        place = get_object_or_404(Place, pk=kwargs['place_id'])
        if (fishing.owner and place.owner) == self.request.user:
            try:
                fishing_place = FishingPlace.objects.get(fishing=fishing)
            except FishingPlace.DoesNotExist:
                fishing_place = FishingPlace()
                fishing_place.owner = self.request.user
                fishing_place.fishing = fishing
            fishing_place.place = place
            fishing_place.save()
            return redirect('fishing:fishing_details', fishing.id)
        return redirect('fishing:fishing')


class FishingPlaceWaterSelect(View):
    
    template = 'fishing/notes/fishing/place/water/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        water_list = Water.objects.filter(owner=self.request.user)
        return render(self.request,
                self.template,
                {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id': kwargs['fishing_id'],
                 'water_list': water_list})


class FishingPlaceWaterAdd(View):
    
    template = 'fishing/notes/fishing/place/water/add.html'
    @method_decorator(login_required)
    def dispatch(self,*args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            result = WaterForm.save_me(self.request)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_place_water_place_add', kwargs['fishing_id'], result)
            else:
                watercategorys = WaterCategory.objects.all()
                return render(self.request,
                            self.template,
                            {'fisherman': getuserinfo(self.request),
                            'siteinfo': siteinfo(),
                            'watercategorys': watercategorys,
                            'fishing_id': kwargs['fishing_id'],
                            'form': result})
        return redirect('fishing:fishing_details', fishing.id)
    
    def get (self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = WaterForm()
            watercategorys = WaterCategory.objects.all()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'watercategorys': watercategorys,
                           'form': form})
        return redirect('fishing:fishing_details', fishing.id)


class FishingPlaceWaterPlaceAdd(View):
    
    template = 'fishing/notes/fishing/place/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if fishing.owner == self.request.user and water.owner == self.request.user:
            result = PlaceFullForm.save_me(self.request, water=water)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_place_add', kwargs['fishing_id'], result)
            else:
                return render(self.request,
                            self.template,
                            {'fisherman': getuserinfo(self.request),
                            'siteinfo': siteinfo(),
                            'water_id': kwargs['water_id'],
                            'fishing_id': kwargs['fishing_id'],
                            'form': result})
        return redirect('fishing:fishing_details', fishing.id)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        water = get_object_or_404(Water, pk=kwargs['water_id'])
        if fishing.owner == self.request.user and water.owner == self.request.user:
            form = PlaceFullForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'water_id': kwargs['water_id'],
                           'fishing_id': kwargs['fishing_id']})
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingPlaceDelete(View):
    """
    Удаляет место из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPlaceDelete, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_place = FishingPlace.objects.get(fishing=fishing)
            except:
                return redirect('fishing:fishing')
            fishing_place.delete()
        return redirect('fishing:fishing_details', fishing.id)


class FishingWeatherDelete(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingWeatherDelete, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_weather = FishingWeather.objects.get(fishing=fishing)
            except:
                return redirect('fishing:fishing')
            weather = fishing_weather.weather
            fishing_weather.delete()
            weather.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingWeatherAdd(View):
    """
    Добавляет информацию о погоде в рыбалку (ручной ввод)
    """
    
    template = 'fishing/notes/fishing/edit_add_weather.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingWeatherAdd, self).dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_weather = FishingWeather.objects.get(fishing=fishing)
                weather = fishing_weather.weather
                form = WeatherForm(self.request.POST, instance=weather)
                new_weather = False
            except:
                form = WeatherForm(self.request.POST)
                new_weather = True
            if form.is_valid():
                weather = form.save(commit=False)
                weather.date = fishing.date
                weather.save()
                if new_weather:
                    fishing_weather = FishingWeather()
                    fishing_weather.owner = self.request.user
                    fishing_weather.fishing = fishing
                    fishing_weather.weather = weather
                    fishing_weather.save()
                return redirect('fishing:fishing_details', fishing.id)
            overcasts = Overcast.objects.all()
            conditions = Conditions.objects.all()
            return render(self.request,
                        self.template,
                        {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'overcasts': overcasts,
                        'conditions': conditions,
                        'form': form,
                        'fishing_id': kwargs['fishing_id']})
        return redirect('fishing:fishing')
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_weather = FishingWeather.objects.get(fishing=fishing)
                weather = fishing_weather.weather
                form = WeatherForm(instance=weather)
            except:
                form = WeatherForm()
            overcasts = Overcast.objects.all()
            conditions = Conditions.objects.all()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'overcasts': overcasts,
                           'conditions': conditions,
                           'form': form,
                           'fishing_id': kwargs['fishing_id']})
        return redirect('fishing:fishing')


class FishingTackleSelect(View):
    """
    Возращает список снастей для выбора
    """
    
    template = 'fishing/notes/fishing/tackle/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTackleSelect, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            tackle_list = Tackle.objects.filter(owner=request.user)
            if kwargs['fishing_tackle_id'] != 0:
                fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
            else:
                fishing_tackle = FishingTackle()
                fishing_tackle.id = 0
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishing': fishing,
                           'fishing_tackle': fishing_tackle,
                           'tackle_list': tackle_list})
        return redirect('fishing:fishing')


class FishingTackleAdd(View):
    """
    Добавляет выбраную снасть в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTackleAdd, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        tackle = get_object_or_404(Tackle, pk=kwargs['tackle_id'])
        fishing_tackle_id = kwargs['fishing_tackle_id']
        if fishing.owner == request.user and tackle.owner == fishing.owner:
            if fishing_tackle_id != 0:
                fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
            else:
                fishing_tackle = FishingTackle()
                fishing_tackle.owner = request.user
                fishing_tackle.fishing = fishing
            fishing_tackle.tackle = tackle
            fishing_tackle.save()
            return redirect('fishing:fishing_details', fishing.id)
        return redirect('fishing:fishing')


class FishingNewTackleAdd(View):

    template = 'fishing/notes/fishing/tackle/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = TackleForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_tackle_add', kwargs['fishing_id'], result, kwargs['fishing_tackle_id'])
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = TackleForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': form})
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingTackleDelete(View):
    """
    Удаляет снасть из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTackleDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if fishing_tackle.owner == request.user:
            fishing_tackle.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingMontageSelect(View):
    """
    Возращает список монтажей для выбора
    """
    
    template = 'fishing/notes/fishing/montage/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingMontageSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing.owner and fishing_tackle.owner) == self.request.user:
            montage_list = Montage.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'montage_list': montage_list})
        return redirect('fishing:fishing')


class FishingMontageAdd(View):
    """
    Добавляет выбраный монтаж в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingMontageAdd, self).dispatch(*args, **kwargs)
    
    def get(self,  *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        montage = get_object_or_404(Montage, pk=kwargs['montage_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing.owner and montage.owner and fishing_tackle.owner) == self.request.user:
            try:
                fishing_montage = get_object_or_404(FishingMontage, fishing_tackle=fishing_tackle)
            except:
                fishing_montage = FishingMontage()
                fishing_montage.owner = self.request.user
                fishing_montage.fishing_tackle = fishing_tackle
            fishing_montage.montage = montage
            fishing_montage.save()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingNewMontageAdd(View):

    template = 'fishing/notes/fishing/montage/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = MontageForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_montage_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result)
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = MontageForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': form})
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingMontageDelete(View):
    """
    Удаляет монтаж из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingMontageDelete, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        
        if (fishing_tackle.fishing == fishing) and (fishing.owner and fishing_tackle.owner) == self.request.user:
            try:
                fishing_montage = FishingMontage.objects.get(fishing_tackle=fishing_tackle)
            except:
                return redirect('fishing:fishing')
            fishing_montage.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingTroughSelect(View):
    """
    Возращает список кормушек для выбора
    """
    
    template = 'fishing/notes/fishing/trough/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTroughSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner and fishing_tackle.owner) == self.request.user:
            trough_list = Trough.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'trough_list': trough_list})
        return redirect('fishing:fishing')


class FishingNewTroughAdd(View):

    template = 'fishing/notes/fishing/trough/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = TroughForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_trough_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result)
        else:
            feedcapacitys = FeedCapacity.objects.all()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'feedcapacitys': feedcapacitys,
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            feedcapacitys = FeedCapacity.objects.all()
            form = TroughForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'feedcapacitys': feedcapacitys,
                           'form': form})
        return redirect('fishing:fishing')


class FishingTroughAdd(View):
    """
    Добавляет выбраную кормушку в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTroughAdd, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        trough = get_object_or_404(Trough, pk=kwargs['trough_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner and trough.owner) == fishing.owner:
            try:
                fishing_trough = FishingTrough.objects.get(fishing_tackle=fishing_tackle)
            except:
                fishing_trough = FishingTrough()
                fishing_trough.owner = request.user
                fishing_trough.fishing_tackle = fishing_tackle
            fishing_trough.trough = trough
            fishing_trough.save()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingTroughDelete(View):
    """
    Удаляет кормушку из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTroughDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_trough = FishingTrough.objects.get(fishing_tackle=fishing_tackle)
            except:
                return redirect('fishing:fishing')
            fishing_trough.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingLeashSelect(View):
    """
    Возращает список поводков для выбора
    """
    
    template = 'fishing/notes/fishing/leash/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLeashSelect, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            leash_list = Leash.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'leash_list': leash_list})
        return redirect('fishing:fishing')


class FishingNewLeashAdd(View):

    template = 'fishing/notes/fishing/leash/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = LeashForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_leash_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result)
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            form = LeashForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': form})


class FishingLeashAdd(View):
    """
    Добавляет выбраный поводок в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLeashAdd, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        leash = get_object_or_404(Leash, pk=kwargs['leash_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner and leash.owner) == self.request.user:
            try:
                fishing_leash = FishingLeash.objects.get(fishing_tackle=fishing_tackle)
            except:
                fishing_leash = FishingLeash()
                fishing_leash.owner = self.request.user
                fishing_leash.fishing_tackle = fishing_tackle
            fishing_leash.leash = leash
            fishing_leash.save()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingLeashDelete(View):
    """
    Удаляет поводок из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLeashDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and fishing.owner == self.request.user:
            try:
                fishing_leash = FishingLeash.objects.get(fishing_tackle=fishing_tackle)
            except:
                return redirect('fishing:fishing')
            fishing_leash.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingCrochetSelect(View):
    """
    Возращает список крючков для выбора
    """
    
    template = 'fishing/notes/fishing/crochet/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingCrochetSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            crochet_list = Crochet.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'crochet_list': crochet_list})
        return redirect('fishing:fishing')


class FishingNewCrochetAdd(View):

    template = 'fishing/notes/fishing/crochet/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = CrochetForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_crochet_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result)
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fisihng_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fisihng_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            form = CrochetForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'form': form})


class FishingCrochetAdd(View):
    """
    Добавляет выбраный крючок в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingCrochetAdd, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        crochet = get_object_or_404(Crochet, pk=kwargs['crochet_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner and crochet.owner) == request.user and crochet.owner == fishing.owner:
            try:
                fishing_crochet = FishingCrochet.objects.get(fishing_tackle=fishing_tackle)
            except:
                fishing_crochet = FishingCrochet()
                fishing_crochet.owner = request.user
                fishing_crochet.fishing_tackle = fishing_tackle
            fishing_crochet.crochet = crochet
            fishing_crochet.save()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingCrochetDelete(View):
    """
    Удаляет крючок из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingCrochetDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_crochet = FishingCrochet.objects.get(fishing_tackle=fishing_tackle)
            except:
                return redirect('fishing:fishing')
            fishing_crochet.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingNozzleSelect(View):
    """
    Возращает список наживок/насадок для выбора
    """
    
    template = 'fishing/notes/fishing/nozzle/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingNozzleSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and fishing.owner == self.request.user:
            nozzle_base_list = NozzleBase.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_list': nozzle_base_list,
                           'nozzle_position': kwargs['nozzle_position']})
        return redirect('fishing:fishing')


class FishingNewNozzleAdd(View):

    template = 'fishing/notes/fishing/nozzle/add_nozzle.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        
        result = NozzleBaseForm.save_me(self.request)
        if isinstance(result, int):
            return redirect('fishing:fishing_nozzle_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result, kwargs['fishing_nozzle_id'])
        else:
            nozzletypes = NozzleType.objects.all()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_position':kwargs['nozzle_position'],
                           'nozzletypes': nozzletypes,
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            form = NozzleBaseForm()
            nozzletypes = NozzleType.objects.all()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_position':kwargs['nozzle_position'],
                           'nozzletypes': nozzletypes,
                           'form': form})


class FishingNewBaitAdd(View):

    template = 'fishing/notes/fishing/nozzle/add_bait.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = BaitBaseForm.save_me(self.request)
        if isinstance(result, int):
            return redirect('fishing:fishing_nozzle_add', kwargs['fishing_id'], kwargs['fishing_tackle_id'], result, kwargs['fishing_nozzle_id'])
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_position':kwargs['nozzle_position'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            form = BaitBaseForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_position':kwargs['nozzle_position'],
                           'form': form})


class FishingNozzleAdd(View):
    """
    Выбор состояния наживки и её количества и окончательное доавбление в снасти
    """

    template = 'fishing/notes/fishing/nozzle/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_nozzle = FishingNozzle.objects.get(fishing_tackle=fishing_tackle, position=kwargs['nozzle_position'])
                form = FishingNozzleForm(self.request.POST, instance=fishing_nozzle)
            except:
                fishing_nozzle = FishingNozzle()
                form = FishingNozzleForm(self.request.POST)
            if form.is_valid():
                fishing_nozzle = form.save(commit=False)
                fishing_nozzle.owner = self.request.user
                fishing_nozzle.fishing_tackle = fishing_tackle
                fishing_nozzle.nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_id'])
                fishing_nozzle.set_position()
                fishing_nozzle.save()
                return redirect('fishing:fishing_details', kwargs['fishing_id'])
            else:
                fishing_nozzle.owner = self.request.user
                fishing_nozzle.fishing_tackle = fishing_tackle
                fishing_nozzle.nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_id'])
                nozzle_states = fishing_nozzle.get_nozzle_state_list()
                return render(self.request,
                              self.template,
                              {'fisherman': getuserinfo(self.request),
                               'siteinfo': siteinfo(),
                               'fishing_id': kwargs['fishing_id'],
                               'nozzle_position': kwargs['nozzle_position'],
                               'fishing_tackle_id': kwargs['fishing_tackle_id'],
                               'nozzle_id': kwargs['nozzle_id'],
                               'nozzle_states': nozzle_states,
                               'form': form})
        return redirect('fishing:fishing')

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_nozzle = FishingNozzle.objects.get(fishing_tackle=fishing_tackle, position=kwargs['nozzle_position'])
                form = FishingNozzleForm(instance=fishing_nozzle)
            except:
                fishing_nozzle = FishingNozzle()
                fishing_nozzle.owner = self.request.user
                fishing_nozzle.fishing_tackle = fishing_tackle
                form = FishingNozzleForm()
            fishing_nozzle.nozzle_base = get_object_or_404(NozzleBase, pk=kwargs['nozzle_id'])            
            nozzle_states = fishing_nozzle.get_nozzle_state_list()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'nozzle_position': kwargs['nozzle_position'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'nozzle_id': kwargs['nozzle_id'],
                           'nozzle_states': nozzle_states,
                           'form': form})
        return redirect('fishing:fishing')


class FishingNozzleDelete(View):
    """
    Удаляет наживку/насадку из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingNozzleDelete, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_nozzle = FishingNozzle.objects.get(fishing_tackle=fishing_tackle, position=kwargs['nozzle_position'])
            except:
                return redirect('fishing:fishing')
            fishing_nozzle.delete()
            fishing_nozzle.position_reindexing()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingPaceSelect(View):
    """
    Возращает список темпов для выбора
    """
    
    template = 'fishing/notes/fishing/pace/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPaceSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            pace_list = Pace.objects.all
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'fishing_tackle_id': kwargs['fishing_tackle_id'],
                           'pace_list': pace_list})
        return redirect('fishing:fishing')


class FishingPaceAdd(View):
    """
    Добавляет выбраный темп в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPaceAdd, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        pace = get_object_or_404(Pace, pk=kwargs['pace_id'])
        if (fishing_tackle.fishing == fishing) and  fishing.owner == self.request.user:
            try:
                fishing_pace = FishingPace.objects.get(fishing_tackle=fishing_tackle)
            except:
                fishing_pace = FishingPace()
                fishing_pace.owner = self.request.user
                fishing_pace.fishing_tackle = fishing_tackle
            fishing_pace.pace = pace
            fishing_pace.save()
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingPaceDelete(View):
    """
    Удаляет темп из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingPaceDelete, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_tackle = get_object_or_404(FishingTackle, pk=kwargs['fishing_tackle_id'])
        if (fishing_tackle.fishing == fishing) and (fishing.owner == self.request.user):
            try:
                fishing_pace = FishingPace.objects.get(fishing_tackle=fishing_tackle)
            except:
                return redirect('fishing:fishing')
            fishing_pace.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingLureDelete(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request,*args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            try:
                fishing_lure = FishingLure.objects.get(fishing=fishing)
            except:
                return redirect('fishing:fishing')
            fishing_lure.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingLureSelect(View):
    """
    Выбор прикорма для рыбалки
    """
    
    template = 'fishing/notes/fishing/lure/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            lure_base_list = LureBase.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'lure_base_list': lure_base_list})
        return redirect('fishing:fishing')


class FishingNewLureAdd(View):

    template = 'fishing/notes/fishing/lure/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = LureBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_lure_change_weight', kwargs['fishing_id'], result, 0)
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = LureBaseForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'form': form})


class FishingLureChangeWeight(View):
    
    template = 'fishing/notes/fishing/lure/weight.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_lure = FishingLure.objects.get(fishing=fishing)
                form = FishingLureForm(instance=fishing_lure)
            except:
                form = FishingLureForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'form': form})
        return redirect('fishing:fishing')
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            try:
                fishing_lure = FishingLure.objects.get(fishing=fishing)
                form = FishingLureForm(self.request.POST, instance=fishing_lure)
            except:
                form = FishingLureForm(self.request.POST)
            if form.is_valid():
                fishing_lure = form.save(commit=False)
                fishing_lure.owner = self.request.user
                fishing_lure.fishing = fishing
                lure_base = get_object_or_404(LureBase, pk=kwargs['lure_base_id'])
                if lure_base.owner == self.request.user:
                    fishing_lure.lure_base = lure_base
                    fishing_lure.save()
                    return redirect('fishing:fishing_details', fishing.id)
                else:
                    return redirect('fishing:fishing')
            else:
                return render(self.request,
                              self.template,
                              {'fisherman': getuserinfo(self.request),
                               'siteinfo': siteinfo(),
                               'form': form,
                               'fishing_id': kwargs['fishing_id']})
        return redirect('fishing:fishing')


class FishingLureMixSelect(View):
    """
    Возращает список прикормочных смесей для выбора
    """
    
    template = 'fishing/notes/fishing/luremix/select.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLureMixSelect, self).dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            lure_mix_list = LureMix.objects.filter(owner=self.request.user)
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing': fishing,
                           'lure_mix_list': lure_mix_list})
        return redirect('fishing:fishing')


class FishingNewLureMixAdd(View):

    template = 'fishing/notes/fishing/luremix/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        result = LureMixForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            result = FishingLureMix.save_me(fishing_id=kwargs['fishing_id'], lure_mix_id=result, user=self.request.user)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])
            return redirect('fishing:fishing')

            
        else:
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'form': result})

    def get(self, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == self.request.user:
            form = LureMixForm()
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'fishing_id': kwargs['fishing_id'],
                           'form': form})


class FishingNewLureMixFilling(View):

    template = 'fishing/notes/fishing/luremix/filling.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'fishing_id': kwargs['fishing_id'],
                       'lure_mix': lure_mix})


class FishingNewLureMixFillingLureSelect(View):
    template = 'fishing/notes/fishing/luremix/lure/select.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id']}
        param.update(lure_mix.lure_for_add())
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingLureWeight(View):

    template = 'fishing/notes/fishing/luremix/lure/weight.html'
    edit = None
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        try:
            result = LureForm.save_me(self.request, fishing_id=kwargs['fishing_id'], lure_id=kwargs['lure_id'])
        except KeyError:
            result = LureForm.save_me(self.request, fishing_id=kwargs['fishing_id'], lure_base_id=kwargs['lure_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'form': result,
                 'edit': self.edit}
        return render(self.request,
                      self.template,
                      param)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'edit': self.edit}
        try:
            lure = Lure.objects.get(id=kwargs['lure_id'])
            form = LureForm(instance=lure)
        except:
            form = LureForm()
        param['form'] = form
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingLureDelete(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        lure = get_object_or_404(Lure, pk=kwargs['lure_id'])
        if lure.owner == self.request.user:
            lure.delete()
        return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])


class FishingNewLureMixFillingLureNew(View):
    """
    Описание класса
    """

    template = 'fishing/notes/fishing/luremix/lure/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        result = LureBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_new_lure_mix_filling_lure_weight', kwargs['fishing_id'], result)
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'form': result}
        return render(self.request,
                      self.template,
                      param)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id']}
        form = LureBaseForm()
        param['form'] = form
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingAromaSelect(View):
    template = 'fishing/notes/fishing/luremix/aroma/select.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id']}
        param.update(lure_mix.aroma_for_add())
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingAromaVolume(View):

    template = 'fishing/notes/fishing/luremix/aroma/volume.html'
    edit = None
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        try:
            result = AromaForm.save_me(self.request, fishing_id=kwargs['fishing_id'], aroma_id=kwargs['aroma_id'])
        except KeyError:
            result = AromaForm.save_me(self.request, fishing_id=kwargs['fishing_id'], aroma_base_id=kwargs['aroma_base_id'])
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'form': result,
                 'edit': self.edit}
        return render(self.request,
                      self.template,
                      param)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'edit': self.edit}
        try:
            lure = Aroma.objects.get(id=kwargs['aroma_id'])
            form = AromaForm(instance=lure)
        except:
            form = AromaForm()
        param['form'] = form
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingAromaDelete(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        aroma = get_object_or_404(Aroma, pk=kwargs['aroma_id'])
        if aroma.owner == self.request.user:
            aroma.delete()
        return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])


class FishingNewLureMixFillingAromaNew(View):
    """
    Описание класса
    """

    template = 'fishing/notes/fishing/luremix/aroma/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        result = AromaBaseForm.save_me(self.request)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_new_lure_mix_filling_aroma_volume', kwargs['fishing_id'], result)
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id'],
                 'form': result}
        return render(self.request,
                      self.template,
                      param)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id' : kwargs['fishing_id']}
        form = AromaBaseForm()
        param['form'] = form
        return render(self.request,
                      self.template,
                      param)


class FishingNewLureMixFillingNozzleSelect(View):
    template = 'fishing/notes/fishing/luremix/nozzle/select.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            nozzle_base_list = NozzleBase.objects.filter(owner=lure_mix.owner)
        param = {'fisherman': getuserinfo(self.request),
                'siteinfo': siteinfo(),
                'fishing_id' : kwargs['fishing_id'],
                'nozzle_base_list': nozzle_base_list}
        return render(self.request,
                    self.template,
                    param)


class FishingNewLureMixFillingNozzleNew(View):

    template = 'fishing/notes/fishing/luremix/nozzle/nozzle_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            result = NozzleBaseForm.save_me(self.request)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_new_lure_mix_filling_nozzle_state_select', kwargs['fishing_id'], result)
            param = {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'fishing_id': kwargs['fishing_id']}
            param['form'] = result
            param['nozzletypes'] = NozzleType.objects.all()
            return render(self.request,
                          self.template, 
                          param)
        return redirect('fishing:fishing_deatails', kwargs['fishing_id'])

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'fishing_id': kwargs['fishing_id']}
            param['form'] = NozzleBaseForm()
            param['nozzletypes'] = NozzleType.objects.all()
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:fishing_deatails', kwargs['fishing_id'])


class FishingNewLureMixFillingBaitNew(View):

    template = 'fishing/notes/fishing/luremix/nozzle/bait_add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            result = BaitBaseForm.save_me(self.request)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_new_lure_mix_filling_nozzle_state_select', kwargs['fishing_id'], result)
            param = {'fisherman': getuserinfo(self.request),
                        'siteinfo': siteinfo(),
                        'fishing_id': kwargs['fishing_id']}
            param['form'] = result
            return render(self.request,
                          self.template, 
                          param)
        return redirect('fishing:fishing_deatails', kwargs['fishing_id'])

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'fishing_id': kwargs['fishing_id']}
            param['form'] = BaitBaseForm()
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:fishing_deatails', kwargs['fishing_id'])


class FishingNewLureMixFillingNozzleStateSelect(View):
    template = 'fishing/notes/fishing/luremix/nozzle/state/select.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        param = {'fisherman': getuserinfo(self.request),
                 'siteinfo': siteinfo(),
                 'fishing_id': kwargs['fishing_id'],
                 'nozzle_base_id': kwargs['nozzle_base_id']}
        if lure_mix.owner == self.request.user:
            param.update(lure_mix.state_for_select(nozzle_base_id=kwargs['nozzle_base_id']))
        return render(self.request,
                    self.template,
                    param)


class FishingNewLureMixFillingNozzleStateNew(View):
    template = 'fishing/notes/fishing/luremix/nozzle/state/add.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            result = NozzleStateForm.save_me(self.request)
            if str(type(result)) == str(type(1)):
                return redirect('fishing:fishing_new_lure_mix_filling_nozzle_add', kwargs['fishing_id'], kwargs['nozzle_base_id'], result)
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'fishing_id': kwargs['fishing_id'],
                     'nozzle_base_id': kwargs['nozzle_base_id']}
            param['form'] = result
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:fishing_details', kwargs['fishing_id'])
        
    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(fishing_id=kwargs['fishing_id'], user=self.request.user)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if lure_mix.owner == self.request.user:
            param = {'fisherman': getuserinfo(self.request),
                     'siteinfo': siteinfo(),
                     'fishing_id': kwargs['fishing_id'],
                     'nozzle_base_id': kwargs['nozzle_base_id']}
            param['form'] = NozzleStateForm()
            return render(self.request,
                          self.template,
                          param)
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingNewLureMixFillingNozzleAdd(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        lure_mix = Fishing.get_luremix(user=self.request.user, **kwargs)
        if not lure_mix or not lure_mix.editable():
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        result = Nozzle.save_me(user=self.request.user, **kwargs)
        if result:
            return redirect('fishing:fishing_new_lure_mix_filling', kwargs['fishing_id'])
        return render(self.request,
                      self.template)


class FishingLureMixAdd(View):
    """
    Добавляет выбраную прикормочную смесь в рыбалку
    """

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLureMixAdd, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        result = FishingLureMix.save_me(user=self.request.user, **kwargs)
        if str(type(result)) == str(type(1)):
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        return redirect('fishing:fishing')


class FishingLureMixDelete(View):
    """
    Удаляет темп из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingLureMixDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        try:
            fishing = Fishing.objects.get(id=kwargs['fishing_id'])
            fishing_lure_mix = FishingLureMix.objects.get(fishing=fishing)
        except:
            return redirect('fishing:fishing_details', kwargs['fishing_id'])
        if fishing_lure_mix.owner == self.request.user:
            fishing_lure_mix.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingResultAdd(View):
    """
    Добавляет результат рыбалки
    """

    template = 'fishing/notes/fishing/edit_add_fishing_result.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingResultAdd, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingResultForm(request.POST)
            if form.is_valid():
                fishing_result = form.save(commit=False)
                fishing_result.owner = request.user
                fishing_result.fishing = fishing
                fishing_result.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                fishs = fishing.get_fish_for_result()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'fishs': fishs,
                               'form': form,
                               'fishing': fishing})
        return redirect('fishing:fishing')
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingResultForm()
            fishs = fishing.get_fish_for_result()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishs': fishs,
                           'form': form,
                           'fishing': fishing})
        return redirect('fishing:fishing')


class FishingResultDelete(View):
    """
    Удаляет улов из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingResultDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing_result = get_object_or_404(FishingResult, pk=kwargs['fishing_result_id'])
        if fishing_result.owner == request.user:
            fishing_result.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingResultEdit(View):
    """
    Редактирует результат рыбалки
    """

    template = 'fishing/notes/fishing/edit_add_fishing_result.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingResultEdit, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_result = get_object_or_404(FishingResult, pk=kwargs['fishing_result_id'])
        if fishing.owner == request.user and fishing_result.fishing == fishing:
            form = FishingResultForm(request.POST, instance=fishing_result)
            if form.is_valid():
                fishing_result = form.save(commit=False)
                fishing_result.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                fishs = Fish.objects.all()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'fishs': fishs,
                               'form': form,
                               'fishing': fishing,
                               'fishing_result': fishing_result})
        return redirect('fishing:fishing')
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_result = get_object_or_404(FishingResult, pk=kwargs['fishing_result_id'])
        if fishing.owner == request.user and fishing_result.fishing == fishing:
            form = FishingResultForm(instance=fishing_result)
            fishs = Fish.objects.all()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishs': fishs,
                           'form': form,
                           'fishing': fishing,
                           'fishing_result': fishing_result})
        return redirect('fishing:fishing')


class FishingTrophyAdd(View):
    """
    Добавляет трофей рыбалки
    """

    template = 'fishing/notes/fishing/edit_add_fishing_trophy.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingTrophyForm(request.POST)
            if form.is_valid():
                fishing_trophy = form.save(commit=False)
                fishing_trophy.owner = request.user
                fishing_trophy.fishing = fishing
                fishing_trophy.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                fishs = Fish.objects.all()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'fishs': fishs,
                               'form': form,
                               'fishing': fishing})
        return redirect('fishing:fishing')
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingTrophyForm()
            # fishs = Fish.objects.all()
            fishs = fishing.get_fish_for_trophy()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishs': fishs,
                           'form': form,
                           'fishing': fishing})
        return redirect('fishing:fishing')


class FishingTrophyDelete(View):
    """
    Удаляет трофей из рыбалки
    """
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTrophyDelete, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        fishing_trophy = get_object_or_404(FishingTrophy, pk=kwargs['fishing_trophy_id'])
        if fishing_trophy.owner == request.user:
            fishing_trophy.delete()
        return redirect('fishing:fishing_details', kwargs['fishing_id'])


class FishingTrophyEdit(View):
    """
    Редактирует трофей рыбалки
    """

    template = 'fishing/notes/fishing/edit_add_fishing_trophy.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FishingTrophyEdit, self).dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_trophy = get_object_or_404(FishingTrophy, pk=kwargs['fishing_trophy_id'])
        if fishing.owner == request.user and fishing_trophy.fishing == fishing:
            form = FishingTrophyForm(request.POST, instance=fishing_trophy)
            if form.is_valid():
                fishing_trophy = form.save(commit=False)
                fishing_trophy.save()
                return redirect('fishing:fishing_details', fishing.id)
            else:
                fishs = Fish.objects.all()
                return render(request,
                              self.template,
                              {'fisherman': getuserinfo(request),
                               'siteinfo': siteinfo(),
                               'fishs': fishs,
                               'form': form,
                               'fishing': fishing,
                               'fishing_trophy': fishing_trophy})
        return redirect('fishing:fishing')
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        fishing_trophy = get_object_or_404(FishingTrophy, pk=kwargs['fishing_trophy_id'])
        if fishing.owner == request.user and fishing_trophy.fishing == fishing:
            form = FishingTrophyForm(instance=fishing_trophy)
            fishs = Fish.objects.all()
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'fishs': fishs,
                           'form': form,
                           'fishing': fishing,
                           'fishing_trophy': fishing_trophy})
        return redirect('fishing:fishing')


class FishingNoteAddEdit(View):
    template = 'fishing/notes/fishing/edit_add_fishing_note.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingNoteForm(request.POST)
            if form.is_valid():
                fishing.note = form.cleaned_data['note']
                fishing.save()
                return redirect('fishing:fishing_details', fishing.id)
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'fishing': fishing})
        return redirect('fishing:fishing')
    
    def get(self, request, *args, **kwargs):
        fishing = get_object_or_404(Fishing, pk=kwargs['fishing_id'])
        if fishing.owner == request.user:
            form = FishingNoteForm(instance=fishing)
            return render(request,
                          self.template,
                          {'fisherman': getuserinfo(request),
                           'siteinfo': siteinfo(),
                           'form': form,
                           'fishing': fishing})
        return redirect('fishing:fishing')

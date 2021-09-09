from django.shortcuts import render
from django.views import View
from fishing.getinfo import siteinfo, getuserinfo

from fishing.models import Fishing, FishingResult

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class StatisticTrophyView(View):
    template = 'fishing/notes/statistics/trophys.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        trophys = {}
        trophys['fisherman'] = Fishing.get_trophys(self.request)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'trophys': trophys})


    class EffectivePace(View):
        """
        Эффектиынй темп
        """
    
        template = 'fishing/notes/statistics/effective_pace.html'
    
        @method_decorator(login_required)
        def dispatch(self, *args, **kwargs):
            return super().dispatch(*args, **kwargs)
    
        def effective_pace(self, *args, **kwargs):
            result = []
            result.append({'pace': '',
                           'weight': '',
                           'fishings': '',
                           'time': ''})
            fishings = Fishing.objects.filter(owner=self.request.user)
            for fishing in fishings:
                pass
            return result
        
        def get(self, *args, **kwargs):
            fishing_result = FishingResult.objects.filter(owner=self.request.user)
            if fishing_result:
                result = self.effective_pace()
            else:
                result = None
            return render(self.request,
                          self.template,
                          {'fisherman': getuserinfo(self.request),
                           'siteinfo': siteinfo(),
                           'effective_pace': result})

from django.shortcuts import render
from django.views import View
from fishing.getinfo import siteinfo, getuserinfo

from fishing.models import Fishing

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
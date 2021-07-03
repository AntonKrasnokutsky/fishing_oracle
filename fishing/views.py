from .models import FishingReportsSettings
from .models import Fishing

from django.shortcuts import get_object_or_404, render
from blog.views import Post
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .getinfo import siteinfo, getuserinfo

class Index(View):
    template = 'fishing/index.html'

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'posts': Post.objects.all()})


class FishermanNotes(View):
    template = 'fishing/notes.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request, 
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo()})


class FishermanGear(View):
    template = 'fishing/gear.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo()})


class FishermanFeed(View):
    template = 'fishing/feed.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo()})


class FishingReportView(View):
    
    template = 'fishing/report.html'
    
    def get(self, request, *args, **kwargs):
        fishing_report_settings = get_object_or_404(FishingReportsSettings, self_id=kwargs['report_id'])
        report = fishing_report_settings.report()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'report': report})


class TrophtReport(View):
    template = 'fishing/trophys.html'
    
    def get(self, *args, **kwargs):
        trophys = {}
        # Трофеи пользователя
        if self.request.user.is_authenticated:
            trophys['fisherman'] = Fishing.get_trophys(self.request)
        trophys['reports'] = FishingReportsSettings.get_trophy(request=self.request)
        return render(self.request,
                      self.template,
                      {'fisherman': getuserinfo(self.request),
                       'siteinfo': siteinfo(),
                       'trophys': trophys})

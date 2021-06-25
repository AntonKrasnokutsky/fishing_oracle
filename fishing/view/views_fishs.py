from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from fishing.models import Fish

from fishing.getinfo import siteinfo, getuserinfo


class FishList(View):
    """
    Возвращает список рыб
    """

    template = 'fishing/fish/list.html'
    
    def get(self, request, *args, **kwargs):
        fish_list = Fish.objects.all()
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'fish_list': fish_list})


class FishDetails(View):
    """
    Возвращает подробную нинформацию о рыбе
    """

    template = 'fishing/fish/details.html'
    
    def get(self, request, *args, **kwargs):
        fish_details = get_object_or_404(Fish, pk=kwargs['fish_id'])
        return render(request,
                      self.template,
                      {'fisherman': getuserinfo(request),
                       'siteinfo': siteinfo(),
                       'fish': fish_details})

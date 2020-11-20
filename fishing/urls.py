from django.urls import path, include
from . import views
#import .urls
app_name = 'fishing'
urlpatterns = [
    path('luremix/', include('fishing.url.urls_luremix')),
    path('water/', include('fishing.url.urls_water_place')),
    path('settings/', include('fishing.url.urls_settings')),
    path('aromabase/', include('fishing.url.urls_aroma_base')),
    path('crochet/', include('fishing.url.urls_crochet')),
    path('leash/', include('fishing.url.urls_leash')),
    path('lurebase/', include('fishing.url.urls_lure_base')),
    path('montage/', include('fishing.url.urls_montage')),
    path('nozzlebase/', include('fishing.url.urls_nozzle_base')),
    path('tackle/', include('fishing.url.urls_tackle')),
    path('trough/', include('fishing.url.urls_trough')),
    path('fishings/', include('fishing.url.urls_fishing')),
    # path('districts/', include('fishing.url.urls_districts')),
    
    
    # Главная страница
    path('',
         views.index,
         name='index'),

    

]

from django.urls import path, include
from . import views
#import .urls
app_name = 'fishing'
urlpatterns = [
    path('notes/feed/luremix/', include('fishing.url.urls_luremix')),
    path('notes/water/', include('fishing.url.urls_water_place')),
    path('settings/', include('fishing.url.urls_settings')),
    path('fishs/', include('fishing.url.urls_fishs')),
    path('notes/feed/aromabase/', include('fishing.url.urls_aroma_base')),
    path('notes/gear/crochet/', include('fishing.url.urls_crochet')),
    path('notes/gear/leash/', include('fishing.url.urls_leash')),
    path('notes/feed/lurebase/', include('fishing.url.urls_lure_base')),
    path('notes/gear/montage/', include('fishing.url.urls_montage')),
    path('notes/feed/nozzlebase/', include('fishing.url.urls_nozzle_base')),
    path('notes/gear/tackle/', include('fishing.url.urls_tackle')),
    path('notes/gear/trough/', include('fishing.url.urls_trough')),
    path('notes/fishings/', include('fishing.url.urls_fishing')),
    path('notes/statistics/', include('fishing.url.urls_statistics')),
    # path('districts/', include('fishing.url.urls_districts')),
    
    
    # Главная страница
    path('',
         views.Index.as_view(),
         name='index'),
    path('notes',
         views.FishermanNotes.as_view(),
         name='fisherman_notes'),
    path('notes/gear',
         views.FishermanGear.as_view(),
         name='fisherman_gear'),
    path('notes/feed',
         views.FishermanFeed.as_view(),
         name='fisherman_feed'),
    path('report/<str:report_id>',
         views.FishingReportView.as_view(),
         name='fishing_report'),
    path('trophys',
         views.TrophtReport.as_view(),
         name='trophys_report')
]

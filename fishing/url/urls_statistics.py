from django.urls import path
from fishing.view import views_statistics as views


urlpatterns = [
    path('trophys',
         views.StatisticTrophyView.as_view(),
         name='statistic_trophy'
         ),
    ]

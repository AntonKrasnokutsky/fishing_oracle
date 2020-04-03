from django.contrib import admin
from .models import Fishing
from .models import Fish
from .models import Fish_Trophy
from .models import Fishing_Result
from .models import Weather
from .models import Weather_Phenomena

admin.site.register(Fishing)
admin.site.register(Fish)
admin.site.register(Fish_Trophy)
admin.site.register(Fishing_Result)
admin.site.register(Weather)
admin.site.register(Weather_Phenomena)

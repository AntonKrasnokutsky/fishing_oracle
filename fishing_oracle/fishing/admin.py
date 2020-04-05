from django.contrib import admin
from .models import Fishing
from .models import Fish
from .models import Fish_Trophy
from .models import Fishing_Result
from .models import Weather
from .models import Weather_Phenomena
from .models import Aroma
from .models import Lure
from .models import Fishing_Tackle
from .models import Nozzle
from .models import District
from .models import Water
from .models import Priming
from .models import Bottom_Map
from .models import Point
from .models import Fishing_Point
from .models import Place

admin.site.register(Fishing)
admin.site.register(Fish)
admin.site.register(Fishing_Result)
admin.site.register(Fish_Trophy)
admin.site.register(Weather)
admin.site.register(Weather_Phenomena)
admin.site.register(Aroma)
admin.site.register(Lure)
admin.site.register(Fishing_Tackle)
admin.site.register(Nozzle)
admin.site.register(District)
admin.site.register(Water)
admin.site.register(Priming)
admin.site.register(Bottom_Map)
admin.site.register(Point)
admin.site.register(Fishing_Point)
admin.site.register(Place)

# Для статистической выборки
from .models import Fishing
from .models import FishingResult
from .models import FishingTrophy
from users.forms import CustomUserChangeForm
from users.models import CustomUser

def siteinfo():
    result = {}
    fisherman = CustomUser.objects.all()
    result['fisherman'] = len(fisherman)
    fishing = Fishing.objects.all()
    result['fishing'] = len(fishing)
    fishingresults = FishingResult.objects.all()
    fish = 0
    fish_weight = 0
    for fishingresult in fishingresults:
        fish += fishingresult.number_of_fish
        fish_weight += fishingresult.fish_weight
    result['fish'] = fish
    result['fish_weight'] = fish_weight
    fishingtrophi = FishingTrophy.objects.all()
    fish_trophy = 0
    fish_trophy_weight = 0
    fish_trophy_name = ""
    for fishingtrophy in fishingtrophi:
        fish_trophy += 1
        if fishingtrophy.fish_trophy_weight > fish_trophy_weight:
            fish_trophy_weight = fishingtrophy.fish_trophy_weight
            fish_trophy_name = fishingtrophy.fish.name
    result['fish_trophy'] = fish_trophy
    result['fish_trophy_name'] = fish_trophy_name
    result['fish_trophy_weight'] = fish_trophy_weight
    return result

def getuserinfo(request):
    if request.user.is_authenticated:
        result_dict = {}
        fishing = Fishing.objects.filter(owner=request.user)
        result_dict['fishing'] = len(fishing)
        fishingresults = FishingResult.objects.filter(owner=request.user)
        fish = 0
        fish_weight = 0
        for fishingresult in fishingresults:
            fish += fishingresult.number_of_fish
            fish_weight += fishingresult.fish_weight
        result_dict['fish'] = fish
        result_dict['fish_weight'] = fish_weight
        fishingtrophi = FishingTrophy.objects.filter(owner=request.user)
        fish_trophy = 0
        fish_trophy_weight = 0
        fish_trophy_name = ""
        for fishingtrophy in fishingtrophi:
            fish_trophy += 1
            if fishingtrophy.fish_trophy_weight > fish_trophy_weight:
                fish_trophy_weight = fishingtrophy.fish_trophy_weight
                fish_trophy_name = fishingtrophy.fish.name
        result_dict['fish_trophy'] = fish_trophy
        result_dict['fish_trophy_name'] = fish_trophy_name
        result_dict['fish_trophy_weight'] = fish_trophy_weight
        result = result_dict
    else:
        result = CustomUserChangeForm()
    return result

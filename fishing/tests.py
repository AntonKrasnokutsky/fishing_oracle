from django.contrib.auth import get_user_model
from fishing.models import Fish, Fishing, FishingLureMix, FishingPlace, FishingReportsSettings, FishingResult, FishingTackle, FishingTrophy, FishingWeather, LureMix, Place, Tackle, Water, Weather
from django.test import TestCase

# Create your tests here.
class FishingTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='foo',
            nick='first')
        user_second = User.objects.create_user(
            email='second@user.com',
            password='foo',
            nick='second')
        Fishing.objects.create(owner=user,
                                         date='2020-01-01',
                                         time_start='10:00',
                                         time_end='10:10')
        fishing = Fishing.objects.get(owner=user)
        fish = Fish.objects.create(name='карась')
        fishing.set_planned()
        fishing.save()
        
    def test_fish_first_upper(self):
        fish = Fish.objects.get(name='карась')
        fish.first_upper()
        fish.save()
        self.assertEqual(fish.name, 'Карась')
    
    def test_fishing_trophy_str(self, *args, **kwargs):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        fish = Fish.objects.get(name='карась')
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=1.1)
        fishing_trophy = FishingTrophy.objects.get(fishing=fishing)
        self.assertEqual(str(fishing_trophy), 'Трофей: карась 1.10кг.')
    
    def test_fishing_date_to_str(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        self.assertEqual(fishing.date_to_str(), "01 января 2020")
    
    def test_fishing_set_planned(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        self.assertFalse(fishing.planned)
        fishing.date = '2022-08-24'
        fishing.save()
        fishing = Fishing.objects.get(owner=user)
        fishing.set_planned()
        self.assertTrue(fishing.planned)
        fishing.date = '2020-01-01'
        fishing.save()
        fishing = Fishing.objects.get(owner=user)
        fishing.set_planned()
    
    def test_fishing_get_trophy_report(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        fish = Fish.objects.get(name='карась')
        result = {'fish': [],
                  'weight': [],
                  'fishing': []}
        self.assertEqual(Fishing.get_trophys_report(user), result)
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=1.10)
        fishing_trophy = FishingTrophy.objects.get(fishing=fishing)
        result = {'fish': [str(fishing_trophy.fish)],
                  'weight': [str(fishing_trophy.fish_trophy_weight)],
                  'fishing': [fishing_trophy.fishing.id]}
        self.assertEqual(Fishing.get_trophys_report(user), result)
    
    def test_fishing_get_luremix(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        self.assertFalse(Fishing.get_luremix(fishing_id=fishing.id, user=user))
        lure_mix = LureMix.objects.create(owner=user,
                                          name='Тестовый микс')
        FishingLureMix.objects.create(owner=user,
                                      fishing=fishing,
                                      lure_mix=lure_mix)
        fishing_lure_mix = FishingLureMix.objects.get(fishing=fishing)
        lure_mix = fishing_lure_mix.lure_mix
        self.assertEqual(Fishing.get_luremix(fishing_id=fishing.id, user=user), lure_mix)
    
    def test_fishing_get_fish_for_trophy(self):
        result = []
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        self.assertEqual(fishing.get_fish_for_trophy(), result)
        fish = Fish.objects.get(name='карась')
        result.append(fish)
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     number_of_fish=2,
                                     fish_weight=1.5)
        self.assertEqual(fishing.get_fish_for_trophy(), result)
        
    def test_fishing_get_trophy(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        result = {'fish': [],
                  'weight': [],
                  'target': []}
        self.assertEqual(fishing.get_trophy(), result)
        fish = Fish.objects.get(name='карась')
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     number_of_fish=2,
                                     fish_weight=1.5)
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=1.1)
        result['fish'].append(str(fish))
        result['weight'].append('1.10')
        result['target'].append(False)
        self.assertEqual(fishing.get_trophy(), result)
        fish = Fish.objects.create(name='Лещ')
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     number_of_fish=3,
                                     fish_weight=2.2,
                                     target=True)
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=2.2)
        result['fish'].append(str(fish))
        result['weight'].append('2.20')
        result['target'].append(True)
        self.assertEqual(fishing.get_trophy(), result)        


# class FishingReportTestCase(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         user = User.objects.create_user(email='normal@user.com',
#                                         password='foo',
#                                         nick='first')
#         Fish.objects.create(name='Карась')
#         fish = Fish.objects.get(name='Карась')
#         Fishing.objects.create(owner=user,
#                                date='2021-01-01',
#                                time_start='10:00',
#                                time_end='10:10')
#         fishing = Fishing.objects.get(owner=user)
#         Water.objects.create(owner=user,
#                              name='Маныч')
#         water = Water.objects.get(name='Маныч')
#         Place.objects.create(owner=user,
#                              water=water)
#         place = Place.objects.get(owner=user)
#         FishingPlace.objects.create(owner=user,
#                                     fishing=fishing,
#                                     place=place)
#         del(water)
#         del(place)
#         Weather.objects.create(date=fishing.date,
#                                temperature=26.6)
#         weather = Weather.objects.get(date=fishing.date)
#         FishingWeather.objects.create(owner=user,
#                                       fishing=fishing,
#                                       weather=weather)
#         del(weather)
#         Tackle.objects.create(owner=user,
#                               manufacturer='Производитель',
#                               model_tackle='Модель',
#                               length='Длина',
#                               casting_weight=100)
#         tackle = Tackle.objects.get(owner=user)
#         FishingTackle.objects.create(owner=user,
#                                      fishing=fishing,
#                                      tackle=tackle)
#         del(tackle)
#         LureMix.objects.create(owner=user,
#                                name='Тестовый микс')
#         lure_mix = LureMix.objects.get(owner=user)
#         FishingLureMix.objects.create(owner=user,
#                                       fishing=fishing,
#                                       lure_mix=lure_mix)
#         del(lure_mix)
#         FishingResult.objects.create(owner=user,
#                                      fishing=fishing,
#                                      fish=fish,
#                                      number_of_fish=5,
#                                      fish_weight=2.5,
#                                      target=True)
#         FishingTrophy.objects.create(owner=user,
#                                      fishing=fishing,
#                                      fish=fish,
#                                      fish_trophy_weight=1.5)
#         FishingReportsSettings.objects.create()

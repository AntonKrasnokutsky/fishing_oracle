import fishing
from django.contrib.auth import get_user_model
from fishing.models import Aroma, AromaBase, Crochet, Fish, Fishing, FishingCrochet, FishingLeash, FishingLureMix, FishingMontage, FishingNozzle, FishingPace, FishingPlace, FishingReportsSettings, FishingResult, FishingTackle, FishingTrophy, FishingTrough, FishingWeather, Leash, Lure, LureBase, LureMix, Montage, Nozzle, NozzleBase, NozzleState, Pace, Place, Tackle, Trough, Water, Weather
from django.test import TestCase

class FishTestCase(TestCase):
    def setUp(self):
        Fish.objects.create(name='карась')
        
    def test_fish_first_upper(self):
        print('FishTestCase Fish.first_upper()')
        fish = Fish.objects.get(name='карась')
        fish.first_upper()
        fish.save()
        self.assertEqual(fish.name, 'Карась')

class FishingDetailsTestCase(TestCase):
    maxDiff = None
    
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com',
                                 password='foo',
                                 nick='first')
        Fishing.objects.create(owner=user,
                               date="2021-01-01",
                               time_start="10:00",
                               time_end="10:40")
        fishing = Fishing.objects.get(owner=user)
        water = Water.objects.create(owner=user, name='Водоём')
        place = Place.objects.create(owner=user,
                                     water=water,
                                     name="Место")
        FishingPlace.objects.create(owner=user,
                                    fishing=fishing,
                                    place=place)
        weather = Weather.objects.create(date=fishing.date, temperature=25)
        FishingWeather.objects.create(owner=user,
                                      fishing=fishing,
                                      weather=weather)
        tackle = Tackle.objects.create(owner=user,
                                       manufacturer="Производитель",
                                       model_tackle='Модель',
                                       length=3.6,
                                       casting_weight=100)
        fishing_tackle = FishingTackle.objects.create(owner=user,
                                                      fishing=fishing,
                                                      tackle=tackle)
        montage = Montage.objects.create(owner=user,
                                         name="Монтаж")
        FishingMontage.objects.create(owner=user,
                                      fishing_tackle=fishing_tackle,
                                      montage=montage)
        trough = Trough.objects.create(owner=user,
                                       manufacturer="Производитель")
        FishingTrough.objects.create(owner=user,
                                     fishing_tackle=fishing_tackle,
                                     trough=trough)
        leash = Leash.objects.create(owner=user,
                                     material='Материал',
                                     diameter=0.2,
                                     length=12)
        FishingLeash.objects.create(owner=user,
                                    fishing_tackle=fishing_tackle,
                                    leash=leash)
        crochet = Crochet.objects.create(owner=user,
                                         size=12)
        FishingCrochet.objects.create(owner=user,
                                      fishing_tackle=fishing_tackle,
                                      crochet=crochet)
        nozzle = NozzleBase.objects.create(owner=user,
                                           bait=True,
                                           name='Наживка 1')
        nozzle_state = NozzleState.objects.create(owner=user,
                                                  state="Состояние")
        FishingNozzle.objects.create(owner=user,
                                     fishing_tackle=fishing_tackle,
                                     nozzle_base=nozzle,
                                     nozzle_state=nozzle_state,
                                     number=2,
                                     position=1)
        nozzle = NozzleBase.objects.create(owner=user,
                                           bait=True,
                                           name='Наживка 2')
        FishingNozzle.objects.create(owner=user,
                                     fishing_tackle=fishing_tackle,
                                     nozzle_base=nozzle,
                                     nozzle_state=nozzle_state,
                                     number=2,
                                     position=2)
        pace = Pace.objects.create(interval='Интервал')
        FishingPace.objects.create(owner=user,
                                   fishing_tackle=fishing_tackle,
                                   pace=pace)
        lure_mix = LureMix.objects.create(owner=user,
                                          name="Микс")
        lure_base = LureBase.objects.create(owner=user,
                                            manufacturer="Производитель")
        Lure.objects.create(owner=user,
                            mix=lure_mix,
                            base=lure_base,
                            weight=0.5)
        aroma_base = AromaBase.objects.create(owner=user,
                                              manufacturer="Производтель")
        Aroma.objects.create(owner=user,
                             mix=lure_mix,
                             base=aroma_base,
                             volume=0.4)
        Nozzle.objects.create(owner=user,
                              base=nozzle,
                              state=nozzle_state,
                              mix=lure_mix)
        FishingLureMix.objects.create(owner=user,
                                      fishing=fishing,
                                      lure_mix=lure_mix)
        fish = Fish.objects.create(name='Рыба 1')
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     number_of_fish=4,
                                     fish_weight=2.3,
                                     target=True)
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=1.9)
        fish = Fish.objects.create(name='Рыба 2')
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     number_of_fish=5,
                                     fish_weight=1.3,
                                     target=False)
        fish = Fish.objects.create(name='Рыба 3')
        FishingResult.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     target=False)
        
    
    def test_get_details(self, *args, **kwargs):
        print('FishingTestCase Fishing.get_details()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        result = {'id': 1,
                  'planned': False,
                  'date_time': {'date': "01 января 2021 г.",
                                'time_start': "10:00",
                                'time_end': "10:40"},
                  'note': None,
                  'place': {'water': "Водоём",
                            'locality': None,
                            'name': "Место",
                            'latitude': None,
                            'longitude': None},
                  'weather': {'overcast': None,
                              'conditions': None,
                              'temperature': '25.0',
                              'pressure': None,
                              'direction_wind': None,
                              'wind_speed': None,
                              'lunar_day': None},
                  'tackles': [{'tackle': {'id': 1,
                                          'manufacturer': 'Производитель',
                                          'model_tackle': 'Модель',
                                          'length': '3.6 м.',
                                          'casting_weight': '100 гр.'},
                               'montage': {'name': 'Монтаж'},
                               'trough': {'manufacturer': 'Производитель',
                                          'model_name': None,
                                          'plastic': False,
                                          'lugs': False,
                                          'feed_capacity': None,
                                          'weight': None},
                               'leash': {'material': 'Материал',
                                         'diameter': '0.200 мм.',
                                         'length': '12 см.'},
                               'crochet': {'manufacturer': None,
                                           'model': None,
                                           'size': '12'},
                               'nozzles': [{'position': '1',
                                            'bait': True,
                                            'manufacturer': None,
                                            'name': 'Наживка 1',
                                            'size': None,
                                            'ntype': None,
                                            'number': '2 шт.',
                                            'state': 'Состояние'},
                                           {'position': '2',
                                            'bait': True,
                                            'manufacturer': None,
                                            'name': 'Наживка 2',
                                            'size': None,
                                            'ntype': None,
                                            'number': '2 шт.',
                                            'state': 'Состояние'}],
                               'pace': {'pace': 'Интервал'},
                               }],
                  'lure': None,
                #   'lure': {'lure': {'manufacturer': None,
                #                     'name': None},
                #            'weight': None},
                  'lure_mix': {'name': "Микс",
                               'description': None,
                               'lures':[{'lure': {'manufacturer': 'Производитель',
                                                  'name': None},
                                         'weight': '0.50'}],
                               'aromas': [{'aroma': {'manufacturer': 'Производтель',
                                                     'name': None},
                                           'volume': '0.40'}],
                               'filling': [{'bait': True,
                                            'manufacturer': None,
                                            'name': 'Наживка 2',
                                            'size': None,
                                            'ntype': None,
                                            'state': 'Состояние'}]},
                  'results': [{'id': 1,
                               'fish': 'Рыба 1',
                               'number_of_fish': '4 шт.',
                               'fish_weight': '2.300 кг.',
                               'target': True,
                               'average_weight': '0.575 кг.'},
                              {'id': 2,
                               'fish': 'Рыба 2',
                               'number_of_fish': '5 шт.',
                               'fish_weight': '1.300 кг.',
                               'target': False,
                               'average_weight': '0.260 кг.'},
                              {'id': 3,
                               'fish': 'Рыба 3',
                               'number_of_fish': None,
                               'fish_weight': None,
                               'target': False,
                               'average_weight': None}],
                  'trophys': [{'id': 1,
                               'fish': 'Рыба 1',
                               'weight': '1.90',
                               'target': True}],
                #   'report': {'url': None}
                  'report': None
                  }
        
        fishing = Fishing.objects.get(owner=user)
        # fishing.get_details()
        self.assertEqual(fishing.get_details(), result)
        lure = Lure.objects.get(id=1)
        lure.delete()
        aroma = Aroma.objects.get(id=1)    
        aroma.delete()
        nozzle = Nozzle.objects.get(id=1)
        nozzle.delete()
        
        result = {'id': 1,
                  'planned': False,
                  'date_time': {'date': "01 января 2021 г.",
                                'time_start': "10:00",
                                'time_end': "10:40"},
                  'note': None,
                  'place': {'water': "Водоём",
                            'locality': None,
                            'name': "Место",
                            'latitude': None,
                            'longitude': None},
                  'weather': {'overcast': None,
                              'conditions': None,
                              'temperature': '25.0',
                              'pressure': None,
                              'direction_wind': None,
                              'wind_speed': None,
                              'lunar_day': None},
                  'tackles': [{'tackle': {'id': 1,
                                          'manufacturer': 'Производитель',
                                          'model_tackle': 'Модель',
                                          'length': '3.6 м.',
                                          'casting_weight': '100 гр.'},
                               'montage': {'name': 'Монтаж'},
                               'trough': {'manufacturer': 'Производитель',
                                          'model_name': None,
                                          'plastic': False,
                                          'lugs': False,
                                          'feed_capacity': None,
                                          'weight': None},
                               'leash': {'material': 'Материал',
                                         'diameter': '0.200 мм.',
                                         'length': '12 см.'},
                               'crochet': {'manufacturer': None,
                                           'model': None,
                                           'size': '12'},
                               'nozzles': [{'position': '1',
                                            'bait': True,
                                            'manufacturer': None,
                                            'name': 'Наживка 1',
                                            'size': None,
                                            'ntype': None,
                                            'number': '2 шт.',
                                            'state': 'Состояние'},
                                           {'position': '2',
                                            'bait': True,
                                            'manufacturer': None,
                                            'name': 'Наживка 2',
                                            'size': None,
                                            'ntype': None,
                                            'number': '2 шт.',
                                            'state': 'Состояние'}],
                               'pace': {'pace': 'Интервал'},
                               }],
                  'lure': None,
                #   'lure': {'lure': {'manufacturer': None,
                #                     'name': None},
                #            'weight': None},
                  'lure_mix': {'name': "Микс",
                               'description': None,
                               'lures': None,
                               'aromas': None,
                               'filling': None},
                  'results': [{'id': 1,
                               'fish': 'Рыба 1',
                               'number_of_fish': '4 шт.',
                               'fish_weight': '2.300 кг.',
                               'target': True,
                               'average_weight': '0.575 кг.'},
                              {'id': 2,
                               'fish': 'Рыба 2',
                               'number_of_fish': '5 шт.',
                               'fish_weight': '1.300 кг.',
                               'target': False,
                               'average_weight': '0.260 кг.'},
                              {'id': 3,
                               'fish': 'Рыба 3',
                               'number_of_fish': None,
                               'fish_weight': None,
                               'target': False,
                               'average_weight': None}],
                  'trophys': [{'id': 1,
                               'fish': 'Рыба 1',
                               'weight': '1.90',
                               'target': True}],
                #   'report': {'url': None}
                  'report': None
                  }
        self.assertEqual(fishing.get_details(), result)


class FishingReportsSettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
    
    def setUp(self):
        pass
    
    def test_report(self):
        print('FishingReportsSettingsTestCase FishingReportsSettings.report()')
        pass


class FishingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        User.objects.create_user(email='normal@user.com',
                                 password='foo',
                                 nick='first')
        User.objects.create_user(email='second@user.com',
                                 password='foo',
                                 nick='second')
        Fish.objects.create(name='карась')
    
    def setUp(self):
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        Fishing.objects.create(owner=user,
                               date='2020-01-01',
                               time_start='10:00',
                               time_end='10:10')
        fishing = Fishing.objects.get(owner=user)
        fishing.set_planned()
        fishing.save()
    
    def test_fishing_trophy_str(self, *args, **kwargs):
        print('FishingTestCase FishingTrophy.__str__()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        fish = Fish.objects.get(name='карась')
        FishingTrophy.objects.create(owner=user,
                                     fishing=fishing,
                                     fish=fish,
                                     fish_trophy_weight=1.1)
        fishing_trophy = FishingTrophy.objects.get(fishing=fishing)
        self.assertEqual(str(fishing_trophy), 'карась 1.10кг.')
    
    def test_fishing_date_to_str(self):
        print('FishingTestCase Fishing.date_to_str()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing = Fishing.objects.get(owner=user)
        self.assertEqual(fishing.date_to_str(), "01 января 2020 г.")
    
    def test_fishing_set_planned(self):
        print('FishingTestCase Fishing.set_planned()')
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
        print('FishingTestCase Fishing.get_trophys_report()')
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
        print('FishingTestCase Fishing.get_luremix()')
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
        print('FishingTestCase Fishing.get_fish_for_trophy()')
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
        print('FishingTestCase Fishing.get_trophy()')
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
        

class TackleTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='foo',
            nick='first')
        Tackle.objects.create(owner=user,
                              manufacturer='производитель',
                              model_tackle='модель',
                              length=3.6,
                              casting_weight=100)
    
    def test_str(self):
        print('TackleTestCase Tackle.__str__()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        tackle = Tackle.objects.get(owner=user)
        self.assertEqual(str(tackle), 'производитель модель 3.6м. 100гр.')
    
    def test_first_upper(self, *args, **kwargs):
        print('TackleTestCase Tackle.first_upper()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        tackle = Tackle.objects.get(owner=user)
        tackle.first_upper()
        tackle.save()
        tackle = Tackle.objects.get(owner=user)
        self.assertEqual(str(tackle), 'Производитель Модель 3.6м. 100гр.')
    
    def test_unique(self):
        print('TackleTestCase Tackle.unique()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        tackle_unique = Tackle()
        tackle_unique.owner = user
        tackle_unique.manufacturer = 'Производитель 1'
        tackle_unique.model_tackle = 'Модель 2'
        tackle_unique.length = 2.1
        tackle_unique.casting_weight = 50
        self.assertTrue(tackle_unique.unique())
        tackle = Tackle.objects.get(owner=user)
        tackle_notunique = Tackle()
        tackle_notunique.owner = user
        tackle_notunique.manufacturer = tackle.manufacturer
        tackle_notunique.model_tackle = tackle.model_tackle
        tackle_notunique.length = tackle.length
        tackle_notunique.casting_weight = tackle.casting_weight
        self.assertFalse(tackle_notunique.unique())


class FishingNozzleTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='foo',
            nick='first')
        Fishing.objects.create(owner=user,
                                         date='2020-01-01',
                                         time_start='10:00',
                                         time_end='10:10')
        fishing = Fishing.objects.get(owner=user)
        fishing.set_planned()
        fishing.save()
        tackle = Tackle.objects.create(owner=user,
                              manufacturer='Производитель')
        FishingTackle.objects.create(owner=user,
                                     fishing = fishing,
                                     tackle=tackle)
        NozzleBase.objects.create(owner=user,
                                  bait=True,
                                  name="Опарыш")
        NozzleBase.objects.create(owner=user,
                                  bait=True,
                                  name="Червь")
        NozzleBase.objects.create(owner=user,
                                  bait=True,
                                  name="Мотыль")
        NozzleState.objects.create(owner=user,
                                   state="Натуральное")
        NozzleState.objects.create(owner=user,
                                   state="Резка")
        NozzleState.objects.create(owner=user,
                                   state="Вареная")
        
    def test_set_position(self, *args, **kwargs):
        print('FishingNozzleTestCase FishingNozzle.set_position()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing_tackle = FishingTackle.objects.get(owner=user)
        nozzles = NozzleBase.objects.filter(owner=user)
        nozzles = nozzles.exclude(name='Опарыш')
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base=NozzleBase.objects.get(name='Опарыш')
        fishing_nozzle.number = 1
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name='Опарыш'))
        self.assertEqual(fishing_nozzle.position, 1)
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base=NozzleBase.objects.get(name='Мотыль')
        fishing_nozzle.number = 1
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name='Мотыль'))
        self.assertEqual(fishing_nozzle.position, 2)
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base=NozzleBase.objects.get(name='Червь')
        fishing_nozzle.number = 1
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name='Червь'))
        self.assertEqual(fishing_nozzle.position, 3)
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name='Мотыль'))
        print(fishing_nozzle.position)
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        print(fishing_nozzle.position)
        self.assertEqual(fishing_nozzle.position, 2)
    
    def test_reindexing_position(self):
        print('FishingNozzleTestCase FishingNozzle.reindexing_position()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing_tackle = FishingTackle.objects.get(owner=user)
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.position_reindexing()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Опарыш")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Натуральное')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Червь")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Вареная')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Мотыль")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Резка')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        result = {'Опарыш': 1,
                  'Мотыль': 3,
                  'Червь': 2}
        
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name="Червь"))
        fishing_nozzle.position_reindexing()
                
        reresult = {}
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
        
        fishing_nozzle.delete()
        fishing_nozzle.position_reindexing()
        result = {'Опарыш': 1,
                  'Мотыль': 2}
        reresult = {}
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
    
    def test_position_up(self, *args, **kwargs):
        print('FishingNozzleTestCase FishingNozzle.position_up()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing_tackle = FishingTackle.objects.get(owner=user)
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Опарыш")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Натуральное')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Червь")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Вареная')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Мотыль")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Резка')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        fishing_nozzle.position_up()
        result = {'Опарыш': 1,
                  'Мотыль': 2,
                  'Червь': 3}
        reresult = {}
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
        
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name="Опарыш"))
        fishing_nozzle.position_up()
        
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
    
    def test_position_down(self, *args, **kwargs):
        print('FishingNozzleTestCase FishingNozzle.position_down()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        fishing_tackle = FishingTackle.objects.get(owner=user)
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Опарыш")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Натуральное')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Червь")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Вареная')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = NozzleBase.objects.get(name="Мотыль")
        fishing_nozzle.nozzle_state = NozzleState.objects.get(state='Резка')
        fishing_nozzle.set_position()
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle.objects.get(nozzle_base=NozzleBase.objects.get(name="Червь"))
        fishing_nozzle.position_down()
        
        result = {'Опарыш': 1,
                  'Мотыль': 2,
                  'Червь': 3}
        reresult = {}
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
        
        fishing_nozzle.position_down()
        
        for res in FishingNozzle.objects.filter(fishing_tackle=fishing_tackle):
            reresult[str(res.nozzle_base)] = res.position
        self.assertEqual(reresult, result)
    
    def test_get_nozzle_state_list(self, *args, **kwargs):
        print('FishingNozzleTestCase FishingNozzle.get_nozzle_state_list()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        result = NozzleState.objects.filter(owner=user)
        fishing_tackle = FishingTackle.objects.get(owner=user)
        nozzle_base = NozzleBase.objects.get(name="Опарыш")
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = nozzle_base
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)
        fishing_nozzle.set_position()
        nozzle_state = NozzleState.objects.get(state="Натуральное")
        fishing_nozzle.nozzle_state = nozzle_state
        fishing_nozzle.save()
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)
        
        nozzle_base = NozzleBase.objects.get(name="Червь")
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = nozzle_base
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)
        fishing_nozzle.set_position()
        nozzle_state = NozzleState.objects.get(state="Натуральное")
        fishing_nozzle.nozzle_state = nozzle_state
        fishing_nozzle.save()
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)
        
        fishing_nozzle = FishingNozzle()
        fishing_nozzle.owner = user
        fishing_nozzle.fishing_tackle = fishing_tackle
        fishing_nozzle.nozzle_base = nozzle_base
        result = result.exclude(state="Натуральное")
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)
        fishing_nozzle.set_position()
        nozzle_state = NozzleState.objects.get(state="Резка")
        fishing_nozzle.nozzle_state = nozzle_state
        fishing_nozzle.save()
        
        fishing_nozzle = FishingNozzle.objects.get(position=2)
        result = NozzleState.objects.filter(owner=user)
        result = result.exclude(state="Резка")
        self.assertQuerysetEqual(fishing_nozzle.get_nozzle_state_list(), result)


class NozzleBaseTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='foo',
            nick='first')
        NozzleBase.objects.create(owner=user,
                                  bait=True,
                                  name='наживка')
    
    def test_str(self):
        print('NozzleBaseTestCase NozzleBase.__str__()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        nozzle_base = NozzleBase.objects.get(owner=user)
        self.assertEqual(str(nozzle_base), nozzle_base.name)
        nozzle_base.bait = False
        nozzle_base.manufacturer = 'производитель'
        nozzle_base.name = 'насадка'
        nozzle_base.size = 12
        self.assertEqual(str(nozzle_base), 'производитель насадка 12мм.')
    
    def test_first_upper(self):
        print('NozzleBaseTestCase NozzleBase.first_upper()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        nozzle_base = NozzleBase.objects.get(owner=user)
        nozzle_base.first_upper()
        self.assertEqual(str(nozzle_base), 'Наживка')
        nozzle_base.bait = False
        nozzle_base.manufacturer = 'производитель'
        nozzle_base.name = 'насадка'
        nozzle_base.size = 12
        nozzle_base.first_upper()
        self.assertEqual(str(nozzle_base), 'Производитель Насадка 12мм.')

    def test_unique(self):
        print('NozzleBaseTestCase NozzleBase.unique()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        nozzle = NozzleBase()
        nozzle.owner = user
        nozzle.name = 'опарыш'
        nozzle.bait = True
        self.assertTrue(nozzle.unique())
        nozzle_base = NozzleBase.objects.get(owner=user)
        nozzle.name = nozzle_base.name
        self.assertFalse(nozzle.unique())


class NozzleStateTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com',
                                        password='foo',
                                        nick='first')
        NozzleState.objects.create(owner=user,
                                   state="состояние 1")
        NozzleState.objects.create(owner=user,
                                   state="состояние 2")
        NozzleState.objects.create(owner=user,
                                   state="состояние 3")
    
    def test_str(self):
        print('NozzleStateTestCase NozzleState.__str__()')
        nozzle_state = NozzleState.objects.get(state="состояние 1")
        
        result = 'состояние 1'
        self.assertEqual(nozzle_state.__str__(), result)
        
    def test_first_upper(self, *args, **kwargs):
        print('NozzleStateTestCase NozzleState.first_upper()')
        nozzle_state = NozzleState.objects.get(state="состояние 1")
        nozzle_state.first_upper()
        nozzle_state.save()
        result = "Состояние 1"
        self.assertEqual(nozzle_state.__str__(), result)
        
        nozzle_state = NozzleState.objects.get(state="состояние 2")
        nozzle_state.first_upper()
        nozzle_state.save()
        result = "Состояние 2"
        self.assertEqual(nozzle_state.__str__(), result)
        
        nozzle_state = NozzleState.objects.get(state="состояние 3")
        nozzle_state.first_upper()
        nozzle_state.save()
        result = "Состояние 3"
        self.assertEqual(nozzle_state.__str__(), result)
    
    def test_unique(self, *args, **kwargs):
        print('NozzleStateTestCase NozzleState.unique()')
        User = get_user_model()
        user = User.objects.get(email='normal@user.com')
        nozzle_state = NozzleState()
        nozzle_state.owner = user
        nozzle_state.state = "состояние 1"
        self.assertFalse(nozzle_state.unique())
        nozzle_state.state = "Состояние 1"
        self.assertFalse(nozzle_state.unique())
        nozzle_state.state = "Состояние 2"
        self.assertFalse(nozzle_state.unique())
        nozzle_state.state = "Состояние 4"
        self.assertTrue(nozzle_state.unique())


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

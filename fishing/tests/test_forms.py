from fishing.models import NozzleState
from django.contrib.auth import get_user_model
from fishing.forms import FishingNozzleForm
from django.test import TestCase

# Create your tests here.

class FishingNozzleFormTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com',
            password='foo',
            nick='first')
        NozzleState.objects.create(owner=user,
                                   state='Состояние 1')
        NozzleState.objects.create(owner=user,
                                   state='Состояние 2')
        NozzleState.objects.create(owner=user,
                                   state='Состояние 3')
    
    def setUp(self):
        pass
    
    def test_clean(self):
        form_data = {'nozzle_state': 1,
                     'number': 2}
        form = FishingNozzleForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        form_data = {'nozzle_state': 1,
                     'number': 2.2}
        form = FishingNozzleForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        form_data = {'nozzle_state': None,
                     'number': 2}
        form = FishingNozzleForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        form_data = {'nozzle_state': 1,
                     'number': 0}
        form = FishingNozzleForm(data=form_data)
        self.assertFalse(form.is_valid())

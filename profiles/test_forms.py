from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForms(TestCase):

    def test_create_profile_form(self):
        form = UserProfileForm({
            'profile': 'alex',
            'email': 'alex_a@gmail.com',
            'phone_number': '+46 123456 789',
            'street_adress1': '123 test street',
            'town_or_city': 'test city',
            'country': 'SE'})
        self.assertTrue(form.is_valid())

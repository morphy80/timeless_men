from django.test import TestCase
from .forms import OrderForm


class TestCheckoutOrderForm(TestCase):

    def test_generate_order_with_required_fields(self):
        form = OrderForm({
            'full_name': 'Alex Apo',
            'email': 'alex_a@gmail.com',
            'phone_number': '+46 123456 789',
            'street_adress1': '123 test street',
            'postcode': '455 65',
            'town_or_city': 'test city',
            'country': 'SE'})
        self.assertFalse(form.is_valid())

    def test_generate_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'],
                         [u'This field is required.'])

from django.test import TestCase
from .forms import ProductForm


class TestProductForms(TestCase):

    def test_create_product_form_incomplete(self):
        form = ProductForm({
            'sku': 'pp50000000000',
            'name': 'New product',
            'description': 'This is the product I am testing',
            'case': '',
            'strap': 'leather',
            'rating': '2',
            'brand': '',
            'year_warranty': True,
            'price': 222.34})
        self.assertFalse(form.is_valid())

    def test_create_product_form_complete(self):
        form = ProductForm({
            'category': 'analog',
            'sku': 'pp5011110111',
            'name': 'New product',
            'description': 'This is the product I am testing',
            'price': 222.34,
            'case': '44mm Ø',
            'strap': 'leather',
            'brand': 'Bratelboro',
            'year_warranty': '5 years',
            'rating': '3.95',
            'image_url': 'https://res.cloudinary.com/ddrsbzhmf/image/upload/v1611426563/timeless\
                        /analog_srn7iv.jpg',
            'image': 'analog.jpg'})
        self.assertFalse(form.is_valid())

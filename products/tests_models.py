from django.test import TestCase
from .models import Product, Category


class TestProductModel(TestCase):

    def test_string_representation(self):
        product = Product.objects.create(name="Test products",
                                        description="Test description",
                                        price=255.99)
        self.assertEqual(str(product), product.name)

    def test_warranty_default_value(self):
        product = Product.objects.create(name="Test products",
                                        description="Test description",
                                        price=255.99)
        self.assertEqual(product.year_warranty, str(1))
        self.assertEqual(product.get_year_warranty_display(), 'none')

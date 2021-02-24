from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import view_cart, add_to_cart, adjust_cart, remove_from_cart


class TestCartUrls(SimpleTestCase):

    def test_cart_url(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)

    def test_add_url(self):
        url = reverse('add_to_cart', args=['some-item'])
        self.assertEquals(resolve(url).func, add_to_cart)

    def test_adjust_url(self):
        url = reverse('adjust_cart', args=['some-item'])
        self.assertEquals(resolve(url).func, adjust_cart)

    def test_remove_url(self):
        url = reverse('remove_from_cart', args=['some-item'])
        self.assertEquals(resolve(url).func, remove_from_cart)

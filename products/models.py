from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


WARRANTY_CHOICES = [('1', 'none'), ('2', '2 years'), ('3', '3 years'),
                    ('5', '5 years'), ('l', 'life')]


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    case = models.CharField(max_length=254, null=True, blank=True)
    strap = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    year_warranty = models.CharField(max_length=1,
                                     choices=WARRANTY_CHOICES, default='1')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

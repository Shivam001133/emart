from django.db import models
from django.utils.translation import gettext_lazy as _


class Categary(models.TextChoices):
    PHONE = 'phone', _("Phone")
    BOOK = 'book', _("Book")


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    dis_price = models.IntegerField()
    categary = models.CharField(choices=Categary.choices,
                                default=Categary.BOOK,
                                max_length=30)
    desc = models.TextField()
    image = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# favorites/models.py

from accounts.models import User
from shops.models import Shop
from django.db import models

class Favorite(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'favorites'
        unique_together = ('shop', 'user')

    def __str__(self):
        return f"{self.user} のお気に入り: {self.shop.name}"

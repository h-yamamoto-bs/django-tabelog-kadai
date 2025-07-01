from django.db import models
from accounts.models import User

class Shop(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    seat_count = models.PositiveIntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'shops'

    def __str__(self):
        return f"{self.name}（{self.address}）"

# 画像情報
# class Image(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     image = models.ImageField(upload_to='shop_images/')
#
#     class Meta:
#         db_table = 'images'
#
#     def __str__(self):
#         return f"{self.shop.name} の画像"

# 店舗ごとのカテゴリー情報
# from categories.models import Category
# class ShopCategory(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
#
#     class Meta:
#         db_table = 'shop_categories'
#         unique_together = ('shop', 'category')
#
#     def __str__(self):
#         return f"{self.shop.name} - {self.category.name}"

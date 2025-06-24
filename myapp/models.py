from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# ユーザー情報
class User(AbstractBaseUser):
    job = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField()

# サブスクリプションに関する情報
# class Subscription(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, unique=True)
#     start_date = models.DateField(auto_now_add=True, null=False, blank=False)
#     end_date = models.DateField(null=False, blank=False)
#
#    class Meta:
#        db_table = 'subscriptions'

# 店舗情報
class Shop(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    seats = models.IntegerField(null=False, blank=False)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'shops'

# 画像情報
# class Image(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     image = models.ImageField(upload_to='shop_images/')

#     class Meta:
#         db_table = 'images'

# お気に入り情報
# class Favorite(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

#     class Meta:
#         db_table = 'favorites'
#         unique_together = ('shop', 'user')

# 選択できるカテゴリー情報
# class Category(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False, unique=True)

#     class Meta:
#         db_table = 'categories'

# 店舗ごとのカテゴリー情報
# class ShopCategory(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

#     class Meta:
#         db_table = 'shop_categories'
#         unique_together = ('shop', 'category')

# レビュー情報
# class Review(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     rating = models.IntegerField(null=False, blank=False)
#     comment = models.TextField()

#     class Meta:
#         db_table = 'reviews'

# 予約情報
# class Reservation(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
#     date = models.DateTimeField(null=False, blank=False)
#     number_of_people = models.IntegerField(null=False, blank=False)

#     class Meta:
#         db_table = 'reservations'
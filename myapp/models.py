from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# ユーザー情報
class UserManager(BaseUserManager):
    def create_user(self, mail, password=None, **extra_fields):
        if not mail:
            raise ValueError('メールアドレスは必須です')
        user = self.model(mail=self.normalize_email(mail), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, password=None, **extra_fields):
        extra_fields.setdefault('manager_flag', True)
        user = self.create_user(mail, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    mail = models.EmailField(unique=True)
    manager_flag = models.BooleanField(default=False)  # Shop管理者かどうか
    job = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mail'
    # REQUIRED_FIELDS = ['job', 'birth_year']  # 必要に応じて

    objects = UserManager()

    def __str__(self):
        return f"{self.mail} ({'管理者' if self.manager_flag else '一般'})"

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

# サブスクリプションに関する情報
# class Subscription(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
#     start_date = models.DateField(auto_now_add=True, null=False, blank=False)
#     end_date = models.DateField(null=False, blank=False)

#     class Meta:
#         db_table = 'subscriptions'

#     def __str__(self):
#         return f"{self.user} のサブスクリプション（{self.start_date}〜{self.end_date}）"

# 店舗情報
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

#     class Meta:
#         db_table = 'images'

#     def __str__(self):
#         return f"{self.shop.name} の画像"

# お気に入り情報
# class Favorite(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

#     class Meta:
#         db_table = 'favorites'
#         unique_together = ('shop', 'user')

#     def __str__(self):
#         return f"{self.user} のお気に入り: {self.shop.name}"

# 選択できるカテゴリー情報
# class Category(models.Model):
#     name = models.CharField(max_length=50, null=False, blank=False, unique=True)

#     class Meta:
#         db_table = 'categories'

#     def __str__(self):
#         return self.name

# 店舗ごとのカテゴリー情報
# class ShopCategory(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

#     class Meta:
#         db_table = 'shop_categories'
#         unique_together = ('shop', 'category')

#     def __str__(self):
#         return f"{self.shop.name} - {self.category.name}"

# レビュー情報
# RATING_CHOICES = [(i, '★' * i + '☆' * (5 - i)) for i in range(1, 6)]
# class Review(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     rating = models.IntegerField(
#         choices=RATING_CHOICES,
#         validators=[MinValueValidator(1), MaxValueValidator(5)],
#         null=False,
#         blank=False
#     )
#     comment = models.TextField()

#     class Meta:
#         db_table = 'reviews'

#     def __str__(self):
#         return f"{self.shop.name} 評価: {self.rating} コメント: {self.comment[:15]}..."

# 予約情報
# class Reservation(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
#     date = models.DateTimeField(null=False, blank=False)
#     number_of_people = models.PositiveIntegerField(null=False, blank=False)

#     class Meta:
#         db_table = 'reservations'

#     def __str__(self):
#         return f"{self.shop.name} {self.date} {self.number_of_people}人 by {self.user}"
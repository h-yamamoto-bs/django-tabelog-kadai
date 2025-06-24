from django.contrib import admin
from .models import User, Shop  # Import your models here
# from .models import Subscription, Image, Favorite, Category, ShopCategory, Review, Reservation

# ユーザー情報の管理
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail', 'manager_flag', 'job', 'birth_year')
    search_fields = ('mail', 'job')
    list_filter = ('manager_flag', 'job', 'birth_year')

# @admin.register(Subscription)
# class SubscriptionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'start_date', 'end_date')
#     search_fields = ('user__mail',)
#     list_filter = ('start_date', 'end_date')

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'seat_count', 'user')
    search_fields = ('name', 'address', 'user__mail')
    list_filter = ('seat_count',)

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'shop', 'image')
#     search_fields = ('shop__name',)

# @admin.register(Favorite)
# class FavoriteAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'shop')
#     search_fields = ('user__mail', 'shop__name')
#     list_filter = ('shop',)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)

# @admin.register(ShopCategory)
# class ShopCategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'shop', 'category')
#     search_fields = ('shop__name', 'category__name')
#     list_filter = ('category',)

# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('id', 'shop', 'rating', 'comment')
#     search_fields = ('shop__name', 'comment')
#     list_filter = ('rating',)

# @admin.register(Reservation)
# class ReservationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'shop', 'user', 'date', 'number_of_people')
#     search_fields = ('shop__name', 'user__mail')
#
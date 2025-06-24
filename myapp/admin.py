from django.contrib import admin
from .models import User, Shop  # Import your models here

# ユーザー情報の管理
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'birth_year')
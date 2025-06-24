from django.core.management.base import BaseCommand
from myapp.models import User, Shop
import random

class Command(BaseCommand):
    help = 'サンプルユーザーと店舗データを自動生成して投入します'

    def handle(self, *args, **options):
        # 既存データ削除（必要に応じてコメントアウト）
        # Shop.objects.all().delete()
        # User.objects.all().delete()

        # ユーザー作成
        users = []
        for i in range(5):
            user = User.objects.create_user(
                mail=f'user{i}@example.com',
                password='password',
                manager_flag=(i % 2 == 0),
                job=random.choice(['エンジニア', 'デザイナー', '営業', '学生']),
                birth_year=random.randint(1980, 2005)
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f'ユーザー{len(users)}件作成'))

        # 店舗作成
        shops = []
        for i in range(10):
            shop = Shop.objects.create(
                name=f'サンプル店舗{i+1}',
                address=f'名古屋市サンプル区{i+1}-1-1',
                seat_count=random.randint(10, 50),
                user=random.choice(users)
            )
            shops.append(shop)
        self.stdout.write(self.style.SUCCESS(f'店舗{len(shops)}件作成'))

        self.stdout.write(self.style.SUCCESS('サンプルデータ投入完了'))

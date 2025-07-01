# # reviews/models.py
# from shops.models import Shop
# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator

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

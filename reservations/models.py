# # reservations/models.py

# from shops.models import Shop
# from accounts.models import User
# from django.db import models

# class Reservation(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=False, blank=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
#     date = models.DateTimeField(null=False, blank=False)
#     number_of_people = models.PositiveIntegerField(null=False, blank=False)

#     class Meta:
#         db_table = 'reservations'

#     def __str__(self):
#         return f"{self.shop.name} {self.date} {self.number_of_people}人 by {self.user}"

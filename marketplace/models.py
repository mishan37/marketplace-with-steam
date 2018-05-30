from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(null=True)
    level = models.IntegerField(null=True)
    country = models.CharField(max_length=50, null=True)
    information = models.CharField(max_length=255, null=True)
    inventory_status = models.IntegerField(null=True)
    inventory_capacity = models.IntegerField(null=True)
    image_link = models.CharField(max_length=255, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
 if created:
  Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
  instance.profile.save()

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    starting_price = models.IntegerField()
    type_item = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image_link = models.CharField(max_length=255, null=True)

class User_Inventory_Item(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_code = models.ForeignKey(Item, on_delete=models.CASCADE)

class Lot(models.Model):
    user_seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_code = models.IntegerField()
    lot_name = models.CharField(max_length=30)
    cost = models.IntegerField()
    item_count = models.IntegerField(null=True)

class Transaction(models.Model):
    user_buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    lot_id = models.ForeignKey(Lot, on_delete=models.PROTECT)
    user_seller_id = models.IntegerField(null=True)
    transaction_date = models.DateTimeField(null=True)
    item_count = models.IntegerField(null=True)
    cost = models.IntegerField(null=True)
    item_name = models.CharField(max_length=50, null=True)
    username_buyer = models.CharField(max_length=100, null=True)
    username_seller = models.CharField(max_length=100, null=True)

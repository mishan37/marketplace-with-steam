from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Lot)
admin.site.register(User_Inventory_Item)
admin.site.register(Transaction)
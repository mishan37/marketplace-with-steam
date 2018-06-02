from django.shortcuts import render
from marketplace import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect

def view_regisration(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        return render(request, 'registration/registration.html', locals())


def view_homepage(request):
   All_Lots = models.Lot.objects.all()
   if request.user.is_authenticated:
      Auth_User = User.objects.get(id=request.user.id)
      User_Lots = models.Lot.objects.filter(user_seller_id=Auth_User.id)
      Items = models.Item.objects.all()
   return render(request, 'homepage/homepage.html', locals())

def view_homepage_sort_weapon(request):
    if request.user.is_authenticated:
        Auth_User = User.objects.get(id=request.user.id)
        Items = models.Item.objects.filter(type_item="Оружие")
        All_Lots = models.Lot.objects.all()
    return render(request, 'homepage/homepage.html', locals())

def view_homepage_sort_armor(request):
    if request.user.is_authenticated:
        Auth_User = User.objects.get(id=request.user.id)
        Items = models.Item.objects.filter(type_item="Броня")
        All_Lots = models.Lot.objects.all()
    return render(request, 'homepage/homepage.html', locals())

def view_homepage_sort_food(request):
    if request.user.is_authenticated:
        Auth_User = User.objects.get(id=request.user.id)
        Items = models.Item.objects.filter(type_item="Пища")
        All_Lots = models.Lot.objects.all()
    return render(request, 'homepage/homepage.html', locals())

def view_homepage_search_item(request):
    if request.user.is_authenticated:
        Search_Item = request.POST["input_search_item"]
        Auth_User = User.objects.get(id=request.user.id)
        Items = models.Item.objects.filter(item_name__contains=Search_Item)
        All_Lots = models.Lot.objects.all()
    return render(request, 'homepage/homepage.html', locals())

def view_authorization(request):
   #print(request.session)
   if request.user.is_authenticated:
    return redirect('/')
   else:
    return render(request, 'authorization/authorization.html', locals())


def view_user_profile(request, user_id):
   if request.user.is_authenticated:
    Auth_User = User.objects.get(id=request.user.id)
   Profile_User = User.objects.get(id=user_id)
   Selling = models.Transaction.objects.filter(user_seller_id=Profile_User.id)
   return render(request, 'user/profile.html', locals())


def view_user_inventory(request, user_id):
   if request.user.is_authenticated:
     Auth_User = User.objects.get(id=request.user.id)
     Owner_User = User.objects.get(id=user_id)
     User_Items = models.User_Inventory_Item.objects.filter(user_id_id=user_id)
     User_Item = User_Items.first()
     try:
      Item = models.Item.objects.get(id=User_Item.item_code_id)
     except models.User_Inventory_Item.DoesNotExist:
      Item = None  
     Items = models.Item.objects.all()
     Lots = models.Lot.objects.all()
     return render(request, 'user/inventory.html', locals())
   else:
     return redirect('/')

def view_user_inventory_item(request, user_item_id, user_id):
    if request.user.is_authenticated:
     Auth_User = User.objects.get(id=request.user.id)
     Owner_User = User.objects.get(id=user_id)
     User_Items = models.User_Inventory_Item.objects.filter(user_id_id=Owner_User.id)
     Items = models.Item.objects.all()
     Lots = models.Lot.objects.all()
     User_Item = models.User_Inventory_Item.objects.get(id=user_item_id)
     try:
      Item = models.Item.objects.get(id=User_Item.item_code_id)
     except models.User_Inventory_Item.DoesNotExist:
      Item = None
     return render(request, 'user/inventory.html', locals())
    else:
     return redirect('/')

def view_user_transaction(request):
   Auth_User = models.User.objects.get(id=request.user.id)
   if request.user.is_authenticated:
      User_Transactions = models.Transaction.objects.filter(Q(user_seller_id=request.user.id) | Q(user_buyer_id=request.user.id))
   return render(request, 'user/transaction.html', locals())


def view_lot(request, lot_id):
   Link_Lot = models.Lot.objects.get(id=lot_id)
   if Link_Lot.item_count != 0:
    Item_Lot = models.Item.objects.get(id=Link_Lot.item_code)
    Auth_User = User.objects.get(id=request.user.id)
    return render(request, 'lot/lot.html', locals())
   else:
    return redirect('/')

def view_user_edit_profile(request, user_id):
    Auth_User = models.User.objects.get(id=request.user.id)
    if Auth_User.id == user_id:
     return render(request, 'user/edit_profile.html', locals())
    else:
     return redirect('/')
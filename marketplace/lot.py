from marketplace import models
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render
import datetime

def lotitem(request, lots_id):
 lot_id = request.POST['lot_id']
 if 'buy_item' in request.POST:
     user_seller_id = request.POST['user_seller_id']
     item_count = request.POST['count_input']
     item_cost = request.POST['cost_item']
     item_code = request.POST['item_code']


     User_seller = User.objects.get(id=user_seller_id)
     User_seller.profile.money = User_seller.profile.money + int(item_count)*int(item_cost)
     User_seller.save()

     User_buyer = User.objects.get(id=request.user.id)
     models.Profile.user = User_buyer
     User_buyer.profile.money = User_buyer.profile.money - int(item_count)*int(item_cost)
     User_buyer.save()

     New_User_Item = models.User_Inventory_Item.objects.filter(user_id_id=User_buyer.id, item_code_id=item_code)
     try:
      New_User_Item = models.User_Inventory_Item.objects.get(user_id_id=User_buyer.id, item_code_id=item_code)
      New_User_Item.quantity = New_User_Item.quantity + int(item_count)
      New_User_Item.save()
     except models.User_Inventory_Item.DoesNotExist:
      New_User_Item = models.User_Inventory_Item()
      New_User_Item.user_id_id = User_buyer.id
      New_User_Item.item_code_id = item_code
      New_User_Item.quantity = item_count
      New_User_Item.save()

     User_Item = models.Item.objects.get(id=item_code)

     New_User_Transaction = models.Transaction()
     New_User_Transaction.user_buyer_id = User_buyer.id
     New_User_Transaction.user_seller_id = user_seller_id
     New_User_Transaction.lot_id_id = lot_id
     New_User_Transaction.transaction_date = datetime.datetime.now()
     New_User_Transaction.item_count = item_count
     New_User_Transaction.cost = item_cost
     New_User_Transaction.item_name = User_Item.item_name
     New_User_Transaction.username_buyer = User_buyer.username
     New_User_Transaction.username_seller = User_seller.username
     New_User_Transaction.save()

     Seller_Lot = models.Lot.objects.get(id=lot_id)
     Seller_Lot.item_count = Seller_Lot.item_count - int(item_count)
     Seller_Lot.save()
     return redirect('/')

 if 'reset_lot' in request.POST:
     Return_Lot = models.Lot.objects.get(id=lot_id)

     try:
      User_Return_Item = models.User_Inventory_Item.objects.get(item_code_id=Return_Lot.item_code, user_id_id=Return_Lot.user_seller_id_id)
      User_Return_Item.quantity = User_Return_Item.quantity + int(Return_Lot.item_count)
      User_Return_Item.save()
     except models.User_Inventory_Item.DoesNotExist:
      User_Return_Item = models.User_Inventory_Item()
      User_Return_Item.user_id_id = Return_Lot.user_seller_id_id
      User_Return_Item.item_code_id = Return_Lot.item_code
      User_Return_Item.quantity = Return_Lot.item_count
      User_Return_Item.save()

     Return_Lot.item_count = 0
     Return_Lot.cost = 0
     Return_Lot.save()
     return redirect('/')

def create(request):
    if request.user.is_authenticated:
      Lot_Price = request.POST['price_input']
      Lot_Quantity = request.POST['quantity_input']
      Lot_Name = request.POST['lot_name_input']
      Lot_Seller_Id = request.POST['seller_id_input']
      Lot_Item_Code = request.POST['item_code_input']

      New_Lot = models.Lot()
      New_Lot.lot_name = Lot_Name
      New_Lot.cost = Lot_Price
      New_Lot.item_count = Lot_Quantity
      New_Lot.user_seller_id_id = Lot_Seller_Id
      New_Lot.item_code = Lot_Item_Code
      New_Lot.save()

      User_Inventory_Item = models.User_Inventory_Item.objects.get(item_code_id=Lot_Item_Code, user_id_id=Lot_Seller_Id)
      User_Inventory_Item.quantity = User_Inventory_Item.quantity - int(Lot_Quantity)
      User_Inventory_Item.save()

      return redirect('http://127.0.0.1:8000/inventory/' + Lot_Seller_Id)
    else:
      return redirect('/')


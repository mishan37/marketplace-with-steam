from marketplace import models
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.sessions.models import Session


def reguser(request):
  username = request.POST['RegUserName']
  password = request.POST['RegPassword']
  email = request.POST['Email']
  NewUser = User.objects.create_user(username=username, email=email, password=password)
  NewUser.save()
  NewUser.profile.inventory_status = 1
  NewUser.profile.inventory_capacity = 200
  NewUser.profile.money = 1000
  NewUser.profile.level = 1
  NewUser.save()
  user = authenticate(username=username, password=password)
  if user is not None:
      if user.is_active:
          login(request, user)
          # Redirect to a success page
          return redirect('/profile/' + str(NewUser.id))
      else:
          # Return a 'disabled account' error message
          return redirect('/')
  else:
      return redirect('/')



def login_user(request):
    username = request.POST['AuthUserName']
    password = request.POST['AuthPassword']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page
            return redirect('/profile/' + str(user.id))
        else:
            # Return a 'disabled account' error message
            return render(request,'homepage/homepage.html', {"massage": "Неверный логин или пароль!"})
    else:
        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')

def change_user(request, user_id):
    if request.user.is_authenticated & (request.user.id == user_id):
     Auth_User = User.objects.get(id=user_id)
     username = request.POST['inputEditUserName']
     password = request.POST['EditPassword']
     country = request.POST['EditCountry']
     first_name = request.POST['EditFirstName']
     last_name = request.POST['EditLastName']
     info = request.POST['EditInformation']
     image_link = request.POST['EditImageLink']
     Auth_User.username = username
     if password != "":
         Auth_User.password = password
     Auth_User.profile.country = country
     Auth_User.first_name = first_name
     Auth_User.last_name = last_name
     Auth_User.profile.information = info
     Auth_User.profile.image_link = image_link
     Auth_User.save()
    return redirect('/profile/' + str(user_id))

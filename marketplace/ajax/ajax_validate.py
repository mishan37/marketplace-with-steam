from django.http import JsonResponse
from marketplace import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def validate_username(request):
    username = request.GET['username']
    data = {
        'is_username': User.objects.filter(username=username).exists(),
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET['email']
    data = {
        'is_email': User.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

def edit_validate_username(request):
    username = request.GET['username']
    Auth_User = User.objects.get(id=request.user.id)

    if User.objects.filter(username=username).exists() & (username != Auth_User.username):
        data = {
            'is_username': True,
        }

    else:
       data = {
            'is_username': False,
       }
    print(data)
    return JsonResponse(data)


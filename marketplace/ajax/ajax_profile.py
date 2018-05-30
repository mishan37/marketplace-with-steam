from django.http import JsonResponse
from marketplace import models
from django.contrib.auth.models import User

def profile_activity(request):
    user_id = request.GET['user_id']
    user_transactions = models.Transaction.objects.filter(user_seller_id=user_id)
    data = {
        'selling': user_transactions.count()
    }
    return JsonResponse(data)
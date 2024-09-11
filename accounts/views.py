from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import User

@csrf_exempt
def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    User.objects.create_user(username=username, password=password)
    return JsonResponse({'message': 'signup completed'})
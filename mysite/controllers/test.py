from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    # returrn dummy json data with name and age
    data = {
        'name': 'Rafay',
        'age': 23
    }
    return JsonResponse(data)
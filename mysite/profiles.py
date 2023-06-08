from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def api_view(request):
    if request.method == 'POST':
        # Process the API request here
        return JsonResponse(request.POST)
    else:
        return JsonResponse({'message': 'Invalid request method'})
 
@csrf_exempt   
def api_view2(request):
    
    if request.method == 'POST':
        # Process the API request here
        return JsonResponse(request.POST)
    else:
        return JsonResponse({'message': 'Invalid request method'})
from django.http import JsonResponse
# import item from models
from item.models import Item
from django.views.decorators.csrf import csrf_exempt

def getitem(request):
    # get all items
    items = Item.objects.all()
    # convert to json
    data = {'items': list(items.values('name', 'price', 'quantity'))}
    return JsonResponse(data)

@csrf_exempt
def additem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        # create item
        item = Item(name=name, price=price, quantity=quantity)
        item.save()
        return JsonResponse({'message': 'Item added successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def updateitem(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        # get item
        item = Item.objects.get(id=id)
        item.name = name
        item.price = price
        item.quantity = quantity
        item.save()
        return JsonResponse({'message': 'Item updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})
    
@csrf_exempt     
def deleteitem(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        # get item
        item = Item.objects.get(id=id)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})

@csrf_exempt
def getitembyid(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            item = Item.objects.get(id=id)
            data = {'item': {'name': item.name, 'price': item.price, 'quantity': item.quantity}}
            print(item)
            # return JsonResponse(item)
        except Item.DoesNotExist:
            return JsonResponse({'message': 'Item not found'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
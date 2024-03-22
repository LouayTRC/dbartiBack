import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Category


def addCategory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if name:
            category = Category(name=name)
            try:
                category.save()
                return JsonResponse({'message': 'Category created successfully'}, status=201)
            except Exception as e:
                print('Error:', e)
                return JsonResponse({'error': 'Failed to save category'}, status=500)
        else:
            return JsonResponse({'error': 'Name is required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def getCategorys(request): 
    if request.method == 'GET':
        categories = Category.objects.all()
        data = [{'id': str(category.id), 'name': category.name} for category in categories]
        return JsonResponse(data, safe=False,status=200)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)





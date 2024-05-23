import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Category, Recipe
 

def addCategory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        if name:
            category = Category(name=name)
            try:
                category.save()

                category_dict = {
                    'id': str(category.id),  
                    'name': category.name
                }
                return JsonResponse(category_dict,safe=False, status=201)
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



def updateCategory(request, categoryId):
    if request.method == 'PUT':
        try:
            category = Category.objects.get(id=categoryId)
            data = json.loads(request.body)
            name = data.get('name')
            if name:
                category.name = name
                category.save()
                category_dict = {
                    'id': str(category.id),
                    'name': category.name
                }
                return JsonResponse(category_dict,safe=False, status=200)
            else:
                return JsonResponse({'error': 'Name is required'}, status=400)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=404)
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'error': 'Failed to update category'}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)

def deleteCategory(request, categoryId):
    if request.method == 'DELETE':
        try:
            category = Category.objects.get(id=categoryId)
            category.delete()
            recipes=Recipe.objects.all()
            if(recipes):
                for r in recipes:
                    if(r.category==categoryId):
                        r.delete()
            return JsonResponse({'message': 'Category deleted successfully'}, status=200)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=404)
        except Exception as e:
            print('Error:', e)
            return JsonResponse({'error': 'Failed to delete category'}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

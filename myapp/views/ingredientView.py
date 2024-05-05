import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Ingredient

def addIngredient(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')

        if name:
            try:
                ingredient = Ingredient.objects.create(name=name)
                return JsonResponse({'message': 'Ingredient created successfully'}, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Name is required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def getAllIngredients(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        ingredient_list = [{'name': ingredient.name} for ingredient in ingredients]
        return JsonResponse({'ingredients': ingredient_list}, status=200)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)


def updateIngredientById(request, ingredient_id):
    if request.method == 'PUT':
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            data = json.loads(request.body)
            name = data.get('name')

            if name:
                ingredient.name = name
                ingredient.save()
                return JsonResponse({'message': 'Ingredient updated successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Name is required'}, status=400)
        except Ingredient.DoesNotExist:
            return JsonResponse({'error': 'Ingredient does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)


def deleteIngredientById(request, ingredient_id):
    if request.method == 'DELETE':
        try:
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            ingredient.delete()
            return JsonResponse({'message': 'Ingredient deleted successfully'}, status=200)
        except Ingredient.DoesNotExist:
            return JsonResponse({'error': 'Ingredient does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)
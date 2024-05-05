import json
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Recipe
from myapp.models import Category

def addRecipe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        duration = data.get('duration')
        pic = data.get('pic')
        nbCalories = data.get('nbCalories')
        category_name = data.get('category')
        tuto = data.get('tuto')
        if title and description and duration and pic and nbCalories and category_name:
            try:
                category = Category.objects.get(name=category_name)
                recipe = Recipe.objects.create(title=title, description=description, duration=duration, pic=pic, nbCalories=nbCalories
                , category=category, tuto=tuto)
                return JsonResponse({'message': 'Recipe created successfully'}, status=201)
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Category does not exist'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def getAllRecipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        recipe_list = [{'title': recipe.title, 'description': recipe.description, 'duration': recipe.duration, 'pic': recipe.pic, 'nbCalories': recipe.nbCalories, 'category': recipe.category.name, 'tuto': recipe.tuto} for recipe in recipes]
        return JsonResponse({'recipes': recipe_list}, status=200)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)


def updateRecipeById(request, recipe_id):
    if request.method == 'PUT':
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
            duration = data.get('duration')
            pic = data.get('pic')
            nbCalories = data.get('nbCalories')
            category_name = data.get('category')
            tuto = data.get('tuto')

            if title:
                recipe.title = title
            if description:
                recipe.description = description
            if duration:
                recipe.duration = duration
            if pic:
                recipe.pic = pic
            if nbCalories:
                recipe.nbCalories = nbCalories
            if category_name:
                category = Category.objects.get(name=category_name)
                recipe.category = category
            if tuto:
                recipe.tuto = tuto

            recipe.save()
            return JsonResponse({'message': 'Recipe updated successfully'}, status=200)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe does not exist'}, status=404)
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)


def deleteRecipeById(request, recipe_id):
    if request.method == 'DELETE':
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe.delete()
            return JsonResponse({'message': 'Recipe deleted successfully'}, status=200)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)

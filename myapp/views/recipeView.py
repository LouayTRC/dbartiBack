import json
from bson import ObjectId
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Ingredient, Recipe, User
from myapp.models import Category

def addRecipe(request,userId):
    user = User.objects.get(id=userId)
    if not user:
        raise ValueError("User not found")

    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        duration = data.get('duration')
        pic = data.get('pic')
        nbCalories = data.get('nbCalories')
        category = data.get('category')
        tuto = data.get('tuto')
        ingredients=data.get('ingredients')
        if title and description and duration and nbCalories and category and ingredients:
            recipe = Recipe(title=title, description=description, duration=duration, pic=pic, nbCalories=nbCalories
                , category=category, tuto=tuto,ingredients=ingredients,user=user)
            try:
                recipe.save()
                recipe_dict = {
                    "id":str(recipe.id),
                    "title": recipe.title,
                    "description": recipe.description,
                    "duration": str(recipe.duration),
                    "pic": recipe.pic,
                    "nbCalories": str(recipe.nbCalories),
                    "category": recipe.category,
                    "tuto": recipe.tuto,
                    "ingredients":ingredients,
                    'user':user
                }
                return JsonResponse(recipe_dict,safe=False, status=201)
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Category does not exist'}, status=404)
            except Ingredient.DoesNotExist:
                return JsonResponse({'error': 'Ingredient does not exist'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'All fields are required'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


def getAllRecipes(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()

        recipe_list = []
        for recipe in recipes:
            
            
            ingredients_list = []
            for ingredient in recipe.ingredients:
                ingredients_list.append({
                    'id': str(ingredient.id),
                    'name': ingredient.name
                })
            cat=Category.objects.get(id=recipe.category)
            recipe_dict = {
                'id': str(recipe.id),
                'title': recipe.title,
                'description': recipe.description,
                'duration': recipe.duration,
                'pic': recipe.pic,
                'nbCalories': recipe.nbCalories,
                'category': {
                    'id':str(recipe.category),
                    'name':cat.name
                },
                'tuto': recipe.tuto,
                'ingredients': ingredients_list
            }
            recipe_list.append(recipe_dict)

        return JsonResponse(recipe_list, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)



def updateRecipe(request, recipe_id):
    if request.method == 'PUT':
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
            duration = data.get('duration')
            pic = data.get('pic')
            nbCalories = data.get('nbCalories')
            category = data.get('category')
            tuto = data.get('tuto')
            ingredients = data.get('ingredients')

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
            if category:
                recipe.category = category
            if tuto:
                recipe.tuto = tuto
            if ingredients:
                ingredients_ids = [ObjectId(ing_id) for ing_id in ingredients]
                recipe.ingredients = ingredients_ids

            recipe.save()
            return JsonResponse({'message': 'Recipe updated successfully'}, status=200)
        except Recipe.DoesNotExist:
            return JsonResponse({'error': 'Recipe does not exist'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT method is allowed'}, status=405)


def deleteRecipe(request, recipe_id):
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

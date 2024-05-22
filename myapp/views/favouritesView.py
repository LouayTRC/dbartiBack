import json
from django.http import JsonResponse
from myapp.models import Category, Favorites, Recipe, User

def createFavorites(request, idU):
    try:
        user = User.objects.get(id=idU)
        data = json.loads(request.body)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    favorites = Favorites.objects.create(title=data.get('title'),user=user, recipes=[])

    favorites_info={
        'id':str(favorites.id),
        'title':favorites.title,
        'user':{
                'id': str(favorites.user.id),
                'fullname': favorites.user.fullname,
                'username': favorites.user.username,
                'mail': favorites.user.mail
            },
    }
    
    return JsonResponse({'message': 'Favorites created successfully','favourites':favorites_info})

def deleteFavorites(request, idF):
    try:
        favorites = Favorites.objects.get(id=idF)
    except Favorites.DoesNotExist:
        return JsonResponse({'error': 'Favorites not found'}, status=404)
    
    favorites.delete()
    
    return JsonResponse({'message': 'Favorites deleted successfully'})

def addRecipe(request, idF, idR):
    try:
        favorites = Favorites.objects.get(id=idF)
        recipe = Recipe.objects.get(id=idR)
    except (Favorites.DoesNotExist, Recipe.DoesNotExist):
        return JsonResponse({'error': 'Favorites or Recipe not found'}, status=404)
    
    favorites.recipes.append(recipe)
    favorites.save()
    
    return JsonResponse({'message': 'Recipe added to favorites successfully'})

def deleteRecipe(request, idF, idR):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Only DELETE method is allowed'}, status=405)
    
    try:
        favorites = Favorites.objects.get(id=idF)
        recipe = Recipe.objects.get(id=idR)
    except (Favorites.DoesNotExist, Recipe.DoesNotExist):
        return JsonResponse({'error': 'Favorites or Recipe not found'}, status=404)
    
    if recipe in favorites.recipes:
        favorites.recipes.remove(recipe)
        favorites.save()
        return JsonResponse({'message': 'Recipe deleted from favorites successfully'})
    else:
        return JsonResponse({'error': 'Recipe not found in favorites'}, status=404)
    

def getFavorites(request, idU):
    try:
        user = User.objects.get(id=idU)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    favorites = Favorites.objects.filter(user=user)
    
    favorites_list = []
    for favorite in favorites:
        
        recipe_list = []
        for recipe in favorite.recipes:
            
            
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
                    'id':str(cat.id),
                    'name':cat.name
                },
                'tuto': recipe.tuto,
                'ingredients': ingredients_list
            }
            recipe_list.append(recipe_dict)
        favorites_list.append({
            'id': str(favorite.id),
            'title': favorite.title,
            'user':{
                'id': str(favorite.user.id),
                'fullname': favorite.user.fullname,
                'username': favorite.user.username,
                'mail': favorite.user.mail
            },
            'recipes':recipe_list
        })
    return JsonResponse({'favorites': favorites_list})
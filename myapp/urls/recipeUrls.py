from django.urls import path
from ..views import recipeView

urlpatterns = [
    path('add/', recipeView.addRecipe, name='add_recipe'),
    path('get/', recipeView.getAllRecipes, name='get_all_recipes'),
    path('put/<str:recipe_id>/', recipeView.updateRecipe, name='update_recipe'),
    path('delete/<str:recipe_id>/', recipeView.deleteRecipe, name='delete_recipe'),
]

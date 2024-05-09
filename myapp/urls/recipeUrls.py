from django.urls import path
from ..views import recipeView

urlpatterns = [
    path('addRec/', recipeView.addRecipe, name='add_recipe'),
    path('getRec/', recipeView.getAllRecipes, name='get_all_recipes'),
    path('updateRec/<int:recipe_id>/', recipeView.updateRecipeById, name='update_recipe'),
    path('deleteRec/<int:recipe_id>/', recipeView.deleteRecipeById, name='delete_recipe'),
]

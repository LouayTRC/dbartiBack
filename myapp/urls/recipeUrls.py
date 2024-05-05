from django.urls import path
from ..views import RecipeView

urlpatterns = [
    path('addRec/', RecipeView.addRecipe, name='add_recipe'),
    path('getRec/', RecipeView.getAllRecipes, name='get_all_recipes'),
    path('updateRec/<int:recipe_id>/', RecipeView.updateRecipeById, name='update_recipe'),
    path('deleteRec/<int:recipe_id>/', RecipeView.deleteRecipeById, name='delete_recipe'),
]

from django.urls import path
from ..views import ingredientView

urlpatterns = [
    path('addIng/', ingredientView.addIngredient, name='add_ingredient'),
    path('getIng/', ingredientView.getAllIngredients, name='get_all_ingredients'),
    path('updateIng/<int:ingredient_id>/', ingredientView.updateIngredientById, name='update_ingredient'),
    path('deleteIng/<int:ingredient_id>/', ingredientView.deleteIngredientById, name='delete_ingredient'),
]

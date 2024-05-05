from django.urls import path
from ..views import IngredientView

urlpatterns = [
    path('addIng/', IngredientView.addIngredient, name='add_ingredient'),
    path('getIng/', IngredientView.getAllIngredients, name='get_all_ingredients'),
    path('updateIng/<int:ingredient_id>/', IngredientView.updateIngredientById, name='update_ingredient'),
    path('deleteIng/<int:ingredient_id>/', IngredientView.deleteIngredientById, name='delete_ingredient'),
]

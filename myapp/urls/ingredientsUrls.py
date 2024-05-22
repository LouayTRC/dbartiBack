from django.urls import path
from ..views import ingredientView

urlpatterns = [
    path('add/', ingredientView.addIngredient, name='add_ingredient'),
    path('get/', ingredientView.getAllIngredients, name='get_all_ingredients'),
    path('update/<str:ingredient_id>/', ingredientView.updateIngredient, name='update_ingredient'),
    path('delete/<str:ingredient_id>/', ingredientView.deleteIngredient, name='delete_ingredient'),
]

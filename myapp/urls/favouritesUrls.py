from django.urls import path
from ..views import favouritesView

urlpatterns = [
    path('create/<str:idU>/', favouritesView.createFavorites, name='create_favorites'),
    path('getById/<str:idF>/', favouritesView.getFavouritesById, name='create_favorites'),
    path('get/<str:idU>/', favouritesView.getFavorites, name='create_favorites'),
    path('delete/<str:idF>/<str:idR>/', favouritesView.deleteRecipe, name='delete_recipe_from_favorites'),
    path('delete/<str:idF>/', favouritesView.deleteFavorites, name='delete_favorites'),
    path('add/<str:idF>/<str:idR>/', favouritesView.addRecipe, name='add_recipe_to_favorites'),
]

from django.urls import path
from ..views import categoryView

urlpatterns = [
    path('add/',categoryView.addCategory, name='add_category'),
    path('get/',categoryView.getCategorys, name='get_categorys'),
    path('put/<str:categoryId>/',categoryView.updateCategory, name='updateCategory'),
    path('delete/<str:categoryId>/',categoryView.deleteCategory, name='deleteCategory'),
]
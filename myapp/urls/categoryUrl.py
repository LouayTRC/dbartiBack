from django.urls import path
from ..views import categoryView

urlpatterns = [
    path('add/',categoryView.addCategory, name='add_category')
]
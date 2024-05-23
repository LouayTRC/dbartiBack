from django.urls import path
from ..views import userView

urlpatterns = [
    path('signup/',userView.register, name='register'),
    path('login/',userView.login, name='login'),
    path('createAdmin/',userView.createAdmin, name='createAdmin'),
]
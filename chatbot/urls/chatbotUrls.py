# chatbot/urls.py
from django.urls import path
from ..views import chatbotView

urlpatterns = [
    path('', chatbotView.chatbot, name='chatbot'),
]

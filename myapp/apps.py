from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
from django.apps import AppConfig

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'
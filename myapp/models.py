# models.py
from mongoengine import Document, StringField

class Category(Document):
    name = StringField(max_length=100)

    def __str__(self):
        return self.name

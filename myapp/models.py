# models.py
from mongoengine import Document,EmbeddedDocument, StringField,EmbeddedDocumentField

class Category(Document):
    name = StringField(max_length=100)

    def __str__(self):
        return self.name

class User(Document):
    fullname = StringField(max_length=20)
    username = StringField(max_length=10)
    mail = StringField(max_length=20)
    password = StringField(max_length=100)
    role = StringField(max_length=10)

    def __str__(self):
        return "User(fullname='{self.fullname}', username='{self.username}', mail='{self.mail}'"


class Admin(Document):
    user = EmbeddedDocumentField(User)


    def __str__(self):
        return "Admin(user={self.user})"


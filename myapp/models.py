# models.py
from mongoengine import Document, StringField,IntField,DateField,ReferenceField,ListField,ObjectIdField

# Category document
class Category(Document):
    name = StringField(max_length=100)

    def __str__(self):
        return self.name

# User document
class User(Document):
    fullname = StringField(max_length=20)
    username = StringField(max_length=10)
    mail = StringField(max_length=20)
    password = StringField(max_length=100)
    role = StringField(max_length=10)

    def __str__(self):
        return "User(fullname='{self.fullname}', username='{self.username}', mail='{self.mail}'"

# Admin document
class Admin(Document):
    user = ReferenceField(User)


    def __str__(self):
        return "Admin(user={self.user})"

# Comment document
class Comment(Document):
    user = ReferenceField(User)
    description = StringField(max_length=100)
    date = DateField()
    replies = ListField(ReferenceField('self'))

    def __str__(self):
        return "Comment(description='{self.description}', user={self.user}, date={self.date})"

# Post document
class Post(Document):
    _id= ObjectIdField(primary_key=True)
    title = StringField(max_length=20)
    description = StringField(max_length=20)
    nb_likes = IntField()
    comments = ListField(ReferenceField(Comment))
    pic = StringField(max_length=20)
    user = ReferenceField(User)
    date = DateField()

    def __str__(self):
        return "Post(_id='{self._id}', title='{self.title}', description='{self.description}', likes={self.nb_likes}, pic='{self.pic}', user={self.user}, date='{self.date}')"
    

# Recipe document
class Recipe(Document):
    title = StringField(max_length=255)
    description = StringField()
    duration = IntField()
    pic = StringField(max_length=255)
    nbCalories = IntField()
    ingredients = ListField(StringField(max_length=255))
    category = StringField(max_length=100)
    tuto = StringField()

    def __str__(self):
        return self.title



# Ingredient document
class Ingredient(Document):
    name = StringField(max_length=255)
    quantity = StringField(max_length=100)
    unit = StringField(max_length=50)

    def __str__(self):
        return self.name
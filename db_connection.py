from mongoengine import connect

uri = "mongodb+srv://louuu:louuu@cluster0.bar6ave.mongodb.net/test?retryWrites=true&w=majority&ssl=true"

try:
    connect('dbarti', host=uri)
    print("Successfully connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)
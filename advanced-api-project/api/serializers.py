from .models import Author, Book
from rest_framework import serializers
from datetime import datetime


# The Bookserializer is responsible for converting the complex codes to easily readily format that the end user can use with ease
class BookSerializer(serializers.Modelserializer):
    model = Book
    fields = '__all__'


# If a user enters a year that is not the current year the program is going to throw an error requiring the user to input the current year so as to continue to the next step
    def validate_publication_year(self,value):
        if value > datetime.now().year:
            raise serializers.ValidationError('The year cannot be in the future. It must must be the current year')
        return value

# The Author serializer is responsible for converting complex code into easy formatted readily output to the end user
class AuthorSerializer(serializers.Modelserializer):
    books = BookSerializer(many=True, read_only=True)

    model = Author
    fields = ['name']

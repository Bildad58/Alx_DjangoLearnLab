from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


# The Author and book models are related in a way that if the author is deleted all the books that are related to are also deleted.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)


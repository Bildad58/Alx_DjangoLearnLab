from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=100)
#     publication_year = models.IntegerField

#     def __str__(self):
#         return self.title

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=False)
    profile_photo = models.ImageField(blank=False)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("user must have email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user
        


    def create_superuser(self, email, password):
        user = self.create_user(email, password) 
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(blank=False)
    date_of_admission = models.DateField(blank=False)

    class meta():
        Permissions = [
            ('can_view', 'Can view'),
            ('can_create', 'Can create'),
            ('can_edit', 'Can edit'),
            ('can_delete', 'Can delete'),
        ]





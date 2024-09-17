from django.db import models
from django.contrib.auth.models import AbstractUser


class Customuser(AbstractUser):
    bio = models.TextField(max_length= 100)
    profile_picture = models.ImageField(upload_to = 'profile_pictures')
    followers = models.ManyToManyField('self', related_name = 'following', symmetrical = False)

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    bio = models.TextField(max_length= 100)
    profile_picture = models.ImageField(upload_to = 'profile_pictures')
    followers = models.ManyToManyField('self', related_name = 'Followers', symmetrical = False)
    following = models.ManyToManyField('self', symmetrical=False, related_name='Following')


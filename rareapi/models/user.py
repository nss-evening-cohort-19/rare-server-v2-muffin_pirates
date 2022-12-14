from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    profile_image_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    created_on = models.DateField(auto_now=False, auto_now_add=False)
    active = models.BooleanField()
    is_staff = models.BooleanField()

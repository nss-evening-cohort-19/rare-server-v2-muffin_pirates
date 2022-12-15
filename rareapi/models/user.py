import datetime
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
<<<<<<< HEAD
=======

>>>>>>> main
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=1000)
    profile_image_url = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    created_on = models.DateField(("Date"), default=datetime.date.today)
    active = models.BooleanField()
    is_staff = models.BooleanField()

    def __str__(self):
        return self.name

import datetime
from django.db import models
from .user import User
from .category import Category

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
<<<<<<< HEAD
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
=======
    publication_date = models.DateField(("Date"), default=datetime.date.today)
>>>>>>> main
    image_url = models.URLField(max_length=200)
    content = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.name

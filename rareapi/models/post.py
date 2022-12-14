from django.db import models
from .user import User
from .category import Category

class Post(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    models.DateField(auto_now=False, auto_now_add=False)
    image_url = models.URLField(max_length=200)
    content = models.CharField(max_length=1000)
    objects = models.Manager()

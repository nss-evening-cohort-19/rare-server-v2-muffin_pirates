from django.db import models
from .user import User
from .post import Post


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_on = models.DateField(auto_now=False, auto_now_add=False)

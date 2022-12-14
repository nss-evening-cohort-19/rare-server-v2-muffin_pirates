from django.db import models
from .user import User
from .post import Post


class Comment(models.Model):
  author_id = models.ForeignKey(User, on_delete=models.CASCADE)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
  content = models.CharField(max_length=1000)
  created_on = models.DateTimeField(auto_now=True)


  print("Hello")

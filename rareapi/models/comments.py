import datetime
from django.db import models
from .user import User
from .post import Post


class Comment(models.Model):
<<<<<<< HEAD
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_on = models.DateField(auto_now=False, auto_now_add=False)
=======
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_on = models.DateField(("Date"), default=datetime.date.today)

    def __str__(self):
        return self.name
>>>>>>> main

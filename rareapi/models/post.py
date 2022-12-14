from django.db import models

class Post(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    objects = models.Manager()

    def __str__(self):
        return self.name

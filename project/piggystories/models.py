from django.db import models

# Create your models here.
class StoryModel(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200, default="author")
    date = models.DateTimeField(auto_now_add=True)
    summary = models.CharField(max_length = 300)
    content = models.CharField(max_length= 100000)

    def __str__(self):
        return self.title


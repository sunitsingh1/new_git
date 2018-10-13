from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Resources(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=255)
    slug = models.SlugField(unique=True)


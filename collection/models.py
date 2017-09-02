from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Resources(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(max_length=255)
    slug = models.SlugField(unique=True)
    # define a many-to-one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return "{} resource".format(self.slug)

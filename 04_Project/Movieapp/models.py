from django.db import models

# Create your models here.

class Mymovies(models.Model):
    name = models.CharField(null=True,max_length=50)
    description = models.CharField(max_length=60)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

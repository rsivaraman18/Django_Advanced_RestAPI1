from django.db import models

# Create your models here.

class MyMovie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    active  = models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.name

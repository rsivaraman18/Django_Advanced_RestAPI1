from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator  ## For 5Star Field

### User From Django -->
from django.contrib.auth.models import User

class MyStreamPlatform(models.Model):
    name    = models.CharField(max_length=30)
    about   = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

   
    def __str__(self):
        return self.name


class MyWatchlist(models.Model):
    title     = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform  = models.ForeignKey(MyStreamPlatform , on_delete=models.CASCADE , related_name= "watchdetails")
    active    = models.BooleanField(default=True)
    created   = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class MyReview(models.Model):
    reviewer_name = models.ForeignKey(User , on_delete=models.CASCADE)  # This will show the Superuser,staff in Django
    rating      = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist   = models.ForeignKey(MyWatchlist,on_delete=models.CASCADE,related_name='reviewinfo')
    active      = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.watchlist.title}  {self.rating} star"
        #return self.description

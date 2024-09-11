from django.contrib import admin

from . models import *
admin.site.register(MyWatchlist)
admin.site.register(MyStreamPlatform)

admin.site.register(MyReview)
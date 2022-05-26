from curses.ascii import US
from django.contrib import admin
from .models import Category, User,Genre,Movie,MovieShots,Review,Votes
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Review)
admin.site.register(Votes)


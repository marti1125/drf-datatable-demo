from django.contrib import admin
from .models import Album, Artist, Genre

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)


from django.contrib import admin
from .models import User,Artist_Profile,Book_Artist
# Register your models here.
admin.site.register(User)
admin.site.register(Artist_Profile)
admin.site.register(Book_Artist)
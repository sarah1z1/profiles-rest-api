from django.contrib import admin
from .models import User_Profile, ProfileFeedItem

# Register your models here.

admin.site.register(User_Profile)
admin.site.register(ProfileFeedItem)
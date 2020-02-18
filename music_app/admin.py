from django.contrib import admin
from .models import UserProfileInfo,MusicfileInfo,record_user_click
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(MusicfileInfo)
admin.site.register(record_user_click)
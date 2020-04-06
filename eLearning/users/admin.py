from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class userAdmin(admin.ModelAdmin):
    list_display = ('is_professor', 'is_site_admin')

admin.site.register(UserProfile)
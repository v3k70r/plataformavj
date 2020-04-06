from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Course, Chapter

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_created_date', 'user', 'students', 'for_everybody')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_name', 'chapter_created_date', 'course', 'slug')

admin.site.register(Course)
admin.site.register(Chapter)
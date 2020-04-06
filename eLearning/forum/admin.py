from django.contrib import admin
from .models import Topic, Comment

class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic_message', 'author', 'comment_count', 'stamp_created', 'stamp_updated', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'author', 'date_created', 'comment_fk')

admin.site.register(Topic)
admin.site.register(Comment)

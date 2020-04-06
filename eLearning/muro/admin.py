from django.contrib import admin
from .models import Anuncio, Comment

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'imagen', 'author', 'comment_count', 'stamp_created', 'stamp_updated', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'author', 'date_created', 'comment_fk')

admin.site.register(Anuncio)
admin.site.register(Comment)

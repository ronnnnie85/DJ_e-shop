from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'publicated')
    list_filter = ('title',)
    search_fields = ('title',)

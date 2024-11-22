from django.contrib import admin
from .models import Comment, Post, Category

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author__username', 'text')

admin.site.register(Post)
admin.site.register(Category)   

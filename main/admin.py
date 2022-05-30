from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'get_tags' ]
    
    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())

admin.site.register(Category)
admin.site.register(Comment)
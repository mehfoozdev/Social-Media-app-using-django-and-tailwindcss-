from django.contrib import admin
from .models import Post, Comment

# Register your models here.



# admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'last_updated_date']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'caption']
    list_filter = ['created', 'last_updated_date']
    date_hierarchy = 'created'
    ordering = ['created']

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)
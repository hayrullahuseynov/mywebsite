from django.contrib import admin

# Register your models here.
from .models import BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','id','created_at']
admin.site.register(BlogPost,BlogPostAdmin)

from django.contrib import admin
from .models import Post, Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date_posted' , 'image']
    list_filter = ['date_posted']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)

class ProUser(admin.ModelAdmin):
    list_pro = ['user', 'image']
admin.site.register(Profile, ProUser)
# Register your models here.

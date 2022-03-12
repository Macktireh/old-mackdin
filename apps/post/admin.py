from django.contrib import admin
from apps.post.models import Post, Like
from django.utils.translation import gettext_lazy as _

class PostAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'message', 'count_like', 'date_created',)

    ordering = ('-date_created',)
    
    def full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
    def count_like(self, obj):
        return f"{obj.liked.all().count()}"
    
admin.site.register(Post, PostAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post_id', 'value',)
    
    def user_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
    def post_id(self, obj):
        return f"{obj.post.id}"
    
admin.site.register(Like, LikeAdmin)

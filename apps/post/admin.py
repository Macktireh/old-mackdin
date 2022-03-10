from django.contrib import admin
from apps.post.models import Post  
from django.utils.translation import gettext_lazy as _

class PostAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'message', 'date_created',)

    ordering = ('-date_created',)
    
    def full_name(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
    
admin.site.register(Post, PostAdmin)

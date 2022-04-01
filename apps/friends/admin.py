from django.contrib import admin

from apps.friends.models import Relationship


class RelationshipAdmin(admin.ModelAdmin):

    list_display = ('date_created', 'sender', 'receiver', 'status', 'date_updated',)
    list_filter = ('status', 'date_created',)
    list_editable = ('status',)
    ordering = ('-date_created',)


admin.site.register(Relationship, RelationshipAdmin)
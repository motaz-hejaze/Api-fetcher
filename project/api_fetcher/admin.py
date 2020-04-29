from django.contrib import admin
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    """
    a class to customize list view for items
    """

    # columns to display
    list_display = ["id", "public_id", "title", "image_url", ]
    #order ( older first )
    ordering = ('id',)

admin.site.register(Item,ItemAdmin)
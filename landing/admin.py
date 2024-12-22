from django.contrib import admin
from .models import Announcements, Customers


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image_preview')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    ordering = ('-date',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 150px; max-height: 150px;" />'
        return "No Image"

    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'date')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('status', 'date')
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_editable = ('status',)
    list_per_page = 20

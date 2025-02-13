from django.contrib import admin
from .models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # Column order

admin.site.register(Category)
admin.site.register(Page, PageAdmin)  # Register with custom admin class
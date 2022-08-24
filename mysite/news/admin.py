from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published', 'category', 'views', 'favorites', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published','views')
    list_filter = ('category', 'is_published')
    fields = ('title', 'content',  'get_photo', 'photo', 'created_at', 'is_published', 'category', 'views')
    readonly_fields = ( 'created_at','views', 'get_photo')
    save_on_top = True

    @staticmethod
    def get_photo(obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'no photo'


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
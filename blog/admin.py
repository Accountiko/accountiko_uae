from django.contrib import admin
from .models import Blog

from import_export.admin import ImportExportModelAdmin

# Register your models here.
class BlogAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','category',)
    search_fields = ['title',]

admin.site.register(Blog,BlogAdmin)
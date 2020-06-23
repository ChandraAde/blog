from django.contrib import admin
from .models import *
# Register your models here.

class ArtkelInline(admin.TabularInline):
    model = File
    extra = 1

class ArtikelAdmin(admin.ModelAdmin):
    

    list_display = (
        'judul',
        'kategori',
        'author',
        'published',
        'updated',
    )
    readonly_fields = [
        'slug',
        'published',
        'updated',
        ]

    inlines = [ArtkelInline]

class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Artikel',
        'image',
    )

admin.site.register(Artikel, ArtikelAdmin)
admin.site.register(File, FileAdmin)
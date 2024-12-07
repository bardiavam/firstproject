from django.contrib import admin

from home.models import Category, Products


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created','updated',]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products)


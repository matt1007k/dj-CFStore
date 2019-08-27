from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at')


admin.site.register(Category, CategoryAdmin)

from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Standard admin configuration for Recipes.
    Removed Summernote for stability.
    """
    list_display = ('title', 'author', 'status', 'created_at')
    search_fields = ['title', 'ingredients']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}

from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status', 'created_at')
    search_fields = ['title', 'ingredients']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'instructions')

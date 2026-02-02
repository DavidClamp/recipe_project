from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # Exclude 'author' and 'slug' as we set them in the background
        fields = ('title', 'description', 'ingredients', 'instructions', 'status')
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

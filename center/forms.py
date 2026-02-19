# center/forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients', 'instructions', 'status')
        widgets = {
            'ingredients': forms.Textarea(attrs={'id': 'id_ingredients', 'rows': 5}),
            'instructions': forms.Textarea(attrs={'id': 'id_instructions', 'rows': 8}),
            'description': forms.Textarea(attrs={'id': 'id_description', 'rows': 3}),
        }

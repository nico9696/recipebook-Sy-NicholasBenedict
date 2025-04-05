from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields= '__all__'

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields= '__all__'
from django.shortcuts import render
from .models import Ingredient, Recipe, RecipeIngredient

def show_recipes_list(request):
    return render(request, "ledger/recipes_list.html", {"recipes": Recipe.objects.all()})
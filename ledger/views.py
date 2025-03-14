from .models import Ingredient, Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def show_recipes_list(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "ledger/recipes_list.html", {"recipes": Recipe.objects.all()})

def show_ingredients(request, num):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "ledger/ingredients.html", {"ingredients": RecipeIngredient.objects.filter(recipe=num)})
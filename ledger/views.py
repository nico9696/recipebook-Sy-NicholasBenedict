from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

@login_required(login_url='/ledger/login/') # redirects to login page if not logged in
def show_recipes_list(request):
    return render(request, "ledger/recipes_list.html", {"recipes": Recipe.objects.all()})

@login_required(login_url='/ledger/login/')
def show_ingredients(request, num):
    return render(request, "ledger/ingredients.html", {
        "recipe_ingredient": RecipeIngredient.objects.filter(recipe=num),
        "image" : RecipeImage.objects.filter(recipe=num).first()
    })

@login_required(login_url='/ledger/login/')
def add_recipe_form(request, num):
    return render(request, "ledger/add_recipe_form.html")
	
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("recipe_list"))
    return render(request, "ledger/login.html")

def logout_view(request):
    logout(request)
    return render(request, "ledger/login.html")

def add_recipe(request):
    if (request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        
        if recipe_form.is_valid() and ingredient_form.is_valid():
            recipe_form.save # this is for forms.ModelForm
            ingredient_form.save

        return redirect('add_recipe')
    
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()

    return render(request, 'ledger/add_r&i.html', {
        'add_recipe_form': recipe_form,
        'add_ingredient_form': ingredient_form 
    })
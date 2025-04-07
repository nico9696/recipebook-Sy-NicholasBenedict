from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm

@login_required(login_url='/ledger/login/') # redirects to login page if not logged in
def show_recipes_list(request):
    return render(request, "ledger/recipes_list.html", {"recipes": Recipe.objects.all()})

@login_required(login_url='/ledger/login/')
def show_ingredients(request, num):
    return render(request, "ledger/ingredients.html", {
        "recipe_ingredient": RecipeIngredient.objects.filter(recipe=num),
        "image" : RecipeImage.objects.filter(recipe=num).first()
    })
	
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

@login_required(login_url='/ledger/login/')
def add_recipe_and_ingredient(request):
    if (request.method == "POST"):
        recipe_form = RecipeForm(request.POST, prefix="recipe")
        ingredient_form = IngredientForm(request.POST, prefix="ingredient")
        recipe_ingredient_form = RecipeIngredientForm(request.POST, prefix="recipe_ingredient")
        
        if recipe_form.is_valid():
            recipe_form.save() # this is for forms.ModelForm

        if ingredient_form.is_valid():
            ingredient_form.save() 

        if recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save() 

        return redirect('add_recipe_and_ingredient')
    
    recipe_form = RecipeForm(prefix="recipe")
    ingredient_form = IngredientForm(prefix="ingredient")
    recipe_ingredient_form = RecipeIngredientForm(prefix="recipe_ingredient")

    return render(request, 'ledger/add_r&i.html', {
        'add_recipe_form': recipe_form,
        'add_ingredient_form': ingredient_form,
        'add_recipe_ingredient_form': recipe_ingredient_form,
    })

@login_required(login_url='/ledger/login/')
def add_image(request):
    if (request.method == "POST"):
        recipe_image_form = RecipeForm(request.POST)

        if recipe_image_form.is_valid():
            recipe_image_form.save() 

        return redirect('add_recipe_and_ingredient')
        
    recipe_image_form = RecipeImageForm()

    return render(request, 'ledger/add_image.html', {
        'add_image_form': recipe_image_form,
    })
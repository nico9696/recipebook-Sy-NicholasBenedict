from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('id', 'name')  # Shows readable recipe names

admin.site.register(Recipe, RecipeAdmin)
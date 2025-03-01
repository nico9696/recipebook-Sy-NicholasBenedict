from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )
    list_display = ('id', 'name')  

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('id', 'name')  

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient__name', 'quantity') 
    list_display = ('recipe', 'ingredient', 'quantity')  
    list_filter = ('recipe__name', 'ingredient__name')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
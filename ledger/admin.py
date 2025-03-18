from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# used Chatgpt for syntax of this particular class
class RecipeIngredientInline(admin.TabularInline):  
    """Allows editing RecipeIngredient inside RecipeAdmin."""
    model = RecipeIngredient
    extra = 1  

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author', 'created_on', 'updated_on', )
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on', )  

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('id', 'name')  

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient__name', 'quantity') 
    list_display = ('recipe', 'ingredient', 'quantity')  
    list_filter = ('recipe__name', 'ingredient__name')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
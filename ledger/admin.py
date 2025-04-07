from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# used Chatgpt for syntax of this particular class
class RecipeIngredientInline(admin.TabularInline):  
    """Allows editing RecipeIngredient inside RecipeAdmin."""
    model = RecipeIngredient
    extra = 1  

# allows for RecipeImage to be accessed while in Recipe
class RecipeImageInline(admin.TabularInline): 
    model = RecipeImage
    max_num = 1  # max of 1 image per recipe
    readonly_fields = ('image', 'description')
    can_delete = False


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author', 'created_on', 'updated_on', )
    list_display = ('id', 'name', 'author', 'created_on', 'updated_on', )  
    inlines = [RecipeImageInline]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )
    list_display = ('id', 'name')  

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('ingredient__name', 'quantity') 
    list_display = ('recipe', 'ingredient', 'quantity')  
    list_filter = ('recipe__name', 'ingredient__name')

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ('id', 'recipe', 'image', 'description', )  

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
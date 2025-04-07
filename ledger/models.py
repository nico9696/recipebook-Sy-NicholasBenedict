from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name) 
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    created_on = models.DateTimeField(auto_now_add=True) 
    updated_on = models.DateTimeField(auto_now=True)  
    
    def __str__(self):
        return str(self.name) 

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=64)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredient") 

# Create a Profile model by extending the default User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	bio = models.CharField(max_length=255)
     
class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=True, blank=True)
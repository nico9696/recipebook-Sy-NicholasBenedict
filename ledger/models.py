from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) 
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id) 

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=64)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredient") 

# Create a Profile model by extending the default User model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	bio = models.CharField(max_length=255)
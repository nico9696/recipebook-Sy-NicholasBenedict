from django.db import models

# Create your models here.
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
from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list", views.show_recipes_list, name="recipe_list"),
    path("recipe/<int:num>", views.show_ingredients, name="show_ingredients"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list", views.show_recipes_list, name="recipe_list"),
    # path("recipe/1", views.show_ingredients_1, name="show_ingredients_1"),
    # path("recipe/2", views.show_ingredients_2, name="show_ingredients_2"),
]
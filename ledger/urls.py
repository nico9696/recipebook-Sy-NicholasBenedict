from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list/", views.show_recipes_list, name="recipe_list"),
    path("recipe/<int:num>/", views.show_ingredients, name="show_ingredients"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("recipe/add/", views.add_recipe_and_ingredient, name="add_recipe_and_ingredient"),
    path("recipe/<int:pk>/add_image/", views.add_image , name="add_image"),
]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("recipes/list/", views.show_recipes_list, name="recipe_list"),
    path("recipe/<int:num>/", views.show_ingredients, name="show_ingredients"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render

def show_recipes_list(request):
    recipes = [
        {
            "name": "Recipe 1",
            "link": "/ledger/recipe/1"
        },
        {
            "name": "Recipe 2",
            "link": "/ledger/recipe/2"
        }
    ]
    
    return render(request, "ledger/recipes_list.html", {"recipes": recipes})
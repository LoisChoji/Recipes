from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allrecipes
from django.template import loader

# Create your views here.
def Recipes(request):
    ar = Allrecipes.objects.all() #ar is just a variable for allrecipes
    template = loader.get_template('food_recipes/recipes.html')

    context={
        'ar': ar,
    }
    return HttpResponse(template.render(context, request))

def detail(request, recipe_id):
    try:
        recipe = Allrecipes.objects.get(pk = recipe_id)
    except Allrecipes.DoesNotExist:
        raise Http404("Recipe does not exist")

    return render(request, 'food_recipes/detail.html', {'recipe':recipe})

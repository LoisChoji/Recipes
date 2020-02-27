from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def Recipes(request):
    return HttpResponse('this is my view')
    x = Allrecipes.objects.all()
    template = loader.get_template('')
    return HttpResponse('')

def detail(request, recipe_id):
    return HttpResponse("this is the recipe detail page" + str(recipe_id))

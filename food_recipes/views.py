from django.shortcuts import render
from djano.http import httpResponse

# Create your views here.
def Recipes(request):
    return httpResponse("this is my view")

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Recipes
from .forms import RecipesForm


def home(request):
    Recipe_list = Recipes.objects.order_by('id')
    return render(request,"app_recipe/home.html", {'Recipe_list':Recipe_list})

def create(request):
    if request.method == 'POST':
        obj_creat =RecipesForm(request.POST)
        if obj_creat.is_valid():
            recipe_name = request.POST.get('recipe_name','')
            ingredient_list = request.POST.get('ingredient_list', '')
            making_process = request.POST.get('making_process', '')
            data = Recipes(recipe_name= recipe_name,
                          ingredient_list = ingredient_list,
                          making_process = making_process)
            data.save()
            return redirect('/home')
        else:
            return HttpResponse('data invalid')
    else:
        form = RecipesForm()
        return render (request,"app_recipe/creat.html" ,{'form': form})

def delete(request, id):
    Recipe_list = get_object_or_404(Recipes, pk = id)
    Recipe_list.delete()
    return redirect('/home')

def details(request, id):
    Recipe_list = get_object_or_404(Recipes, pk=id)
    return render(request, "app_recipe/details.html" , {'Recipe_list': Recipe_list})
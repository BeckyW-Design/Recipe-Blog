from django.shortcuts import render
from django.contrib import messages
from .forms import RecipeUploadForm, IngredientForm
from django.forms import modelformset_factory
from blog.models import Ingredient
from .models import RecipeUpload

def recipe_upload(request):
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=1)

    if request.method == "POST":
        recipe_form = RecipeUploadForm(request.POST, request.FILES)
        ingredient_formset = IngredientFormSet(request.POST)

        
        if recipe_form.is_valid() and ingredient_formset.is_valid():
        
            recipe = recipe_form.save()

            
            for form in ingredient_formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = recipe  
                ingredient.save()

            messages.success(request, 'Recipe uploaded successfully!')
            return render(request, 'about/thank_you.html')

    else:
        
        recipe_form = RecipeUploadForm()
        ingredient_formset = IngredientFormSet(queryset=Ingredient.objects.none())

    return render(
        request,
        'about/about.html',
        {'recipe_upload_form': recipe_form, 'ingredient_formset': ingredient_formset}
    )
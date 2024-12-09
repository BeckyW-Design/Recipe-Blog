from django.shortcuts import render
from django.contrib import messages
from .forms import RecipeUploadForm
from django.forms import modelformset_factory
from .models import RecipeUpload

def recipe_upload(request):
    
    if request.method == "POST":
        recipe_form = RecipeUploadForm(request.POST, request.FILES)
                
        if recipe_form.is_valid():
                recipe = recipe_form.save()
                messages.success(request, 'Recipe uploaded successfully!')
        return render(request, 'about/thank_you.html')

    else:
        
        recipe_form = RecipeUploadForm()

    return render(
        request,
        'about/about.html',
        {'recipe_upload_form': recipe_form}
    )
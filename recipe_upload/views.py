from django.shortcuts import render
from django.contrib import messages
from .models import RecipeUpload
from .forms import RecipeUploadForm


def recipe_upload(request):
    
    if request.method == "POST":
        recipe_form = RecipeUploadForm(request.POST)        
        if recipe_form.is_valid():
                recipe = recipe_form.save()
                recipe.author = request.user
                messages.add_message(request, messages.SUCCESS, "Recipe uploaded successfully!")
                messages.success(request, 'Recipe uploaded successfully!')
        return render(request, 'recipe_upload/upload.html')
    else:
        
        recipe_form = RecipeUploadForm()

    return render(
        request,
        'about/about.html',
        {'recipe_upload_form': recipe_form}
    )
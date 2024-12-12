from django import forms
from .models import RecipeUpload


class RecipeUploadForm(forms.ModelForm):
    """
    Form class for users to request a collaboration
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = RecipeUpload
        fields = ('title', 'featured_image', 'servings', 'timings',
        'ingredient', 'content', 'category')

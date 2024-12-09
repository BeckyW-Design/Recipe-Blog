from django import forms
from blog.models import Ingredient
from .models import RecipeUpload
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RecipeUploadForm(forms.ModelForm):
    class Meta:
        model = RecipeUpload
        fields = ['title', 'author', 'featured_image', 'servings', 'timings', 'content', 'category', 'ingredient', 'quantity', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Ingredient', css_class='btn btn-secondary'))
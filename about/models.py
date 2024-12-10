from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class RecipeUpload(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_uploads"
    )
    featured_image = CloudinaryField('image', default='placeholder', blank=True)
    servings = models.IntegerField(null=True)
    timings = models.IntegerField(null=True)
    content = models.TextField(null=True)
    ingredient = models.TextField(null=True)
    category_choices = [
        ('GF', 'Gluten Free'),
        ('QM', '20mins or less'),
        ('Vg', 'Vegan'),
        ('V', 'Vegetarian')

    ]
    category = models.CharField(max_length=2, choices=category_choices, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Thank you for your recipe {self.title}"


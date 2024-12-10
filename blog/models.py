from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    serving = models.IntegerField(null=True)
    timing = models.IntegerField(null=True)
    content = models.TextField(null=True)
    category_choices = [
        ('GF', 'Gluten Free'),
        ('QM', '20mins or less'),
        ('Vg', 'Vegan'),
        ('V', 'Vegetarian')
    ]
    category = models.CharField(max_length=2, choices=category_choices, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Ingredient(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="ingredient")
    name = models.CharField(max_length=150)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)

    unit_choices = [
        ("grams","Grams"),
        ("kilograms","Kilograms"),
        ("cups","Cups"),
        ("tablespoon","Tablespoon"),
        ("teaspoon","Teaspoon"),
        ("small", "Small"),
        ("medium", "Medium"),
        ("large","Large"),
    ]

    unit = models.CharField(max_length=20, choices=unit_choices, default="grams", blank=True, null=True)    

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
        related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
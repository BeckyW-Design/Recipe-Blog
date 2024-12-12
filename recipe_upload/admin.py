from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RecipeUpload


@admin.register(RecipeUpload)
class RecipeUploadAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)
    
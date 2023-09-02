from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Category, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'author',
            'title',
            'text',
            # 'categoryType',
            'postCategory',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if title[0].islower():
            raise ValidationError({
                'title': 'The title should start with uppercase letter'
            })

        return cleaned_data
    

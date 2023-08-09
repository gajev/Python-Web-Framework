from django import forms
from .models import Story


class BaseStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['date', 'overall', 'health', 'love', 'work', 'description', 'favorite_story', 'picture']
        labels = {
            'date': 'Date',
            'overall': 'Overall',
            'health': 'Health',
            'love': 'Love',
            'work': 'Work',
            'description': 'Description',
            'favorite_story': 'Favorite Story',
            'picture': 'Picture'
        }
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Tell me how was your day ...',
                }
            ),
            'picture': forms.URLInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class AddStoryForm(BaseStoryForm):
    pass


class EditStoryForm(BaseStoryForm):
    pass

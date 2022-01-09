from django import forms
from .models import StoryModel
 
 
# creating a form
class StoryForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = StoryModel
 
        # specify fields to be used
        fields = [
            "title",
            "summary",
            "content",
        ]
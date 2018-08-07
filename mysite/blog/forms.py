from django import forms

from .models import MysitePost

class PostForm(forms.ModelForm):

    class Meta:
        model = MysitePost
        fields = ('title', 'text',)
    

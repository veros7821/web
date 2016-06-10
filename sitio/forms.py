from django import forms
from .models import Posteo

class PostForm(forms.ModelForm):

    class Meta:
        model = Posteo
        fields = ('titulo', 'texto')
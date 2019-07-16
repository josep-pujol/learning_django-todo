from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta: # inner class for additional info needed for Django
        model = Item
        fields = ('name', 'done')
        

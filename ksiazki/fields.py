from django import forms

from .models import ksiazki


class ksiazkiForm(forms.ModelForm):
    class Meta:
        model = ksiazki
        fields = [
            'tytuł',
            'autor',
            'ISBN',
            'data',
            'strony',
            'jezyk',
            'link'
        ]

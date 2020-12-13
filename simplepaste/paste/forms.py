from django import forms
from .models import PasteBox


class PasteForm(forms.ModelForm):
    paste = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 15, "cols": 120}))

    class Meta:
        model = PasteBox

        fields = {'title', 'paste'}

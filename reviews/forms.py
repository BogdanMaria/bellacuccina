from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Review
        fields = ['id', 'content']
        widgets = {
            'content': forms.Textarea(attrs={"rows": 4})
        }

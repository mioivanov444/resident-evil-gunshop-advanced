from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        fields = ['text', 'rating']

        labels = {
            'text': 'Review',
            'rating': 'Rating (1-5)',
        }

        help_texts = {
            'rating': 'Enter a number from 1 (worst) to 5 (best).',
        }

        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your review here...',
                'class': 'form-control'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'class': 'form-control'
            }),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if rating is None:
            raise forms.ValidationError("Rating is required.")

        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")

        return rating
from core.models import *
from django import forms

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model=ProductReview
        fields=['review','rating']
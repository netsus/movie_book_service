from django import forms
from reviews.models import Review

class CreateReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = (
      "rating",
      "text", 
    )
  

  # def save(self, *args, **kwargs):
  #   review = super().save(commit=False)
  #   text = self.cleaned_data.get("text")
  #   rating = self.cleaned_data.get("rating")

  #   review.text = text
  #   review.rating = rating
  #   return review

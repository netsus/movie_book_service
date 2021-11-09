from django.urls import path
from reviews.views import create_review

app_name="reviews"

urlpatterns = [
  path("update/<int:pk>", create_review, name="add"),
]
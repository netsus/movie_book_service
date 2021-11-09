from django.shortcuts import render, redirect, reverse
from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.generic import FormView
from reviews.models import Review
from movies.models import Movie
from books.models import Book


def create_review(request, pk):
  kind = request.GET.get('kind')
  user = request.user
  if request.method == "POST":

    if user.is_authenticated: #  and form.is_valid()
      
      if kind == 'movie':
        movie = Movie.objects.get(pk=pk)
        review_list = Review.objects.filter(created_by=user, movie=movie)

        if review_list: # 리뷰가 있을때
          review_list.delete()
          return redirect(reverse('movies:movie', kwargs={'pk': pk}))
        else: # 리뷰가 없을 때
          review_list = Review.objects.create(created_by=user, movie=movie)
          review_list.text = request._post['text']
          review_list.rating = int(request._post['rating'])
          review_list.save()
          return redirect(reverse('movies:movie', kwargs={'pk': pk}))
      else:
        book = Book.objects.get(pk=pk)
        review_list = Review.objects.filter(created_by=user, book=book)
        if review_list: # 리뷰가 있을때
          review_list.delete()
          return redirect(reverse('books:book', kwargs={'pk': pk}))
        else:
          review_list = Review.objects.create(created_by=user, book=book)
          review_list.text = request._post['text']
          review_list.rating = int(request._post['rating'])
          review_list.save()
          return redirect(reverse('books:book', kwargs={'pk': pk}))
  
    else:
      return redirect(reverse('core:home'))
  else:
    return redirect(reverse('core:home'))
    

# class UpdateReview(UpdateView):
#     model = Review
#     template_name = "reviews/review_form.html"
#     fields = (
#       "rating",
#       "text",
#     )

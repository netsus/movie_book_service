from django import template
from reviews.models import Review

register = template.Library()

@register.simple_tag(takes_context=True)
def on_reviews(context, thing):
  user = context.request.user
  obj = context.dicts[-1]['obj']
  kind = context.dicts[-1]['kind']
  if kind == 'movie':
    review_li_mov = Review.objects.filter(
        created_by=user, movie=obj
    )
    return bool(sum([1 if thing == qs.movie else 0 for qs in review_li_mov]))
  elif kind == "book":
    review_li_bok = Review.objects.filter(
        created_by=user, book=obj
    )
    return bool(sum([1 if thing == qs.book else 0 for qs in review_li_bok]))

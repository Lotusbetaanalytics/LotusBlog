from django.urls import path
from .views import CommentView, BlogView

urlpatterns = [
    path('comment/<blog_id>/', CommentView.as_view()),
    path('post/', BlogView.as_view()),
    path('post/<blog_id>/', BlogView.as_view()),
]
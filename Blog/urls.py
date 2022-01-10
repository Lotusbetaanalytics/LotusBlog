from django.urls import path
from .views import (
    # CommentView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView,
    BlogListCreateView,
    BlogRetrieveUpdateDestroyView
)

urlpatterns = [
    path('post/', BlogListCreateView.as_view()),
    path('post/<blog_id>/', BlogRetrieveUpdateDestroyView.as_view()),
    path('post/<blog_id>/comment/', CommentListCreateView.as_view()),
    path('comment/<comment_id>/', CommentRetrieveUpdateDestroyView.as_view()),
]

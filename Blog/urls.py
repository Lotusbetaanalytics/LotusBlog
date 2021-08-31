from django.urls import path
from .views import CommentView, BlogView

urlpatterns = [
    path('comment/<blog_id>/', CommentView.as_view()),
    path('<blog_id>/', BlogView.as_view()),
    path('blogs/', BlogView.as_view()),
]
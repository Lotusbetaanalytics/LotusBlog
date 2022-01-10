from .models import Comment, BlogPost
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
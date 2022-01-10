from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CommentSerializer, BlogPostSerializer
from .models import Comment, BlogPost
# Create your views here.


# class CommentView(CreateAPIView):
#     queryset = Comment.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = CommentSerializer


#     def post(self, request, **args):
#         blog = BlogPost.objects.get(id=args['blog_id'])
#         if blog:
#             request.data['blog'] = args['blog_id']
        
#             serializer_class = CommentSerializer(data=request.data)
#             serializer_class.is_valid(raise_exception=True)
#             serializer_class.save()
#             response = {
#                 'success': True,
#                 'status_code': status.HTTP_200_OK,
#                 'message': 'Comment Created'
#             }

#             status_ = status.HTTP_200_OK

#         else:
#             response = {
#                 'success': True,
#                 'status_code': status.HTTP_404_NOT_FOUND,
#                 'message': 'Blog not found'
#             }

#             status_ = status.HTTP_404_NOT_FOUND
        
#         return Response(response, status=status_)


#     def get(self, request, **args):
#         comments_ = []
#         comment_objects = Comment.objects.filter(blog=args['blog_id'])
#         for comment in comment_objects:
#             data = {
#                 "id": comment.id,
#                 "name": comment.name,
#                 "email": comment.email,
#                 "commnet": comment.comment
#             }

#             comments_.append(data)

#         response = {
#                 'success': True,
#                 'status_code': status.HTTP_200_OK,
#                 'message': 'comments fetched!',
#                 'data': comments_
#             }

#         status_ = status.HTTP_200_OK
#         return Response(response, status_)


class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer

    def post(self, request, **args):
        blog = BlogPost.objects.get(id=args['blog_id'])
        if blog:
            request.data['blog'] = args['blog_id']
        
            serializer_class = CommentSerializer(data=request.data)
            serializer_class.is_valid(raise_exception=True)
            serializer_class.save()
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Comment Created'
            }
            status_ = status.HTTP_200_OK
        else:
            response = {
                'success': True,
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Blog not found'
            }
            status_ = status.HTTP_404_NOT_FOUND
        
        return Response(response, status=status_)


    def get(self, request, **args):
        comments_ = []
        comment_objects = Comment.objects.filter(blog=args['blog_id'])
        for comment in comment_objects:
            data = {
                "id": comment.id,
                "name": comment.name,
                "email": comment.email,
                "commnet": comment.comment
            }
            comments_.append(data)

        response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'comments fetched!',
                'data': comments_
            }
        status_ = status.HTTP_200_OK
        return Response(response, status_)


class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = CommentSerializer


# class BlogView(RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = BlogPostSerializer

#     def get(self, request, **args):
#         if not args:
#             blog_objects = BlogPost.objects.all()
#             blogs_ = []
#             for blog in blog_objects:
#                 data = {
#                     'id': blog.id,
#                     'title': blog.title,
#                     'tag': blog.tag,
#                     'image': blog.image.url,
#                     'body': blog.body,
#                     'created': blog.created
#                 }
#                 blogs_.append(data)

#             response = {
#                 'success': True,
#                 'status_code': status.HTTP_200_OK,
#                 'message': 'blogs fetched!',
#                 'data': blogs_
#             }

#             status_ = status.HTTP_200_OK

#         else:
#             blog_id = args['blog_id']
#             blog = BlogPost.objects.get(id=blog_id)
#             blogs_ = {
#                 'title': blog.title,
#                 'tag': blog.tag,
#                 'image': blog.image.url,
#                 'body': blog.body,
#                 'created': blog.created
#             }

#             response = {
#                 'success': True,
#                 'status_code': status.HTTP_200_OK,
#                 'message': 'blogs fetched!',
#                 'data': blogs_
#             }

#             status_ = status.HTTP_200_OK

#         return Response(response, status_)


class BlogListCreateView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = BlogPostSerializer

    def get(self, request, **args):
        blog_objects = BlogPost.objects.all()
        blogs_ = []
        for blog in blog_objects:
            data = {
                'id': blog.id,
                'title': blog.title,
                'tag': blog.tag,
                'image': blog.image.url,
                'body': blog.body,
                'created': blog.created
            }
            blogs_.append(data)

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'blogs fetched!',
            'data': blogs_
        }
        status_ = status.HTTP_200_OK
        return Response(response, status_)


class BlogRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = BlogPostSerializer

    def get(self, request, **args):
        blog_id = args['blog_id']
        blog = BlogPost.objects.get(id=blog_id)
        blogs_ = {
            'id': blog.id,
            'title': blog.title,
            'tag': blog.tag,
            'image': blog.image.url,
            'body': blog.body,
            'created': blog.created
        }

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'blogs fetched!',
            'data': blogs_
        }
        status_ = status.HTTP_200_OK
        return Response(response, status_)

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .models import User
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'message': 'User registered successfully!'
        }
        
        status_ = status.HTTP_200_OK
        return Response(response, status_)



class UserLoginView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : True,
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully!',
            'token' : serializer.data['token'],
            'username': serializer.data['email']
            }

        status_ = status.HTTP_200_OK

        return Response(response, status=status_)


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

class UserAccountRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    # def get_queryset(self):
    #     print(f"User: {self.request.user}")
    #     user = User.objects.get(id=self.request.user.id)
    #     return user

    def get_object(self):
        """retrieve and return the authenticated user"""
        return self.request.user

    # def get(self, request):
    #     print(request.user)
    #     serialized_user = UserSerializer(request.user)
    #     return request.user


class PasswordResetView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

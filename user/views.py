from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer, ChangePasswordSerializer, ForgotPasswordSerializer
# from rest_framework.permissions import IsAuthenticated   
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


class ForgotPasswordView(CreateAPIView):
    # queryset = User.objects.all()
    # model = User
    serializer_class = ForgotPasswordSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        #TODO: Add functionality to send mail

        response = {
            'success' : True,
            'status code' : status.HTTP_200_OK,
            'message': 'Check your mail for the password reset link!',
            # 'token' : serializer.data['token'],
            'email': serializer.data['email']
            }

        status_ = status.HTTP_200_OK

        return Response(response, status=status_)


class ChangePasswordView(UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        email = self.request.Get.get('email')
        id = id = self.request.Get.get('id')

        obj = User.objects.get(email=email, id=id)
        # obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # # Check old password
            # if not self.object.check_password(serializer.data.get("old_password")):
            #     return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # # set_password also hashes the password that the user will get
            # self.object.set_password(serializer.data.get("new_password"))
            # self.object.save()
            # Check old password
            self.object.set_password(serializer.data.get("password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
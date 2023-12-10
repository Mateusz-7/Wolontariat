from django.http import HttpRequest, HttpResponse
from .models import User
from .serializer import UserSerializer
from rest_framework import generics


# GET all users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# GET user by id
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

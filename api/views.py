from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from .serializers import DiaryNotesSerializer, UserSerializer 
from .models import DiaryNotes
# Create your views here.

class UserListView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes= [AllowAny]
  
 
 
class NoteListView(generics.ListCreateAPIView):
  serializer_class= DiaryNotesSerializer
  permission_classes= [IsAuthenticated]
  
  
  def get_queryset(self):
    user =  self.request.user
    return DiaryNotes.objects.filter(author= user)
  
  
  def perform_create(self, serializer):
    serializer.save(author= self.request.user)

class NoteUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class= DiaryNotesSerializer
  permission_classes= [IsAuthenticated]
  
  def get_queryset(self):
    user = self.request.user
    return DiaryNotes.objects.filter(author=user)
  
class MeView(APIView):
  permission_classes= [IsAuthenticated]
  
  def get(self, request):
    user = request.user
    return Response({
      "first_name": user.first_name,
      "last_name": user.last_name,
      "email": user.email,
    })
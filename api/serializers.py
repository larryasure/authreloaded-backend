from django.contrib.auth.models import  User
from rest_framework import serializers
from .models import DiaryNotes

class UserSerializer(serializers.ModelSerializer):
  password= serializers.CharField(write_only= True)
    
  class Meta:
    model = User
    fields = ["id", "email", "username", "first_name", "last_name", "password" ]
    
    
  def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      return user
    
    
class DiaryNotesSerializer(serializers.ModelSerializer):
  author = serializers.CharField(source="author.username", read_only=True)
  
  
  class Meta:
    model = DiaryNotes
    fields = ["id", "author", "title", "content", "created_at", "updated_at"]
    extra_kwargs= {"author": {"read_only": True}}
    
    


 
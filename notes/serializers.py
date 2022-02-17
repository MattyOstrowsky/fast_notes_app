from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Note
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'name', 'password')
        
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
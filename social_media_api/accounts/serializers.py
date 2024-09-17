from rest_framework import serializers
from .models import Customuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id', 'email', 'password', 'bio', 'profile_picture', 'username',]
        extra_kwargs =  {'password': {'write_only': True}}


    
    def create(self, validated_data):
        return Customuser.objects.create_user(**validated_data)
    
    
    
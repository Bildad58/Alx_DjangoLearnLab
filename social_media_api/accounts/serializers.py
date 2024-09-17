from rest_framework import serializers
from .models import Customuser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)    

    class Meta:
        model = Customuser
        fields = ['id', 'email', 'username','profile_picture', 'bio',  'password','password2']
        extra_kwargs =  {'password': {'write_only': True}}


    def validate(self,attr):
        if attr['password'] != attr['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attr


    def create(self, validated_data):
        validated_data.pop('password2')
        user = Customuser.objects.create_user(
            username = validated_data['username'],
            password= validated_data['password'],
            bio = validated_data['bio'],
            profile_picture = validated_data.get('profile_picture',None)

        )
        Token.objects.create(user=user)
        return user

    
    
    
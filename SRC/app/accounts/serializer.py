from rest_framework import serializers
from .models import CustomUser, Customer


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'

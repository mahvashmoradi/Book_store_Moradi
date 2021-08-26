from rest_framework import serializers
from .models import CustomUser, Customer, AddressModel, CityModel, ProvinceModel

from drf_writable_nested import WritableNestedModelSerializer


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceModel
        fields = ('name',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = ('name',)


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


class AddressSerializer(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField()
    # customer = CustomerSerializer(required= False, read_only=True)
    province = ProvinceSerializer
    city = CitySerializer

    class Meta:
        model = AddressModel
        fields = ('province', 'city', 'address', 'postal_code', 'phone_number')
        # fields = ( 'customer', )


class CustomerSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    inf_address = AddressSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['user', 'first_name', 'last_name', 'gender', 'inf_address']

    # def create(self, validated_data):
    #     inf_addresses = validated_data.pop('inf_address')
    #     customer = Customer.objects.create(**validated_data)
    #     for address in inf_addresses:
    #         AddressModel.objects.create(customer = customer, **address)
    #     return customer

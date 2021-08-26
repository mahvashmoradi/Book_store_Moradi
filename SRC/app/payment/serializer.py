from rest_framework import serializers
from .models import Coupons, Discount, Invoice, InvoiceLine
from app.book.serializer import BookSerializer


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class InvoiceLineSerializer(serializers.ModelSerializer):
    # invoice = serializers.PrimaryKeyRelatedField(read_only=True)
    # book = serializers.PrimaryKeyRelatedField(read_only=True)
    # url = serializers.CharField(source='get_absolute_url', read_only=True)
    # items = serializers.StringRelatedField()

    # invoice =
    class Meta:
        model = InvoiceLine
        # fields = '__all__'
        fields = ['items', 'unit_price', 'quantity']
    # def create(self, validated_data):
    #     InvoiceLine.objects.create(validated_data)


class InvoiceSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    # discount_value = serializers.PrimaryKeyRelatedField(read_only=True)
    Items = InvoiceLineSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ['customer', 'invoice_complete_date', 'Items', 'total', 'total_with_discount', ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # def create(self, validated_data):
    #
    #     # serializer = InvoiceLineSerializer(validated_data)
    #     InvoiceLine.objects.create()
    #     user = User(
    #         email=validated_data['email'],
    #         username=validated_data['username']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     Token.objects.create(user=user)
    #     return user

from rest_framework import serializers
from .models import BookModel, CategoryModel, Author


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('name')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name')


class BookSerializer(serializers.ModelSerializer):
    # invoice = serializers.PrimaryKeyRelatedField(read_only=True)
    # book = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = BookModel
        # fields = '__all__'
        fields = ['name', 'author', 'price', 'price_discount', 'created', 'image', 'categories']
        extra_kwargs = {'price_discount': {'read_only': True}}

    def create(self, validated_data):
        price = self.price
        # print('chek',self.dis_value.all())
        if self.dis_value.all():
            print('hi')
            if self.dis_value.values('choice_discount')[0]['choice_discount'] == 'V':
                print('chek if')
                amount = self.dis_value.values('value')[0]
                price = price - amount['value']
            else:
                percent = self.dis_value.values('percent')[0]
                print('p', percent)
                price = (100 - percent['percent']) * price / 100
        if price != self.price:
            self.price_discount = price
        book_save= BookModel.objects.create(**validated_data)
        return book_save


from django.urls import reverse
from django.db import models
# from django.urls import revers
# CategoryModel
from django.shortcuts import redirect

from app import payment
from app.book.manager import CategoriesManager


class CategoryModel(models.Model):
    # name of Category
    name = models.CharField('نام', max_length=50)
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name


# Author
class Author(models.Model):
    name = models.CharField('نام', max_length=150, blank=False)

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def __str__(self):
        return self.name


# book
class BookModel(models.Model):
    name = models.CharField('نام', max_length=100)
    author = models.ManyToManyField(Author, verbose_name='نویسنده')
    price = models.PositiveBigIntegerField('قیمت', )
    discount_price = models.PositiveBigIntegerField('قیمت با تخفیف', default=0)
    # discount = models.IntegerField('تخفیف', default=0)
    created = models.DateField('تاریخ ثبت کتاب', auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel, blank=False, related_name='category', verbose_name='گروه')
    inventory = models.IntegerField('موجودی')
    image = models.ImageField(upload_to='book/', null=True, blank=True)

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    # def get_absolute_url(self):
    #     return reverse("home", args=[str(self.id)])
    #     # return reverse("home", kwargs={'slug': self.slug })

    # calculate discount price(both value and percentage)
    def cal_discount_price(self, instance):
        price = self.price
        if instance.choice_discount == 'V':
            amount = instance.value
            print('v')
            price = price - amount

        else:
            percent = instance.percent
            print('p', percent)
            price = (100 - percent) * price / 100
        self.discount_price = price
        self.save()
        return price

    # get category of book
    def get_category_display(self):
        return self.categories.values('name')

    def add_cart(self):
        return reverse('payment:add_to_cart',
                       # pk= str(self.id) )
        kwargs={'pk': self.id})

    def __str__(self):
        return self.name

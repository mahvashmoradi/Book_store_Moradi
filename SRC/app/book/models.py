from django.db import models
# from django.urls import revers
# CategoryModel
from app import payment


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
    price = models.PositiveBigIntegerField('قیمت',)
    discount_price = models.PositiveBigIntegerField('قیمت با تخفیف', default=0)
    # discount = models.IntegerField('تخفیف', default=0)
    created = models.DateField('تاریخ ثبت کتاب', auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel, blank=False,related_name='category', verbose_name='گروه')
    inventory = models.IntegerField('موجودی')
    image = models.ImageField(upload_to='book/', null=True, default='0.png')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'
    # def get_absolute_url(self):
    #     return reverse("home", args=[str(self.id)])
    #     # return reverse("home", kwargs={'slug': self.slug })

    # calculate discount price(both value and percentage)
    def cal_discount_price(self):
        price = self.price
        # print('chek',self.dis_value.all())
        if self.dis_value.all():
            if self.dis_value.values('choice_discount')[0]['choice_discount'] == 'V':
                amount = self.dis_value.values('value')[0]
                price = price - amount['value']
            else:
                percent = self.dis_value.values('percent')[0]
                print('p',percent)
                price = (100 - percent['percent']) * price / 100
        if price != self.price:
            self.price_discount = price
        else:
            self.price_discount = self.price
        self.save()
        return self.price_discount

    # get category of book
    def get_category_display(self):
        return self.categories.values('name')

    def __str__(self):
        return self.name

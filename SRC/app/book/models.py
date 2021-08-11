from django.db import models
# from django.urls import reverse


# CategoryModel
class CategoryModel(models.Model):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    # name of Category
    name = models.CharField('نام', max_length=50)

    def __str__(self):
        return self.name


# Author
class Author(models.Model):
    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    name = models.CharField('نام', max_length=150, blank=False)

    def __str__(self):
        return self.name


# book
class BookModel(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    name = models.CharField('نام', max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name='نویسنده')
    price = models.DecimalField('قیمت', max_digits=18, decimal_places=2)
    price_discount = models.DecimalField('قیمت با تخفیف', max_digits=18, decimal_places=2, blank=True, null=True)
    created = models.DateField('تاریخ ثبت کتاب', auto_now_add=True)
    categories = models.ManyToManyField(CategoryModel, blank=False, verbose_name='گروه')
    image = models.ImageField(upload_to='book/', null=True, default='0.png')

    # def get_absolute_url(self):
    #     return reverse("home", args=[str(self.id)])
    #     # return reverse("home", kwargs={'slug': self.slug })

    # calculate discount price(both value and percentage)
    def discount_price(self):
        price = self.price
        if self.dis_percent.all():
            price = (100 - self.dis_percent.values('percent')[0]['percent']) * price / 100

        if self.dis_value.all():
            amount = self.dis_value.values('value')[0]
            price = price - amount['value']
        if price != self.price:
            self.price_discount = price
            return self.price_discount

    # get category of book
    def get_category_display(self):
        return self.categories.values()

    def __str__(self):
        return self.name


# Store Model
class Store(models.Model):
    class Meta:
        verbose_name = 'فروشگاه'
        verbose_name_plural = 'فروشگاه ها'

    product = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='product', verbose_name='محصولات')
    Inventory = models.IntegerField('موجودی')

    def __str__(self):
        return str(self.product)

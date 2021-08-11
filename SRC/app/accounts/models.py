from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# CustomUser
class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    REQUIRED_FIELDS = [('email'), ]
    USERNAME_FIELDS = ('email',)
    username = models.CharField('نام کاربری', max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField('ایمیل', blank=False, unique=True)
    password = models.CharField('رمز عبور', max_length=50)
    register_date = models.DateTimeField(verbose_name='تاریخ ساخت حساب', auto_now_add=True, blank=True)
    # Address_Customer = models.ManyToManyField('AddressModel', blank=False, related_name='address_text')
    # Address_Customer = models.ForeignKey('AddressModel',on_delete=models.DO_NOTHING, blank=False,
    # related_name='address_text')

    def __str__(self):
        return self.email


# Customer
class Customer(models.Model):
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
    Female = 'F'
    Male = 'M'
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    GENDER_CHOICES = [(Female, 'زن'), (Male, 'مرد')]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField('جنسیت', choices=GENDER_CHOICES, max_length=1, blank=True, null=True)

    def __str__(self):
        return str(self.user)


# Address model
class AddressModel(models.Model):
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس کاربران'

    customer = models.ForeignKey(Customer, blank=False, on_delete=models.CASCADE, verbose_name='کاربر')
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField('آدرس', max_length=300)
    Postal_code = models.IntegerField()

    def __str__(self):
        return str(self.customer)

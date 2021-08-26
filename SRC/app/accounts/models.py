from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# CustomUser
class CustomUser(AbstractUser):
    REQUIRED_FIELDS = [('email'), ]
    USERNAME_FIELDS = ('email',)
    username = models.CharField('نام کاربری', max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField('ایمیل', blank=False, unique=True)
    password = models.CharField('رمز عبور', max_length=100)
    register_date = models.DateTimeField(verbose_name='تاریخ ساخت حساب', auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return str(self.email)


# Customer
class Customer(models.Model):
    Female = 'F'
    Male = 'M'
    first_name = models.CharField('نام', max_length=100, blank=True, null=True)
    last_name = models.CharField('نام خانوادگی', max_length=100, blank=True, null=True)
    GENDER_CHOICES = [(Female, 'زن'), (Male, 'مرد')]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField('جنسیت', choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    device = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        if self.user:
            name = self.user
        else:
            name = self.device
        return str(name)


# Address model
class AddressModel(models.Model):
    customer = models.ForeignKey(Customer, blank=False, related_name='inf_address', on_delete=models.CASCADE,
                                 verbose_name='کاربر')
    city = models.ForeignKey('CityModel', verbose_name='شهر', on_delete=models.PROTECT, related_name='city')
    province = models.ForeignKey('ProvinceModel', on_delete=models.PROTECT, related_name='province',
                                 verbose_name='استان')
    address = models.TextField('آدرس')
    postal_code = models.CharField('کد پستی', max_length=10)
    phone_number = models.CharField('شماره تلفن', max_length=11)

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس کاربران'

    def __str__(self):
        return str(self.customer)


# City model
class CityModel(models.Model):
    name = models.CharField('نام', max_length=100)

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'

    def __str__(self):
        return str(self.name)


# Province model
class ProvinceModel(models.Model):
    name = models.CharField('نام', max_length=100)

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'

    def __str__(self):
        return str(self.name)

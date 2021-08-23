from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from app.payment.models import Discount
from .models import BookModel


# """اگر از جدول تخفیف ها کتابی حذف شد، قیمت تخفیفی آن صفر می شود"""
@receiver(post_delete, sender=Discount)
def my_handler(sender, instance, **kwargs):
    instance.book.discount_price = 0
    instance.book.save()


# """اگربه جدول تخفیف ها کتابی اضافه شد، قیمت تخفیفی آن محاسبه می شود"""
@receiver(post_save, sender=Discount)
def my_handler(sender, instance, **kwargs):
    a = instance.book.cal_discount_price(instance=instance)
    instance.book.discount_price = a
    instance.book.save()


# """اگر تغییری در قیمت کتاب ها اتفاق افتاد، قیمت تخفیف آن مجددا محاسبه می شود"""
@receiver(post_save, sender=BookModel)
def my_handler(sender, instance, **kwargs):
    discount = Discount.objects.get(book__name=instance.name)
    a = instance.cal_discount_price(instance=discount)
    instance.discount_price = a
    instance.save()

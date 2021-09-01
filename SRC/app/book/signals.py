from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from app.payment.models import Discount


# """اگر از جدول تخفیف ها کتابی حذف شد، قیمت تخفیفی آن صفر می شود"""
@receiver(pre_delete, sender=Discount)
def delete_discount(sender, instance, **kwargs):
    instance.book.discount_price = 0
    instance.book.save()
    instance.save()


# """اگربه جدول تخفیف ها کتابی اضافه شد، قیمت تخفیفی آن محاسبه می شود"""
@receiver(post_save, sender=Discount)
def add_discount(sender, instance, created, **kwargs):
    if created:
        instance.book.cal_discount_price(instance=instance)
        instance.save()


# # """اگر تغییری در قیمت کتاب ها اتفاق افتاد، قیمت تخفیف آن مجددا محاسبه می شود"""
# @receiver(post_save, sender=BookModel)
# def update_discount(sender, instance,created, **kwargs):
#     if not created:
#         discount = Discount.objects.filter(book__name=instance.name)
#         if discount:
#             a = instance.cal_discount_price(instance=discount[0])
#             instance.discount_price = a
#             instance.save()


# post_save.connect(add_discount, dispatch_uid="add_discount_identifier")
# pre_delete.connect(delete_discount, dispatch_uid="delete_discount_identifier")
# post_save.connect(update_discount, dispatch_uid="update_discount_identifier")

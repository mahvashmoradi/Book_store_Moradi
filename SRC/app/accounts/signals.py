from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, Customer
from django.contrib.auth.models import Group


@receiver(post_save, sender=CustomUser)
def my_handler(sender, instance, created, **kwargs):
    """
    وقتی کاربری ساخته شد،
     مشتری با همین مشخصات ساخته می شود و به گروه customer_group اضافه می شود و دسترسی های این گروه را دارد
    """
    if not instance.is_staff and created:
        try:
            customer = Customer.objects.create(user=instance)
            group = Group.objects.get(name='customer_group')
            # group.user_set.add(customer)
            # group.save()
            instance.groups.add(group)
            instance.save()
        except:
            print('again')

# post_save.connect(create_customer, sender=CustomUser)

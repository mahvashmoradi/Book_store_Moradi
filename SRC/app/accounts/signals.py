from django.db.models.signals import post_save
from django.dispatch import receiver

from app.accounts.models import CustomUser, Customer


# python manage.py sqlsequencereset auth

@receiver(post_save, sender=CustomUser)
def my_handler(sender, instance, **kwargs):
    if not instance.is_staff:
        try:
            Customer.objects.create(user=instance)
        except:
            print('again')

# post_save.connect(create_customer, sender=CustomUser)

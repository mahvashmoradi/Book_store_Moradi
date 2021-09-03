from django.apps import AppConfig
# from django.db.models.signals import post_save
#
# from app.accounts.models import CustomUser
# from app.accounts.signals import create_customer


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.accounts'

    def ready(self):
        import app.accounts.signals

# post_save.connect(create_customer, sender=CustomUser)
# post_save.connect(save_user_profile, sender=User)
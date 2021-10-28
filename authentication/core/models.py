from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# Create your models here.
@receiver(user_signed_up)
def after_user_signed_up(request, user, **kwargs):
    if user.email.endswith('mtmail.mtsu.edu'):
        # do something for valid accounts
        pass
    elif user.email.endswith('mtsu.edu'):
        # do something for valid accounts
        pass
    else:
        user.is_active = False
        user.save()
        # raise SomeException
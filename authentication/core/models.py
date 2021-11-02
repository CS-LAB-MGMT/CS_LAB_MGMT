from django.db import models
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.conf import settings


# user.email -> returns the user's email as a string
# user.password -> returns the user's password

@receiver(user_signed_up)
def after_user_signed_up(request, user, **kwargs):
	# Domain checker using allauth signals
	if user.email.endswith('mtmail.mtsu.edu'):
		pass

	elif user.email.endswith('mtsu.edu'):
		pass

	else:
		user.is_active = False
		user.save()

	

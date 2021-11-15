from django.contrib import admin

# Register your models here.

#Database models
from .models import Systems
from .models import Students
from .models import Scripts
from .models import AccountRequests

#register models so they show up on Admin page and can be manipulated
admin.site.register(Systems)
admin.site.register(Students)
admin.site.register(Scripts)
admin.site.register(AccountRequests)


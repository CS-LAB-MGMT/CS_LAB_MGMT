from django.contrib import admin

# Register your models here.

#Database models
from .models import Systems
from .models import Students
from .models import Scripts
from .models import AccountRequests
from .models import RequestType

#register models so they show up on Admin page and can be manipulated
# admin.site.register(Systems)
admin.site.register(Students)
# admin.site.register(Scripts)
# admin.site.register(AccountRequests)

# Register and custom fields show in table of AdminPortal
# @admin.register(AccountRequests)
#Below creates an action to "Generate Script" with the selection.
# queryset is what contains the selection.
# for acc_req in queryset: returns a row that's easy to work with.
@admin.action(description='Generate Script')
def generate_script(modeladmin,request,queryset):
  scripts = Scripts.objects.all()

  for acc_req in queryset:
    # script = scripts.
    print(acc_req.reason)

class RequestTypeListFilter(admin.SimpleListFilter):
  title = "request type"
  parameter_name = "request_type"
  default_value = None

  def lookups(self,request,model_admin):
    list_of_request_types = []
    queryset = RequestType.objects.all()
    for req in queryset:
      list_of_request_types.append(
        (str(req.request_type),str(req.request_type))
      )
    return sorted(list_of_request_types,key=lambda tp: tp[1])

  def queryset(self,request,queryset):
    if self.value():
      return queryset.filter(request_type=self.value())
    return queryset


@admin.register(AccountRequests)
class AccountRequestsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in AccountRequests._meta.get_fields()]
  actions = [generate_script]
  list_filter = (RequestTypeListFilter,)

@admin.register(RequestType)
class RequestTypeAdmin(admin.ModelAdmin):
  pass

class SystemsAdmin(admin.ModelAdmin):
  list_display = ['system_name','group_name']

class ScriptsAdmin(admin.ModelAdmin):
  list_display = [f.name for f in Scripts._meta.get_fields()]

# admin.site.register(AccountRequests,AccountRequestsAdmin)
admin.site.register(Systems,SystemsAdmin)
admin.site.register(Scripts,ScriptsAdmin)
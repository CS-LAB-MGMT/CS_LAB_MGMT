from django.contrib import admin
from django.forms.models import model_to_dict
# Register your models here.
from datetime import datetime
#Database models
from .models import Systems
from .models import Students
from .models import Scripts
from .models import AccountRequests
from .models import RequestType

from django.shortcuts import render
from django.contrib import messages
from django.utils.safestring import mark_safe

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


def gen_search(items,key,value,key2=None,value2=None):

  if key2 is None:
    for item in items:
      if item[key]==value:
        return item
  else:
    for item in items:

      if item[key]==value and item[key2]==value2:
        return item
  return None




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

  def generate_script(self,request,queryset):
    systems = Systems.objects.all()
    systems = systems.values()
    scripts = Scripts.objects.values()
    scripts = list(scripts)
    
    new_script = ""
    num_no_script = 0

    for acc_req in queryset:

      sys = str(acc_req.system_name)
      rt = str(acc_req.request_type)

      script= gen_search(scripts,'system_name_id',sys,'script_type_id',rt)

      group_name = gen_search(systems,'system_name',sys)
    
      group = group_name['group_name']
      if script:
        script = script['script_string']

        new_script_next = script.format(user=acc_req.pipeline_id,group=group) + '\n'
        new_script = new_script + new_script_next

        queryset.update(request_complete=1)
        queryset.update(request_status=4)
      else:
        num_no_script += 1

    if num_no_script > 0:
      messages.warning(request,f'{num_no_script} requests could not be processed due to a lack of script templates.')

    return render(request,
                  'script.html',
                  context={'new_script':new_script})


  generate_script.short_description = 'Generate Script'

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
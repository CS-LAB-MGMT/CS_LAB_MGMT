from django.contrib import admin
from django.forms.models import model_to_dict
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


def gen_search(items,key,value,key2=None,value2=None):

  if key2 is not None:
    for item in items:
      if item[key]==value:
        return item
  else:
    for item in items:
      print(item)
      if item[key]==value and item[key2]==value2:
        return item
  return None

@admin.action(description='Generate Script')

def generate_script(modeladmin,request,queryset):
  systems = Systems.objects.all()
  systems = systems.values()
  scripts=Scripts.objects.values()
  scripts=list(scripts)
  print(scripts)
  #return
  #print (systems.objects.get(system_name='system64'))
  script='This is the scripts you need to copy \n \n'
  password_input="put the password here"
  # make sure this file save in scrirpts or media
  f=open("script.txt","w+")
  #first=True
  for acc_req in queryset:

    sys=str(acc_req.system_name)
    #rt=request type
    rt=str(acc_req.request_type)
    script=gen_search(scripts,'system_name_id',sys,'request_type',rt)

    group_name=gen_search(systems,'system_name',sys)
    #print(group_name['group_name'])
    group_name=group_name['group_name']
    script=script['script_string']
    script_new=script.format(user=acc_req.pipeline_id,group=group_name)+'\n'
    #script_new=('add-LocalGroupMember -Group "{}"'.format(group_name))+\
    #(' -Member "{}"'.format(acc_req.pipeline_id))+"\n"
    script=script+script_new

  f.write(script_string)
  queryset.update(request_complete=1)
  queryset.update(request_status=4)

  print (script_string)
  f.close()



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
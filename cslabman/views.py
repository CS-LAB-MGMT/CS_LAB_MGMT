# import statements
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from cslabman.models import Systems, RequestType, Scripts, AccountRequests, Students
# Shows User view of request page. Takes HTML template from Templates directory home.html
def home (request):
    return render(request, 'cslabman/home.html')

#Shows user view of about page, takes HTML template from Templates directory help.html
def help(request):
    return render(request, 'cslabman/help.html')

# This allows an admin to initialize the database. Its not pretty and should be moved to the Admin Portal
def initdb(request):
    # Init db here
    # Check content of Systems, assume if systems is empty, db is uninitialized.
    systems = Systems.objects.all()
    if systems.exists():
        messages.warning(request,f'Database must be empty to be initialized.')
    else:
        req_acc = RequestType.objects.create(request_type="Request Access")
        upd_acc = RequestType.objects.create(request_type="Change Access")
        rnw_acc = RequestType.objects.create(request_type="Renew Access")

        st1 = Students.objects.create(pipeline_id="st1")
        st2 = Students.objects.create(pipeline_id="st2")
        st3 = Students.objects.create(pipeline_id="st3")

        gta = Systems.objects.create(system_name="GTA",group_name="csgtas")
        cluster = Systems.objects.create(system_name="Cluster",group_name="clusterusers")

        script = Scripts.objects.create(system_name=gta,script_type=req_acc,script_string='Add-LocalGroupMember -Group "{group}" -Member "{user}"')
        script = Scripts.objects.create(system_name=cluster,script_type=req_acc,script_string='Add-LocalGroupMember -Group "{group}" -Member "{user}"')
        
        ar1 = AccountRequests(pipeline_id=st1,system_name=gta,reason="Because",request_type=req_acc,request_status=1,request_complete=0)
        ar1.save()
        ar2 = AccountRequests(pipeline_id=st1,system_name=cluster,request_type=req_acc)
        ar2.save()
        ar3 = AccountRequests(pipeline_id=st2,system_name=gta,request_type=req_acc)
        ar3.save()
        ar4 = AccountRequests(pipeline_id=st2,system_name=cluster,request_type=req_acc)
        ar4.save()
        ar5 = AccountRequests(pipeline_id=st3,system_name=gta,request_type=req_acc)
        ar5.save()
        ar6 = AccountRequests(pipeline_id=st3,system_name=cluster,request_type=req_acc)
        ar6.save()
        # add two for update user
        # add two for renew access
        
        messages.success(request,f'Database has been initialized.')
        
    return render(request,'cslabman/home.html')



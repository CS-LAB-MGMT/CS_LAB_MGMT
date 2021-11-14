import datetime
import this

from django.shortcuts import render, redirect
from .forms import registerForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import requestForm
from .forms import systemForm
from csldap.ldap import isAlreadyStillMember
from cslabman.models import Systems, Students
# Create your views here.

#View when users try to register for website

def register(request):

    if request.method == 'POST':

        form = registerForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')

    else:
        form = registerForm().as_p()

    return render(request, 'users/login.html', {'form': form})

#After login, take to access request questionnaire form, must be logged in to view
@login_required
def mtcsRequests(request):
    #return render(request, 'users/mtcsRequests.html')
    if request.method == 'POST':

        form = requestForm(request.POST,
                            )
        #form = systemForm(request.POST)
        username = request.user.username
        user = Students()
        user.pipeline_id = username

        system_name = form['system_name'].value()
        query_group = Systems.objects.get(system_name=system_name)
        group_name = query_group.group_name
        renew_access = form['request_type'].value() == "Renew Access"
        print(username)
        print(system_name)
        print(group_name)
        print(form['request_type'].value())
        # CHRIS: Reorder things in this function in the most logical and sensible way.
        # CHRIS: Verifies the username is in the group, and also not expired.
        csldap_res = isAlreadyStillMember(username,group_name)
        print(csldap_res)
        if form.is_valid():
# REMOVE 'not' if 'not' csldap_res
            if  csldap_res['isExpired'] and not renew_access:
                messages.warning(request,f'{username} account may be expired. Please use Renew Access.')

            elif csldap_res['isMember'] and not renew_access:
                messages.error(request,f'User {username} is already a member of {system_name}.')

            elif not csldap_res['isValid']:
                pass

            else:
                if request.user.is_authenticated:
                    obj = form.save(commit=False)
                    user.save()
                    obj.pipeline_id = user
                    form.save()
                    messages.success(request,f'Request sent.')
                
                return redirect('/MTCS-Requests')
    else:
        form = requestForm().as_p()
        #form = systemForm().as_p()
    return render(request, 'users/mtcsRequests.html',  {'form': form})






from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import requestForm
from cslabman.models import AccountRequests



#After login, take to access request questionnaire form, must be logged in to view
@login_required
def mtcsRequests(request):

    if request.method == 'POST':

        form = requestForm(request.POST, initial={'pipeline_id': request.user})


        if form.is_valid():
            form.save()
            messages.success(request, f'Request Saved')
            return redirect('Request-Home')
    else:

        form = requestForm().as_p()
    return render(request, 'users/mtcsRequests.html',  {'form': form})


# After login, view current requests of this user
@login_required
def viewRequests(request):

    #get current requests, filter by current user
    stuRequests = AccountRequests.objects.filter(pipeline_id=request.user.username)

    students = {
        "students": stuRequests
    }

    return render(request, 'users/viewRequests.html',  students, )

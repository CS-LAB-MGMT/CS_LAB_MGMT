import datetime
import this

from django.shortcuts import render, redirect
from .forms import registerForm

from django.contrib.auth.decorators import login_required
from .forms import requestForm
from .forms import systemForm

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

        form = requestForm(request.POST)
        #form = systemForm(request.POST)
        if form.is_valid():

            form.save()

            return redirect('Request-home')
    else:
        form = requestForm().as_p()
        #form = systemForm().as_p()
    return render(request, 'users/mtcsRequests.html',  {'form': form})




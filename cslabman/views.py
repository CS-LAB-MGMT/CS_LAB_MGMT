# import statements

from django.shortcuts import render
from django.http import HttpResponse

# Shows User view of request page. Takes HTML template from Templates directory home.html
def home (request):
    return render(request, 'cslabman/home.html')

#Shows user view of about page, takes HTML template from Templates directory help.html
def help(request):
    return render(request, 'cslabman/help.html')





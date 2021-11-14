import datetime

from django.forms import ModelForm
from django import forms
from cslabman.models import AccountRequests
from cslabman.models import Systems
from cslabman.models import RequestType
from django.db import models


class registerForm(forms.Form):
    Pipeline_ID = forms.CharField(label="Pipeline_ID", min_length=6, required=True)
    Pipeline_Password = forms.CharField(label="Pipeline_Password", widget=forms.PasswordInput, required=True)

class requestForm(ModelForm):

    #django specs require html select values to be specified in this format
    REQUESTCHOICES = [('1', 'Request a new account'),
                      ('3', 'Request special permissions'),
                      ('4', 'Reset Password')]

    SYSTEMCHOICES = [
                     ('Ranger', 'Ranger'),
                     ('System64', 'System64'),
                     ('Cluster', 'Cluster'),
                     ('PersonalAccount', 'Personal CS Account')]

    #specify the order in which rom fields show up on webpage
    field_order = ['system_name', 'request_type', 'reason']

    #declare form fields with some styling and labels
    systems = Systems.objects.all()

    system_name = forms.ModelChoiceField(queryset=systems, widget=forms.Select,
                                    label='What system is this request for?', required=True, )
    
    requesttypes = RequestType.objects.all().order_by('request_type')
    
    request_type = forms.ModelChoiceField(queryset=requesttypes, widget=forms.RadioSelect, label='What is this request for?',
                                   required=True)

    reason = forms.CharField(required=False, label='Reason for Request:',
                             widget=forms.Textarea(attrs={'style': 'width:100%;'}))



    #Declare what model form is based on
    class Meta:
        model = AccountRequests
        fields = ['request_type', 'system_name',  'reason']
        

class systemForm(ModelForm):
    SYSTEMCHOICES = [
        ('Ranger', 'Ranger'),
        ('Sysetm64', 'System64'),
        ('Cluster', 'Cluster'),
        ('Personal CS Account', 'Personal CS Account')]
    system_name = forms.ChoiceField(choices=SYSTEMCHOICES, label='What system is this request for?', required=True,)
    class Meta:
        model = Systems
        fields = ['system_name']



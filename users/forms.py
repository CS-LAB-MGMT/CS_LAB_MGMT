
from django.forms import ModelForm
from django import forms
from cslabman.models import AccountRequests
from cslabman.models import Students
from cslabman.models import Systems



#Form that shows when user wants to request things from department
class requestForm(ModelForm):

    #django specs require html select values to be specified in this format (value, human readable name)
    REQUESTCHOICES = [(1, 'Request a new account'),
                      (3, 'Request special permissions'),
                      (4, 'Reset Password')]


    #specify the order in which form fields show up on webpage
    field_order = ['system_name', 'request_type', 'reason']


    #declare form fields with some styling and labels

    #What is this request for
    request_type = forms.TypedChoiceField(choices=REQUESTCHOICES, widget=forms.RadioSelect, label='What is this request for?',
                                   required=True, coerce=int)

    #what system is this request for
    system_name = forms.ModelChoiceField(queryset=Systems.objects.all().order_by('system_name'), widget=forms.Select,
                                         label='What system is this request for?', required=True,
                                         to_field_name='system_name')
    #Reason for asking
    reason = forms.CharField(required=False, label='Reason for Request:',
                             widget=forms.Textarea(attrs={'style': 'width:100%;'}))

    #pipeline id for request will be set to curernt logged in user, no need to show this on the form
    #Only here so that on form submission ID can be saved
    pipeline_id = forms.ModelChoiceField(required=False, queryset=Students.objects.all().order_by('pipeline_id'),
                              disabled=True, widget=forms.HiddenInput())

    #Declare what model form is based on
    class Meta:
        model = AccountRequests
        fields = ['request_type', 'system_name',  'reason', 'pipeline_id']


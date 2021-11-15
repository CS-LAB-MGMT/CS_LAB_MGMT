from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm
from django import forms
from core import settings
from cslabman.models import Students

#This overrides the django allauth default signup form to add a pipeline ID field, and to
#save users to website once they have signed up.
class CustomSignupForm(SignupForm):



    #Change the labels on django allauth signup fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # here you can change the fields
        self.fields['email'] = forms.EmailField(label='MTSU Email')
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput(), label='Pipeline Password')
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
        self.fields['username'] = forms.CharField(max_length=6, label='Pipeline ID')

        # hide the remember me button from default allauth form, removing it completely affects default allauth
        #functions. If you want to permanently remove it, you would need to also define other allauth functions for
        #the form
        self.fields['remember'] = forms.CharField(disabled=True, widget=forms.HiddenInput(), required=False)




class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # here you can change the fields
        self.fields['login'] = forms.EmailField(label='MTSU Email')
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput(), label='Pipeline Password')

        # hide the remember me button from default allauth form, removing it completely affects default allauth
        # functions. If you want to permanently remove it, you would need to also define other allauth functions for
        # the form
        self.fields['remember'] = forms.CharField(disabled=True, widget=forms.HiddenInput(), required=False)



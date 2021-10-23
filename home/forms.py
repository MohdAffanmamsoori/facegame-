# Bismillah Hir Rehman Nir Rahim

from django.contrib.auth import models
from django.forms import ModelForm
# from . models import Contactus
# from .models import UserProfile   

# class UserDetailsForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['company','address1','address2','city','region', 'postcode','country','phone']
from django.forms import ModelForm

from . models import Contactus

class ContactForm(ModelForm):
 class Meta:
    model=Contactus
    fields=['Name','Email','Problem']
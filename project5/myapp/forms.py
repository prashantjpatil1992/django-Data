from django import forms
from .models import Django_Khalid,Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class django_form(forms.ModelForm):
    gen = (('Male','Male'),('Female','Female'),('Other','Other'))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
    
    ct = (('Mumbai',"Mumbai"),("Thane","Thane"),("Ghatkopar","Ghatkopar"),("Nashik","Nshik"))
    city = forms.ChoiceField(choices=ct, widget=forms.Select)
    class Meta:
        model = Django_Khalid
        fields = '__all__'
        
class SignUp_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        

    
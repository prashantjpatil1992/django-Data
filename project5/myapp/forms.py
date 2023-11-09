from django import forms
from .models import Django_Khalid

class django_form(forms.ModelForm):
    gen = (('Male','Male'),('Female','Female'),('Other','Other'))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
    
    ct = (('Mumbai',"Mumbai"),("Thane","Thane"),("Ghatkopar","Ghatkopar"),("Nashik","Nshik"))
    city = forms.ChoiceField(choices=ct, widget=forms.Select)
    class Meta:
        model = Django_Khalid
        fields = '__all__'
    
from django import forms
from app1.models import reg, login

class regForm(forms.ModelForm):
    uname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name', 'class':'form-control','type':'text','id':'Name'}))
    uemail=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Email', 'class':'form-control','type':'email','id':'Email'}))
    upass=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Password', 'class':'form-control', 'type':'password','id':'Password'}))
    uadd=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Address', 'class':'form-control','type':'textarea','id':'Address'}))


    class Meta:
        model = reg 
        fields='__all__'
        
class loginform(forms.ModelForm):
    uname=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Name', 'class':'form-control','type':'text','id':'Name'}))
    upass=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Password', 'class':'form-control', 'type':'password','id':'Password'}))

    class Meta:
        model = login
        fields = '__all__' 
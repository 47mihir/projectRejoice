from django import forms
from .models import Person

class UsrForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('name','username','email','password', 'role')
        labels = {
            'name':'Name',
            'username':'Username',
            'email':'Email',
            'password':'Password',
            'role':'Role',
        }

    def __init__(self, *args, **kwargs):
        super(UsrForm,self).__init__(*args, **kwargs)
        self.fields['role'].empty_label = "Select"



class loginForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('username','password')
        widgets= {
            'password' : forms.PasswordInput(),
            }
    
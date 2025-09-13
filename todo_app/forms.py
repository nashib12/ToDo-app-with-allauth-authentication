from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import ToDoList

class ListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ('category', 'content', 'date',)
        
        labels = {
            'category' : '',
            'content' : '',
            'date' : '',
        }
        
        widgets = {
            'category' : forms.Select(attrs={'class' : 'form-control fs-5', 'id' : 'category'}),
            'content' : forms.TextInput(attrs={'class' : 'form-control fs-5', 'id' : 'content'}),
            'date' : forms.DateInput(attrs={'class' : 'form-control fs-5', 'id' : 'date', 'type' : 'date'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label=""  ,widget=forms.TextInput(attrs={'class' : 'form-control fs-5', 'id' : 'username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class' : 'form-control fs-5', 'id' : 'passwortd'}))
    
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'form-control fs-5', 'id' : 'fname'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class' : 'form-control fs-5', 'id' : 'lname'}))
    email = forms.CharField(label="", widget=forms.EmailInput(attrs={'class' : 'form-control fs-5', 'id' : 'email'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control fs-4'
        self.fields['username'].widget.attrs['id'] = 'username'
        
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control fs-4'
        self.fields['password1'].widget.attrs['id'] = 'password1'
        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control fs-4'
        self.fields['password2'].widget.attrs['id'] = 'password2'
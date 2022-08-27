from pyclbr import Class
from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    name = forms.CharField()
    id = forms.CharField()
    pw = forms.CharField()
    email = forms.EmailField()
    user_nickname = forms.CharField()
    user_school = forms.CharField()
    user_major = forms.CharField()
    user_favor = forms.CharField()

    class Meta:
        model = User
        fields = '__all__'
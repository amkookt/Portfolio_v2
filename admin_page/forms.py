from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreationUserForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super(CreationUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        # widgets = {
        #         'username'    : forms.TextInput(attrs={'class':'form-control'}),
        #         'email'       : forms.EmailInput(attrs={'class':'form-control'}),
        #         'password1'   : forms.PasswordInput(attrs={'class':'form-control'}),
        #         'password2'   : forms.PasswordInput(attrs={'class':'form-control'}),
        # }
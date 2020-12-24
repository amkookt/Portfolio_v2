from django import forms 
from .models import Project,About,Service

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title','languages','image','description')
        widgets = {
                'title'         : forms.TextInput(attrs={'class':'form-control'}),
                'languages'     : forms.TextInput(attrs={'class':'form-control'}),
                'image'         : forms.ClearableFileInput(attrs={'class':'form-control'}),
                'description'   : forms.Textarea(attrs={'class':'form-control'}),

        }


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('title','about_image','description')
        widgets = {
                'title'         : forms.TextInput(attrs={'class':'form-control'}),
                'about_image'   : forms.ClearableFileInput(attrs={'class':'form-control'}),
                'description'   : forms.Textarea(attrs={'class':'form-control'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('title_service','about_service','image_service')
        widgets = {
                'title_service'         : forms.TextInput(attrs={'class':'form-control'}),
                'about_service'   : forms.Textarea(attrs={'class':'form-control'}),
                'image_service'   : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }


# class ContactForm(forms.Form):

#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea)

#     def __init__(self, *args, **kwargs):
#         self.helper = FormHelper()
#         self.helper.add_input(Submit('submit', 'Submit'))
#         super(ContactForm, self).__init__(*args, **kwargs)



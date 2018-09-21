from django import forms
from django.contrib.auth.models import User
from elpapp.models import Employer,Student,AccessRecord,jobs,SUserProfileInfo,EUserProfileInfo
from django.core import validators

class EUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')

class EUserProfileInfoform(forms.ModelForm):
    class Meta():
        model = EUserProfileInfo
        fields = ('portfolio_site','profile_pic')

class SUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')

class SUserProfileInfoform(forms.ModelForm):
    class Meta():
        model = SUserProfileInfo
        fields = ('portfolio_site','profile_pic')

class NewStudentform(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'

        #def clean(self):
        #    all_clean_data = super().clean()
        #    email = all_clean_data['email']

class NewEmployerform(forms.ModelForm):
    class Meta():
        model = Employer
        fields = '__all__'

    #def clean(self):
    #    all_clean_data = super().clean()
    #    email = all_clean_data['email']


#I'd want to add a mobile number field and clean it too
#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput())
#    class Meta():
#        model = User
#        fields=('username','email','password')

#class UserProfileInfoform(forms.ModelForm):
#    class Meta():
#        model = UserProfileInfo
#        fields = ('portfolio_site','profile_pic')

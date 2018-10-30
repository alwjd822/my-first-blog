from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
 
class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=50,required=False)
    tel = forms.CharField(max_length=50,required=False)
    #gender = forms.BooleanField('성별',default=True)
    address = forms.CharField(max_length=50,required=False)
    birth = forms.DateField(required=False)

    def save(self):
        user =  super().save()

        profile = Profile.objects.create(
            user = user,
            name =self.cleaned_data['name'],
            tel =self.cleaned_data['tel'],
            #gender =self.cleaned_data['gender'],
            address =self.cleaned_data['address'],
            birth =self.cleaned_data['birth'])

        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tel', 'address']
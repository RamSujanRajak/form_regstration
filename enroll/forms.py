import datetime
from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField( widget=forms.TextInput(attrs={'class':'name'}))
    date_of_birth = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'class':'name'} ))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'name'}))
    def clean(self):
        cleaned_data=super().clean()
        date_of_birth = self.cleaned_data['date_of_birth']
        varname = self.cleaned_data['name']
        remail = self.cleaned_data['email']
        payphone = self.cleaned_data['phone']

        if len(varname) < 5:
            raise forms.ValidationError('Name should be more than or equal 4')
        
        if len(remail) < 10:
            raise forms.ValidationError('Email should be more than or equal 10 char')
        
        if len(payphone) <= 10:
            raise forms.ValidationError('phone number should be digits 10')

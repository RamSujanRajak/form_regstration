from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

# def thankyou(request):
#   return render(request, 'enroll/userregistration.html')

def thankyou(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   print('Form Validated')
   name = fm.cleaned_data['name']
   date_of_birth = fm.cleaned_data['date_of_birth']
   phone = fm.cleaned_data['phone']
   email = fm.cleaned_data['email']
   print('Name:', name)
   print('Email:', email)
   print('date_of_birth:', date_of_birth)
   print('phone:', phone)
   return render(request, 'enroll/success.html', {'nm':name})
   
 else:
  fm = StudentRegistration()

 return render(request, 'enroll/userregistration.html', {'form':fm})

def show_data(request):
  return render(request,'userregistration.html')
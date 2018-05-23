from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
  # the index function is called when root is visite
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
def index(request):
    
    return render(request,'login_registration/registration.html')

def new(request,id):
  context={
    'users': Users.objects.get(id=id)
  }
  return render(request,'login_registration/registration.html', context)
def new_registration(request):
  pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
  print("PASSWORD:",pw_hash)

  password_hash=pw_hash.decode('utf8')
  errors = Users.objects.basic_validator(request.POST)
        # check if the errors object has anything in it
  if len(errors):
      # if the errors object contains anything, loop through each key-value pair and make a flash message
      for key, value in errors.items():
          messages.error(request, value)
      # redirect the user back to the form to fix the errors
      return redirect('/new/'+id)
  else:
      user = Users.objects.create(first_name=request.POST['first_name'],
      last_name=request.POST['last_name'],
      email=request.POST['email'], password=password_hash)
      user.save()
      messages.success(request, "User successfully updated")
            # redirect to a success route
      return redirect('/success.html')

def login(request):
  
 return render(request,'login_registration/success.html')

def validate_login(request):
  user = Users.objects.get(email=request.POST['email'])
  if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
      print("password match")
  else:
      print("failed password") 
  return redirect('/')
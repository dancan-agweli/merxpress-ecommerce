from django.shortcuts import render, redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import authenticate,login 
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
        else:
            errmsg = form.errors
    else:
        form = SignUpForm()
        errmsg = None
    context={'form':form, 'errmsg': errmsg}
    return render(request,'signup.html',context)

def login(req):
    if req.method=='POST':
        form=LoginForm(req,req.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user=authenticate(req,email=email,password=password)
            if user is not None:
                login(req, user)
                print("hello")
                return redirect('home')
            else:
                form.add_error(None,'Invalid username or password')
    else:
        form =LoginForm()
    
    return render(req,'login.html',{'form': form})

def home(req):
    return render(req,'home.html')
    






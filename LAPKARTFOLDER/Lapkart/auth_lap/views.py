from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def register_view(request):
    reg = UserCreationForm()
    if request.method == 'POST':
        reg = UserCreationForm(request.POST)
        if reg.is_valid():
            reg.save()
            return HttpResponse('register')
    template_name = 'authlap/reg.html'
    context = {'reg':reg}
    return render(request,template_name,context)

def login_view(request):

    if request.method == 'POST':
        u = request.POST['un']
        p = request.POST['pw']

        user =authenticate(username=u, password=p)
        if user is not None:
            login(request,user)
            return redirect('/golap/show/')
        else:
            messages.add_message(request, messages.INFO,"Invalid UserInfo")

    template_name = "authlap/login.html"
    context = {}
    return render(request,template_name,context)

def logout_view(request):
    logout(request)
    return redirect('/lapauth/login/')

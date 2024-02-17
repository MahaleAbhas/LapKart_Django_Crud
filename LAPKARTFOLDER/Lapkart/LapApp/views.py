from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Lap_Form
from .models import Lap_Model

# Create your views here.
def Layout(request):
    template_name = "temp/Layout.html"
    context = {}
    return render(request,template_name,context)
def Add_view(request):
    form = Lap_Form()
    if request.method == 'POST':
        form = Lap_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/golap/show/')

    template_name = ('temp/Add.html')
    context = {"form":form}
    return render(request,template_name,context)

@login_required(login_url="/lapauth/login/")
def Show_View(request):
    template_name = 'temp/show.html'
    All_Show = Lap_Model.objects.all()
    context = {"All_Show":All_Show}
    return render(request,template_name,context)

def Update_view(request,i):
    upd_info = Lap_Model.objects.get(id=i)
    form = Lap_Form(instance=upd_info)
    if request.method == 'POST':
        form = Lap_Form(request.POST,instance=upd_info)
        if form.is_valid():
            form.save()
            return redirect('/golap/show/')

    template_name = ('temp/Add.html')
    context = {"form":form}
    return render(request,template_name,context)

def Delete_View(request,i):
    del_info = Lap_Model.objects.get(id=i)
    del_info.delete()
    return redirect('/golap/show/')
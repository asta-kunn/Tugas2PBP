from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import BarangTodolist
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.username
    todolist_data = BarangTodolist.objects.filter(user=request.user)
    context = { 
        "nama": username,
        "todo_list": todolist_data,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def tambah_input(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user
        data = BarangTodolist(user=user, title=title, description=description)    
        data.save()
        return redirect("todolist:show_todolist")
    return render(request, "create-task.html", context)
    
def hapus_input(request, pk):
    data = BarangTodolist.objects.filter(pk=pk)
    data.delete()
    return redirect("todolist:show_todolist")

def cheklist_todolist(request, pk):
    data = BarangTodolist.objects.get(id=pk)
    if(data.status == False):
        data.status = True
    else:
        data.status = False
    data.save()
    return redirect("todolist:show_todolist")

def registrasi(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful")
            return redirect("todolist:login")
    context = {"form":form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.warning(request, "Username OR password is incorrect")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
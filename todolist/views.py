from this import d
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from todolist.models import BarangTodolist
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = { 
        "nama": request.user,
    }
    return render(request, "todolist.html", context)

# create function to show json
@login_required(login_url='/todolist/login/')
def show_json(request):
    todolist_data = BarangTodolist.objects.filter(user=request.user)
    
    return HttpResponse(serializers.serialize("json", todolist_data), content_type='application/json')

@login_required(login_url='/todolist/login/')
def tambah_input(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user
        data = BarangTodolist(user=user, title=title, description=description,  date=datetime.datetime.today())    
        data.save()
        return redirect("todolist:show_todolist")
    return render(request, "create-task.html", context)

@login_required(login_url='/todolist/login/')
def hapus_input(request, pk):
    # data = BarangTodolist.objects.filter(pk=pk)
    # data.delete()
    # return redirect("todolist:show_todolist")
    if request.method == "DELETE":
        data = BarangTodolist.objects.get(user=request.user,pk=pk)
        data.delete()
        return JsonResponse(
            {
                "pk": data.pk,
                "fields": {
                "title": data.title,
                "description": data.description,
                "status": data.status,
                "date": data.date,
                },

            },
            status=200,
        )

def cheklist_todolist(request, pk):
    if request.method == "PUT":
        data = BarangTodolist.objects.get(user=request.user,pk=pk)
        data.status = not data.status
        data.save()
        return JsonResponse(
            {
                "pk": data.pk,
                "fields": {
                "title": data.title,
                "description": data.description,
                "status": data.status,
                "date": data.date,
                },

            },
            status=200,
        )

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

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method ==  "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user
        data = BarangTodolist.objects.create(user=user, title=title, description=description, date=datetime.datetime.today())    
        return JsonResponse({
            "pk": data.pk,
            "fields": {
                "title": data.title,
                "description": data.description,
                "status": data.status,
                "date": data.date,
            },
        },
        status=200,
        )

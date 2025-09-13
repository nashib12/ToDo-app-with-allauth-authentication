from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .models import ToDoList
from .forms import ListForm, LoginForm, CustomUserCreationForm


def home(request):
    # list = List.objects.filter(author=request.user, is_deleted=False)
    context_dict = {
        # "list" : list,
    }
    return render(request, "todo_app/index.html", context_dict)

@login_required(login_url="log-in")
def details(request):
    list = ToDoList.objects.filter(author=request.user, is_deleted=False)
    context_dict = {
        "list" : list,
    }
    return render(request, "todo_app/details.html", context_dict)
    

def createUser(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Log In successfull!")
            return redirect("home")
        else:
            messages.error(request, "Username or password doesnot match")
            return redirect("log-in")
    
    context_dict = {
        "form" : form,
    }
    
    return render(request, "todo_app/createuser.html", context_dict)

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Log In successfull!")
                return redirect("home")
            else:
                messages.error(request, "Username or password doesnot match")
                return redirect("log-in")
    else:
        form = LoginForm()
        
    context_dict = {
        "form" : form,
    }

    return render(request, "todo_app/login.html", context_dict)

@login_required(login_url="log-in")
def log_out(request):
    logout(request)
    messages.success(request, "Successfully Log out")
    return redirect("log-in")

@login_required(login_url="log-in/")
def addItem(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        
        messages.success(request, "Item added successfully")
        return redirect("home")
    
    context_dict = {
        "form" : form,
    }
    
    return render(request, "todo_app/additem.html", context_dict)

@login_required(login_url="log-in")
def updateItem(request, id):
    item = ToDoList.objects.get(id=id)
    form = ListForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Item updated successfully")
        return redirect("home")
    
    context_dict = {
        "form" : form,
    }
    
    return render(request, "todo_app/updateitem.html", context_dict)

@login_required(login_url="log-in")
def deleteItem(request, id):
    if not request.method == "POST":
        messages.error(request, "Invalid")
        return HttpResponse("error")
    
    item = ToDoList.objects.get(id=id)
    if not item.is_deleted:
        item.is_deleted = True
        item.save()
        messages.success(request, "Item successfully deleted")
        return redirect("home")
    else:
        item.is_deleted = False
        item.save()
        messages.success(request, "Item Successfully restored")
        return redirect("home")

@login_required(login_url="log-in")
def recycleItem(request):
    list = ToDoList.objects.filter(author=request.user, is_deleted=False)
    context_dict ={
        'list' : list,
    }
    
    return redirect(request, "todo_app/recycle.html", context_dict)


        


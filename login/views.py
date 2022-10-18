from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.http import HttpResponse, JsonResponse
import login
from .models import Project, Task, User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserRegisterForm


# Create your views here.

    
def register(request):
    if request.method =='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            ''' return redirect('home')'''
    else:
        form = UserRegisterForm()

    context = { 'form' : form}
    return render(request, 'register.html', context)


def index(request):
    return render(request,"index.html")

def home(request):
    return render(request, "home.html")

def register(request):
    
    register_form  = UserRegisterForm
    contexto ={'register_form': register_form}
    if request.method == 'POST':
        register_form = UserRegisterForm
    return render(request, "register.html", contexto)
    
def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>"% username)

def about(request):
    return HttpResponse('About')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    ''''task= Task.objects.get(id=id)'''
    task = Task.objects.get(title=title)
    return HttpResponse('tasks: %s' % task.title)

def schedulemeetings(request):
    return render(request, "schedulemeetings.html")

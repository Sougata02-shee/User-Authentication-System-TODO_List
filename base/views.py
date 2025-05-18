from django.shortcuts import redirect, render
from .models import TaskModel
from .forms import TaskForm
from django.db.models import Q

# Create your views here.

def home(request):
    if request.method=='GET':
        if 'search' in request.GET:
            search=request.GET['search']
            all=TaskModel.objects.filter(Q(title__contains=search) & Q(host=request.user) |Q(desc__contains=search)& Q(host=request.user) )   

        else:
            all=TaskModel.objects.filter(host=request.user)


    return render(request,'home.html',{'all':all})

def addtask(request):

    if request.method=='POST':
        form=TaskForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form=TaskForm(initial={'host':request.user})

    return render(request,'addtask.html',{'form':form})


        
 
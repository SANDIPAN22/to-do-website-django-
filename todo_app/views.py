from django.shortcuts import render,redirect
from todo_app.models import taskModel
from todo_app.form import task_add_form
# Create your views here.
def index(request):
    addForm=task_add_form()
    context={'result':taskModel.objects.all,
    'addForm':task_add_form}

    if request.method=='post' or request.method=='POST':
        addForm_resp=task_add_form(request.POST)
        if addForm_resp.is_valid:
            addForm_resp.save()
        return redirect('/')



    return render(request,'index.html',context) 

def updateTask(request, pk):
    t1=taskModel.objects.get(id=pk)
    tt1=task_add_form(instance=t1)
    context={'updateForm':tt1}
    if request.method=='POST':
        form_update_resp=task_add_form(request.POST,instance=t1)
        if form_update_resp.is_valid:
            form_update_resp.save()
        return redirect('index')
    return render(request,'update.html',context)

def deleteTask(request,pk):
    d1=taskModel.objects.get(id=pk)
    context={'d1':d1}
    if request.method=='POST':
        d1.delete()
        return redirect('index')
    return render(request, 'del.html',context)
from django.shortcuts import render,redirect
from to_do_app.models import ToDo_Datas
from django.contrib import messages


# Create your views here.

def Home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        date = request.POST.get('date')
        data = ToDo_Datas()
        if len(content) == 0 or len(date) == 0:
            messages.error(request, 'Please fill the required feilds')
        else:
            data.Content = content
            data.Date = date
            data.save()
            messages.success(request, 'Datas are saved successfully')
    return render(request, 'to_do_app/index.html')

def View(request):
    data = ToDo_Datas.objects.all()
    return render(request, 'to_do_app/view.html',{'data':data})

def viewdata(request):
    return redirect('/to_do_app/View')

def delete(request,id):
    data = ToDo_Datas.objects.get(id=id).delete()
    messages.success(request, 'Data deleted successfully')
    return redirect('/to_do_app/View')

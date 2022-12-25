from django.shortcuts import render, redirect
from .forms import StudentDetailForm, ResultDetailForm
from django.views.generic.list import ListView
from .models import StudentDetail, ResultDetail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http.request import QueryDict


# Create your views here.

def index(request): 
    stu = StudentDetailForm()
    if request.POST:
        stu = StudentDetailForm(request.POST)
        if stu.is_valid():
            print(stu, "----1")
            stu.save()
            stu = StudentDetailForm() 
            return render(request,"studentDetails/index.html",{'form':stu, 'success_message': 'true'})
        else:
            print(stu, "---2")
            stu = StudentDetailForm(request.POST)
            return render(request,"studentDetails/index.html",{'form':stu, 'success_message': 'false'})

    return render(request,"studentDetails/index.html",{'form':stu})  





def StudentListView(request):

    students = StudentDetail.objects.all()
    results = ResultDetail.objects.all()

    return render(request, 'studentDetails/studentdetail_list.html', context = {'students':students, 'results': results})


def result_add_index(request): 
    res = ResultDetailForm()
    if request.POST:
        print(type(request.POST))
        res = ResultDetailForm(request.POST)
        if res.is_valid():
            print(res, "----1")
            res.save()
            res = ResultDetailForm() 
            return render(request,"studentDetails/resultadd.html",{'form':res, 'success_message': 'true'})
        else:
            print(res, "---2")
            res = ResultDetailForm(request.POST)
            return render(request,"studentDetails/resultadd.html",{'form':res, 'success_message': 'false'})
    
    return render(request,"studentDetails/resultadd.html",{'form':res})  


def result_add_pk(request, pk):

    if request.method == 'POST':
        
        res = ResultDetailForm(request.POST)
        print(request.POST)
        if res.is_valid():
            res.save()
            res = ResultDetailForm()
            return render(request,"studentDetails/resultadd.html",{'form':res, 'success_message': 'true'})
        
        else:
            print("Here-2")
            res = ResultDetailForm(request.POST)
            return render(request,"studentDetails/resultadd.html",{'form':res, 'success_message': 'false'})

    elif request.method == 'GET':
        #print(pk, StudentDetail.objects.all().count(), pk<=StudentDetail.objects.all().count())
        if pk > 0 and pk <= StudentDetail.objects.all().count():
            try:
                res = ResultDetailForm(initial = {'student': StudentDetail.objects.get(pk = int(pk))})
                return render(request,"studentDetails/resultadd.html",{'form':res})
            except:
                return redirect(reverse('addstudent'))

        elif pk >0:
            return redirect(reverse('addstudent'))



    res = ResultDetailForm()
    return render(request,"studentDetails/resultadd.html",{'form':res})


def error_404_view(request, exception):
   
    return redirect(reverse('studentlist'))
from django.shortcuts import render,redirect
from .models import Client
from .forms import ClientForm
from .retirementAge import retirementage
from .graph import graph1,graph2

# Create your views here.

def createClient(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            #add user if necessary
            new.save()
            name = form.cleaned_data['name']
            salary = float(form.cleaned_data['annual_income'].amount)
            age = form.cleaned_data['age']
            savings = salary - float(form.cleaned_data['annual_expenses'].amount)
            new_age = retirementage(age,salary,savings)
            fig1 = graph1(salary,age)
            # fig2 = graph2(salary,age,savings)
            # return render(request,'invest/result.html',{'name':name,'cur_age':age,'ret_age':new_age,'fig1':fig1,'fig2':fig2})
            return render(request,'invest/result.html',{'name':name,'cur_age':age,'ret_age':new_age,'fig1':fig1})
        else:
            pass
    else:
        return render(request,'invest/create.html',{'form':ClientForm()})
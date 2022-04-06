from multiprocessing import context
from django.shortcuts import render
from .models import HighPriority,LowPriority
# Create your views here.
def homeView(request):
    return render(request,"index.html",{})


def aboutdmft(request):
    return render(request,"dmft.html",{})

def directlyAffectedArea(request):
    return render(request,"affectedarea.html",{})

def indirectAffectedArea(request):
    return render(request,"affectedarea.html",{})
def teamView(request):
    return render(request,"team.html",{})

def projectView(request):

    return render(request,"projects.html",{})

def HighPriorityView(request):
    highprioritydata = HighPriority.objects.all()
    context = {
        "highprioritydata":highprioritydata
    }
    return render(request,"highpriority.html",context)


def LowPriorityView(request):

    lowprioritydata = LowPriority.objects.all()
    context = {
        "lowprioritydata":lowprioritydata
    }
    return render(request,"lowpriority.html",context)


def pressRelease(request):
    return render(request,"press.html",{})

def photoGallery(request):
    return render(request,"photogallery.html",{})

def AnnualreportView(request):

    return render(request,"anualreport.html",{})

def AuditreportView(request):

    return render(request,"auditreport.html",{})
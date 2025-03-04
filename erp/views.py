from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from User.models import User, Profile


# Create your views here.

@login_required(login_url='login/')
def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'erp/index.html', context)


def groups(request):
    return render(request,'erp/gruops.html')

def staff(request):
    return render(request,'erp/staff.html')

def attendance(request):
    return render(request,'erp/attendance.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from User.models import User, Profile
from erp.forms import VideoModelForm, AttendanceModelForm, HomeworkModelForm
from erp.models import Video, Attendance, Homework

# Create your views here.

@login_required(login_url='login/')
def index(request):
    profile = Profile.objects.get(user=request.user)
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

def settings(request):
    return render(request, 'erp/setttings.html')


def videos(request):
    if request.method == 'POST':
        form = VideoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('erp:video_list')
    else:
        form = VideoModelForm()
    return render(request, 'erp/videos.html', {'form': form})




def videos_list(request):
    videos = Video.objects.all()
    search_query = request.GET.get('q','')
    if search_query:
        videos = Video.objects.filter(name__icontains=search_query)
    context = {
        'videos': videos
    }

    return render(request,'erp/videos.html', context=context)

def video_watch(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {
        'video': video,
    }
    return render(request,'erp/watch_video.html', context=context)

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    video.delete()
    return redirect('erp:video_list')


def attendance_view(request):
    profile = Profile.objects.all()
    if request.method == 'POST':
        form = AttendanceModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('erp:attendance')
    else:
        form = AttendanceModelForm()

    context = {
        'profiles': profile,
        'form': form
    }
    return render(request, 'erp/attendance.html', context=context)


def delete_homework(request, pk):
    homework = get_object_or_404(Homework, pk=pk)
    homework.delete()
    return redirect('erp:homework')



class CreateVideo(CreateView):
    model = Video
    form_class = VideoModelForm
    template_name = 'erp/create_video.html'
    success_url = reverse_lazy('erp:video_list')


class EditVideo(UpdateView):
    model = Video
    form_class = VideoModelForm
    template_name = 'erp/edit.html'
    success_url = reverse_lazy('erp:video_list')


def homework(request):
    homework = Homework.objects.all()
    search_query = request.GET.get('q','')
    if search_query:
        homework = Homework.objects.filter(name__icontains=search_query)

    context = {
        'homeworks': homework
    }
    return render(request, 'erp/homework.html', context=context)

def homework_detail(request,pk):
    homework = get_object_or_404(Homework, pk=pk)
    context = {
        'homework': homework
    }
    return render(request,'erp/homework_detail.html', context=context)


class CreateHomework(CreateView):
    model = Homework
    form_class = HomeworkModelForm
    template_name = 'erp/create_home.html'
    success_url = reverse_lazy('erp:homework')


class EditHomework(UpdateView):
    model = Homework
    form_class = HomeworkModelForm
    template_name = 'erp/edit_home.html'
    success_url = reverse_lazy('erp:homework')
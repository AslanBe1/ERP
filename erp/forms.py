from django import forms

from erp.models import Video, Attendance, Homework


class VideoModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class AttendanceModelForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status']


class HomeworkModelForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'is_present': forms.CheckboxInput()
        }
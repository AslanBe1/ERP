from django.utils import timezone
import cv2
from django.db import models
from User.models import User, Profile


# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    duration = models.FloatField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='videos', null=True)

    def __str__(self):
        return self.lesson.name

    def get_absolute_url(self):
        return self.video.url

    def save(self, *args, **kwargs):
        if self.video and not self.duration:
            self.duration = get_video_duration(self.video.path)
            super().save(*args, **kwargs)

def get_video_duration(file_path):
    cap = cv2.VideoCapture(file_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    cap.release()
    if fps > 0:
        return round(frame_count / fps, 2)
    return 0


class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student} => {self.date} => {self.status}'



class Homework(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='homeworks')

    def __str__(self):
        return self.lesson.name

    def save(self, *args, **kwargs):
        if self.deadline <= timezone.now():
            raise ValueError("Deadline passed, cannot save.")
        super().save(*args, **kwargs)
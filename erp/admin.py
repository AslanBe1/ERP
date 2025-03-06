from django.contrib import admin

from erp.models import Lesson, Video, Attendance, Homework

# Register your models here.

admin.site.register(Lesson)
admin.site.register(Attendance)


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline')
    search_fields = ('name',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video','duration')
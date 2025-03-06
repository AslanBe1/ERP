from django.urls import path

from erp import views

app_name = 'erp'

urlpatterns = [
    path('erp/', views.index, name='index'),
    path('groups/',views.groups, name='groups'),
    path('staff/',views.staff, name='staff'),
    path('settings/',views.settings, name='settings'),
    path('attendance/',views.attendance_view, name='attendance'),
    path('video/', views.videos_list, name='video_list'),
    path('videos/<int:pk>/', views.video_watch, name='videos'),
    path('create-video/', views.CreateVideo.as_view(), name='create_video'),
    path('edit-video/<int:pk>/', views.EditVideo.as_view(), name='edit_video'),
    path('delete-video/<int:pk>/', views.delete_video, name='delete_video'),
    path('homework/', views.homework, name='homework'),
    path('homework-detail/<int:pk>/', views.homework_detail, name='homework_detail'),
    path('create-homework/', views.CreateHomework.as_view(), name='create_homework'),
    path('edit_homework/<int:pk>/', views.EditHomework.as_view(), name='edit_homework'),
    path('delete-homework/<int:pk>/', views.delete_homework, name='delete_homework'),
]
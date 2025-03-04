from django.urls import path

from erp import views

app_name = 'erp'

urlpatterns = [
    path('erp/', views.index, name='index'),
    path('groups/',views.groups, name='groups'),
    path('staff/',views.staff, name='staff'),
    path('attendance/',views.attendance, name='attendance'),
]
from django.urls import path

from User import views

app_name = 'user'

urlpatterns = [
    path('register-page/', views.register, name='register'),
    path('erp/login/', views.login_page, name='login'),
    path('logout-page/', views.logout_page, name='logout'),
]
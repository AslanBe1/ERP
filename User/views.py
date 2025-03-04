import random
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from User.forms import RegisterForm, LoginForm


# Create your views here.

def generate_verify_code():
    return str(random.randint(100000, 999999))

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            get_name_by_email = user.email.split('@')[0]
            user.set_password(form.cleaned_data['password'])
            user.save()
            verification_code = generate_verify_code()
            send_mail(
                'Code',
                f'Code {verification_code}',
                'aslanabdimuminov31@gmail.com',
                [user.email],
                fail_silently=False,
            )
            request.session['verification_code'] = verification_code
            request.session['password'] = password
            request.session['email'] = user.email

            request.session['user_data'] = {
                'email': user.email,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser,
            }

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Your account has been created!')
            return redirect('erp:index')

    context = {
        'form': form,
    }
    return render(request, 'User/register.html', context=context)



def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('erp:index')

            else:
                messages.add_message(request, messages.ERROR, 'Invalid login')

    context = {
        'form': form,
    }

    return render(request, 'User/login.html', context=context)

def logout_page(request):
    logout(request)
    return redirect('erp:index')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        email = email.lower()

        if password1 == password2 and password1 :
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'username is taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            messages.info(request, 'Passward is not matching')
            return redirect('register')
        
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
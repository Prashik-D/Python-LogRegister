from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):
    return render(request, 'users/main.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.danger(request, 'Username is Already Exists!')
                return render(request, 'users/register.html')

            elif User.objects.filter(email=email).exists():
                messages.danger(request, 'Email is Already Exists!')
                return render(request, 'users/register.html')

            else:
                user = User.objects.create_user(username=username,  email=email, password=password1)
                user.save()
                return redirect('login')
    else:
        return render(request, 'users/register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Invalid!')
            return render(request, 'users/login.html')
    else:
        messages.info(request, 'Sorry, Network Problem, Please try later!')
        return render(request, 'users/login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')
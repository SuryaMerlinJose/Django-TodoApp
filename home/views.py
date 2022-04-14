from django.contrib.auth import authenticate, login, logout


from .models import Task


from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# Create your views here.
from django.http import HttpResponse

def create_user(request):
    if request.method == 'POST':
        check1 = False
        check2 = False
        check3 = False
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            if password != password1:
                check1 = True
                messages.error(request, 'Password did not match!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(username=username).exists():
                check2 = True
                messages.error(request, 'Username already exists!',
                               extra_tags='alert alert-warning alert-dismissible fade show')
            if User.objects.filter(email=email).exists():
                check3 = True
                messages.error(request, 'Email already registered!',
                               extra_tags='alert alert-warning alert-dismissible fade show')

            if check1 or check2 or check3:
                messages.error(
                    request, "Registration Failed!", extra_tags='alert alert-warning alert-dismissible fade show')
                return redirect('/create_user')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email)
                messages.success(
                    request, f'Thanks for registering {user.username}.', extra_tags='alert alert-success alert-dismissible fade show')
                return redirect('/loginview')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})





def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        #date = request.POST['date']
        print(title,desc)
        ins= Task(taskTitle=title,taskDesc=desc)
        ins.save()
        context={'success':True}

    return render(request,'index.html', context)
def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks':allTasks}
    return render(request,'tasks.html',context)

def delete(request, id):
    if request.method=='POST':
        y = Task.objects.get(id= id)
        y.delete()
        return  redirect('/')
    return render(request,'delete.html')




def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect_url = request.GET.get('next', 'home')
            return render(request,"index.html")
        else:
            messages.error(request, "Username Or Password is incorrect!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'login.html')


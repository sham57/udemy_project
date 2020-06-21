from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        #get values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is already taken')
                    return redirect('register')
                else:#llooks good
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,password=password,email=email,username=username)
                    user.save()
                    #to keep registerd user loged in
                    # auth.login(request,user)

                    # messages.success(request,'you are logged in')
                    # return redirect('index')
                    messages.success(request,'you have registered and can now log in')
                    return redirect('login')
            
        else:
            messages.error(request, 'Password unmatched!!!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you have succesfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'you have logged out')
        return redirect('index')


def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contact
    }

    return render(request, 'accounts/dashboard.html', context)

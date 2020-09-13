from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User , auth
# Create your views here.

# method for the Index or main Page
def index(request):
    return render(request, 'users/index.html')

# method the perform Login in the System
def login(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request , user)
            return redirect('productapp:home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'users/login.html')


# method for the Registeration of the User
def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 ==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request , 'Username Already Taken')
                return redirect('register')
            elif User.objects.filter(email =email).exists():
                messages.info(request , 'Email Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username =username , password = password1 , email = email , first_name = first_name , last_name = last_name)
                user.save()
                messages.info(request , 'Please check mail address for Email and Password')
                send_mail('Welcome to multi database system' , 
               'Your user name is :-   ' + username + '  And password is :-   ' + password1  , 
               'jeevanc162@gmail.com' , 
               [email] ,
               fail_silently = False)
                return redirect('login')
        else:
            messages.info(request , 'password not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'users/register.html')

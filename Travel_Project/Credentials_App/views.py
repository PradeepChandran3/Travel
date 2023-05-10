from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def login (request):
    if request.method == 'POST':
        logname = request.POST["username"]
        logpassword = request.POST["password"]
        user=auth.authenticate(username=logname,password=logpassword)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('log')

    return render(request,"login.html")

def register (request):
    if request.method== 'POST':
        u_name =request.POST['username']
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        pwd = request.POST['password']
        c_pwd = request.POST['confirmpassword']

        if pwd==c_pwd:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,"Username Taken")
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect("reg")
            else:
                user=User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pwd)

                user.save();
                return redirect('log')
            # print("User Created")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("reg")
        return redirect('/')
    return render(request,"register.html")
def logout (request):
    auth.logout(request)
    return redirect('/')

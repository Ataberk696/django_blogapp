from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blogapp.decorators import authenticated_redirect

# Create your views here.

@authenticated_redirect
def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request,"account/login.html", {
                "error": "username ya da parola yanlış"
            })


    return render(request, "account/login.html")

@authenticated_redirect
def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                 return render(request, "account/register.html", 
                               {
                                    "error": "Username kullanılıyor.",   
                                    "username":username,                                 
                                    "firstname":firstname,
                                    "lastname":lastname,  
                                    "email":email,                              
                                })
            else:
                if User.objects.filter(email = email):
                     return render(request, "account/register.html",
                                    {
                                        "error": "Mail hesabı sistemimize kayıtlı.",
                                        "username":username,
                                        "email":email,
                                        "firstname":firstname,
                                        "lastname":lastname,                                   
                                    })
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password, is_active=False)
                    user.save()
                    return redirect("login")
                    
        else:
            return render(request, "account/register.html", 
                          {
                                "error": "girdiğiniz parolalar eşleşmiyor.",
                                "username":username,
                                "email":email,
                                "firstname":firstname,
                                "lastname":lastname,                                        
                          })
        
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")
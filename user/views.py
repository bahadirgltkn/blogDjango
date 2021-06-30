from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None) # get request olursa bos olarak davranacak 
    # Post islemi gerceklesirse valid islemine girecek 
    # Get islemi gerceklesir ise yalnızca bos context ile form olusturulacak
    if form.is_valid():
        # is_valid ile birlikte forms icerisinde yazılan clean() metodu calistirilir ve parola kontrolu gerceklesmesi saglanır
        username = form.cleaned_data.get("username")
        checkUsername =  User.objects.filter(username = username)
        if checkUsername:
            messages.warning(request,"Username already exist !")
            return render(request,"register.html",{"form" : form})
        else:
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
        
            newUser = User(username = username)
            newUser.email = email
            newUser.set_password(password)
            newUser.save()
            login(request,newUser)
            # login ile kayıt olan kullanıcıyı giris yaptıracak
            messages.success(request,"You have successfully registered...")
        
            return redirect("index") # ve sonrasında index sayfasına redirect olacak
    
    context = {
        "form" : form
    }
    
    return render(request, "register.html", context)
           
           
def loginUser(request):
    
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username, password = password)
        # authenticate ile kullanıcı adı ve password eslesmesi kontrol ediliyor sayet boyle bir kullanıcı yoksa veya var ama parola eslesmiyorsa hata mesajı yolluyoruz
        if user is None:
            messages.warning(request,"Username or Password is incorrect !")
            return render(request, "login.html", context)
        
        messages.success(request,"You have successfully logged in...")
        login(request, user)
        return redirect("index")

    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request," You have succesfully logged out...")
    
    return redirect("index")

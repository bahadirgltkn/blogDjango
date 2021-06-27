from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles": articles})
    
    articles = Article.objects.all()
    
    return render(request, "articles.html",{"articles" : articles} )

def index(request):
    # request her view isleminde olmak zorunda get ve post islemleri icin request kullanılacak
    # view icerisinde ister httpresponse olarak istersek de template seklinde bir return alabiliriz
    #return HttpResponse("<h3> Ana sayfa </h3>")
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url= "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    
    context = {
        "articles" : articles
        # yazara ait tum makaleler sozluk yapısı olarak alınmıs oldu
        # artık on tarafta bunları for donugusu ile yazdırabiliriz
    }
    
    return render(request,"dashboard.html",context)

@login_required(login_url= "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        # form tarafında author bilgisi alınmadığı icin bunu elle eklememiz gerekmektedir
        # sonrasında database kaydetme islemini gerceklestirebiliriz
        article.author = request.user
        article.save()
        
        articles = Article.objects.filter(author = request.user)
        # update dashboard
        context = {
        "articles" : articles
        }

        messages.success(request,"Article created successfully !")
        return render(request,"dashboard.html",context)
    
    return render(request,"addArticle.html", {"form" : form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    # ilgili id'ye sahip makale icin ozel sayfa olusturmak icin
    # first() bize liste yerine obje donecektir
    
    article = get_object_or_404(Article, id = id)
    
    return render(request,"detail.html",{"article" : article})

@login_required(login_url= "user:login")
def updateArticle(request,id):
    
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance= article)
    # instance --> loading old data
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        articles = Article.objects.filter(author = request.user)
        context = {
        "articles" : articles
        }

        messages.success(request,"Article updated successfully !")
        return render(request,"dashboard.html",context)
    
    return render(request,"update.html", {"form" : form})

@login_required(login_url= "user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id= id)
    article.delete()
    messages.success(request,"Article deleted successfully !")
    
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    
    return render(request,"dashboard.html", context)

def addComment(request, id):
    pass
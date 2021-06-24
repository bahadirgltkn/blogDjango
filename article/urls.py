from django.contrib import admin
from django.urls import path
from . import views

app_name = "artcile"
# article icerisindeki url yonlendirmelerini buradan yapacagız
# daha moduler hale getirmek icin buna basvurduk

urlpatterns = [
    
    path('dashboard/',views.dashboard, name = "dashboard"),
    path('addarticle/',views.addArticle, name = "addarticle"),
    path('article/<int:id>',views.detail, name = "detail"),
    path('update/<int:id>',views.updateArticle, name = "update"),
    path('delete/<int:id>',views.deleteArticle, name = "delete"),
   
]
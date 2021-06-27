from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE) # hangi tabloyu gosterdiğini foreign key ile belirtiriz
    title = models.CharField(max_length = 50)
    
    content = RichTextField()
    # richtextfield kullanılabilmesi icin {{myform.media}} seklinde html sayfasında bir kullanıma ihtiyacımız var
    # ayrıca on tarafta bir bozulma olmaması icin ve form yapısıyla uygunluk gostermesi icin settings.py icerisinde bunu confıg ile belirtmeliyiz
    
    createdDate = models.DateTimeField(auto_now=True)
    #tarih otomatik olarak eklenecek
    articleImage = models.FileField(blank=True, null=True ,verbose_name= " Add photo to article ")
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name = "Article",related_name="comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "name")
    comment_content = models.CharField(max_length = 200, verbose_name = "comment")
    comment_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment_content
        
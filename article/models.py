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
    def __str__(self):
        return self.title
    

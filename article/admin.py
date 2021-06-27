from django.contrib import admin
from .models import Article, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    #list display icerisinde admin panelinde hangi alanların gorunmesini istiyorsak belirtmeliyiz
    list_display = ["title","author","createdDate"]
    list_display_links = ["title","author"]
    search_fields = ["title"]
    list_filter = ["createdDate"]
    
    
    class Meta:
        model = Article
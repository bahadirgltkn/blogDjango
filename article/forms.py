from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # form ile article modeli baglantılı hale getirilmis oldu
        fields = ["title","content"]
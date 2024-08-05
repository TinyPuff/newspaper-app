from django import forms
from .models import Article

# Customizing the forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'body',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;'}),
            # 'author': forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;'}),
        }

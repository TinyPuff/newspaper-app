from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Article

# Create your views here.


class HomePageView(ListView):
    model = Article
    fields = ('title', 'author', 'date', )
    template_name = 'home.html'
    context_object_name = 'article'
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Article
from .forms import ArticleForm

# Create your views here.


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'new_article.html'
    # fields = ("title", "author", "body",)

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    # fields = ("title", "body",) # might add author here
    template_name = 'edit_article.html'
    success_url = reverse_lazy('home')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

class ArticleView(DetailView):
    model = Article
    template_name = 'article_details.html'
    # context_object_name = 'article'
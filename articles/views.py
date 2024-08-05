from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
from .forms import ArticleForm

# Create your views here.


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'new_article.html'
    login_url = 'login'
    # fields = ("title", "author", "body",)
    
    def form_valid(self, form): # The author's name is now selected automatically.
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    # fields = ("title", "body",) # might add author here
    template_name = 'edit_article.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_details.html'
    # context_object_name = 'article'
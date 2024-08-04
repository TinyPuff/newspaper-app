from django.urls import path
from .views import ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleView


urlpatterns = [
    path('new/', ArticleCreateView.as_view(), name='new_article'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='edit_article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
    path('<int:pk>/', ArticleView.as_view(), name='article_details'),
]
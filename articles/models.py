from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.pk)])


class Comment(models.Model):

    post = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    comment = models.TextField(max_length=250)

    def __str__(self):
        return str(self.comment[:50])
    
    
        

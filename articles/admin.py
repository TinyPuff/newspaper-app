from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInline(admin.StackedInline):  # Can change StackedInline to TabularInline to take less space
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

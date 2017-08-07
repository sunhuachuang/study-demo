from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article
# Create your views here.


def index(request):
    return render(request, "articles/index.djhtml", {
        "articles": Article.objects.all()
    })


def details(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "articles/details.djhtml", {"article": article})

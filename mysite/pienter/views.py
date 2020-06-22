from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Acount, Article


def index(request):
    article_list = Article.objects.all()
    context = {
        "article_list": article_list,
    }
    return render(request, "pienter/index.html", context)


def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Pien does not exist")
    return render(request, "pienter/detail.html", {"article": article})


def acountpage(request, user_id):
    try:
        acount = Acount.objects.get(user_id=user_id)
        articles_list = Article.objects.all()
        context = {
            "acount": acount,
            "article_list": articles_list,
        }
    except Article.DoesNotExist:
        raise Http404("Pien does not exist")
    return render(request, "pienter/acountpage.html", context)

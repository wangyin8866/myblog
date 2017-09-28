from django.shortcuts import render
from django.http import HttpResponse

from . import models


# Create your views here.
def index(request):
    # 从数据库中获取所有对象 查
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    # 从数据库中获取对应对象 pk= .主键 id  查
    article = models.Article.objects.get(pk=article_id)

    return render(request, 'blog/article_page.html', {'article': article})


def article_edit(request, article_id):
    if str(article_id) == '0':  # 创建新消息

        return render(request, 'blog/edit_page.html', {'article_id': '0'})
    else:  # 修改消息
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/edit_page.html', {'article': article})


def article_edit_action(request):
    title = request.POST.get('title', 'TITLE')  # 获取传过来的参数
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('id', '0')
    if str(article_id) == '0':
        # 创建对象  增
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
    else:  # 改
        #   第一种
        models.Article.objects.filter(pk=article_id).update(title=title, content=content)
        #   第二种
        # article = models.Article.objects.get(pk=article_id)
        # article.title = title
        # article.content = content
        # article.save()
        articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_delete(request, article_id):
    models.Article.objects.filter(pk=article_id).delete()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

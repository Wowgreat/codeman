from codeman.models import Article, Group, User
from codeman.serializers import ArticleSerializer
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.views import APIView
from .commonFunc import *

"""
create article
"""


class ArticleAdd(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, format=None):
        return Response({"必要字段": "title,content,post_man,group"})

    def post(self, request, format=None):
        form_data = request.data
        user_info = jwtdecode(form_data.get('token'))
        if user_info is False:
            return Response({"status": "ERROR", "msg": "token无效,请先登录,如有问题请联系管理员"})
        user = User.objects.get(id=user_info.get('id'))
        try:
            group = user.groups.all().get(id=form_data.get('group'))
        except Group.DoesNotExist:
            return Response({"status": "ERROR", "msg": "您还没有加入该小组，所以不能在该小组中发布文章"})

        article = user.articles.create(
            title=form_data.get('title'),
            content=form_data.get('content'),
            post_man=user,
            group=group,
            is_show=True,
            helped_number=0
        )
        article_serializer = ArticleSerializer(article, many=False)
        return Response({"status": "OK", 'data': article_serializer.data})


'''
find article by id
'''


class GetArticleInfoById(APIView):

    def get(self, request, format=None):
        if request.GET.get('id') is None:
            return Response({"必要字段": "id(文章的id)"})
        else:
            try:
                article = Article.objects.get(id=request.GET.get('id'))
            except Article.DoesNotExist:
                return Response({"status": "ERROR", "msg": "没有对应该id的文章"})
            article_serializer = ArticleSerializer(article, many=False)
            return Response({"status": "OK", "data": article_serializer.data})


'''
find articles by key_word
'''


class GetArticlesByKeyWord(APIView):

    def get(self, request, format=None):
        key_word = request.GET.get('key_word')
        if key_word is None:
            return Response({"必要字段": "key_word(查询的关键字)"})
        articles = Article.objects.filter(content__contains=key_word) | Article.objects.filter(title__contains=key_word)
        articles_serializer = ArticleSerializer(articles, many=True)
        return Response({"status": "OK", "data": articles_serializer.data})
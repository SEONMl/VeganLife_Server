# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from community.models import *
from community.serializers import *


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':  # 200
        articles = Article.objects.all()
        seri = ArticleSerializer(articles, many=True)
        return Response(seri.data, status=200)
    else:  # 200
        reqdata = request.data
        seri = ArticleSerializer(data=reqdata)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=200)
        return Response(seri.errors, status=400)


@api_view(['GET'])
def select_commu(request, code):
    reqdata = request.data
    if request.method == 'GET':
        # 커뮤 코드에 해당하는 글
        selected = Article.objects.filter(community_code=code)
        seri = ArticleSerializer(selected, many=True)
        return Response(seri.data, status=200)

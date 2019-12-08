from rest_framework import viewsets

from magazines.models import Article, Magazine
from magazines.serializers import ArticleSerializer, MagazineSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

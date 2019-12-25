from celery import shared_task
from django.core.files import File

from .models import Article, Magazine
from .magazine import generete_epub


@shared_task
def create_magazine_epub(magazine_key):
    magazine = Magazine.objects.get(_id=magazine_key)
    article_urls = [
        article.url for article in Article.objects.filter(magazine=magazine)]
    magazine_epub_path = generete_epub(
        article_urls, magazine.name, str(magazine._id))
    magazine.ebook.save(f'{magazine._id}.epub', File(
        open(magazine_epub_path, 'rb')))
    magazine.save()
    return {'magazine_id': magazine._id}

import uuid
from django.db import models


class Article(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)


class Magazine(models.Model):
    _id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, db_column='id')

    articles = models.ManyToManyField('magazines.Article')

    name = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)

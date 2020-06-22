from django.db import models


class Acount(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)


class Article(models.Model):
    article_id = models.IntegerField(default=0)
    acount = models.ForeignKey(Acount, on_delete=models.PROTECT,)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    pien = models.IntegerField(default=0)

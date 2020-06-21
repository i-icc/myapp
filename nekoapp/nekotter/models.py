from django.db import models


class Acount(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.ForeignKey("auth.User", on_delete=models.CASCADE,)


class Article(models.Model):
    id = models.IntegerField(default=0)
    user_id = models.ForeignKey(Acount, on_delete=models.PROTECT,)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name

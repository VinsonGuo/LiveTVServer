from django.db import models


# Create your models here.


class Live(models.Model):
    name = models.CharField(max_length=20)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    url = models.TextField()
    category = models.IntegerField(
        default=0,
        choices=[(0, "央视"),
                 (1, "地方"),
                 (2, "港澳"),
                 (3, "台湾"),
                 (4, "国际"),
                 (5, "体育"),
                 (6, "影视"),
                 (7, "少儿"),
                 (8, "新闻")])

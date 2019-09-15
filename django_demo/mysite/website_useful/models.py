from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='类别')


class UrlTools(models.Model):
    title = models.CharField(max_length=100)
    url_link = models.CharField(max_length=100)
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE)

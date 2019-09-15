import datetime
import time

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题')
    pub_date = models.DateTimeField('发布时间')

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='选择问题')
    choice_tex = models.CharField(max_length=200, verbose_name='新增选项')
    votes = models.IntegerField(default=0, verbose_name='票数')

    def __str__(self):
        return self.choice_tex

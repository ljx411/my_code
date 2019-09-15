from django.db import models


# Create your models here.

class Game_5566(models.Model):
    num = models.CharField(max_length=30, verbose_name='ID号')
    game_title = models.CharField(max_length=150, verbose_name='游戏名称')

    def __str__(self):
        return self.game_title

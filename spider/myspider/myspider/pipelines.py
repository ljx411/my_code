# -*- coding: utf-8 -*-
from pymysql import connect


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def __init__(self):
        self.con = connect('localhost', 'root', '123456', 'game')
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        sql = 'insert into new_game5566(game_id, game_title) VALUES ("%s","%s")' % (item['game_id'], item['game_title'])
        self.cur.execute(sql)
        self.con.commit()
        return item

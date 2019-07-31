# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class LimpiarValoresVacios(object):
    def process_item(self, item, spider):
        market_cap = item['market_cap']
        price = item['price']
        supply = item['supply']
        volume = item['volume']
        
        if(('?' in market_cap)or('?' in price)or('?' in supply)or('?' in volume)or('Low Vol' in supply)or('Low Vol' in volume)):
            raise DropItem('No reconoce dato')
        else:
            return item
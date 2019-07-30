# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def limpiar_saltos_lineas(texto):
    return texto.replace('\n','')

def datos_vacios(texto):
    return texto.replace('?','')

class ProyectofinalItem(scrapy.Item):
    
    name = scrapy.Field()
    market_cap = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            datos_vacios
        ),
        output_processor = MapCompose()
    )
    price = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            datos_vacios
        ),
        output_processor = MapCompose()
    )
    pass

class ProyectofinalItem2(scrapy.Item):
    
    supply = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            datos_vacios
        ),
        output_processor = MapCompose()
    )
    volume = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            datos_vacios
        ),
        output_processor = MapCompose()
    )
    pass

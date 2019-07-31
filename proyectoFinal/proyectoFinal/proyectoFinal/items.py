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

def limpiar_signos(texto):
    return texto.replace('$','')

def limpiar_comas(texto):
    return texto.replace(',','')

def convertir_decimales(texto):
    return texto.replace('.',',')

class ProyectofinalItem(scrapy.Item):
    
    name = scrapy.Field()
    market_cap = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            limpiar_signos,
            limpiar_comas
        ),
        output_processor = TakeFirst()
    )
    price = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            limpiar_signos,
            limpiar_comas
        ),
        output_processor = TakeFirst()
    )
    supply = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            limpiar_signos,
            limpiar_comas
        ),
        output_processor = TakeFirst()
    )
    volume = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas,
            limpiar_signos,
            limpiar_comas
        ),
        output_processor = TakeFirst()
    )
    pass

class ProyectofinalItem2(scrapy.Item):
    
    name = scrapy.Field()
    volume24h = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas
        ),
        output_processor = TakeFirst()
    )
    volume7d = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas
        ),
        output_processor = TakeFirst()
    )
    volume30d = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas
        ),
        output_processor = TakeFirst()
    )
    markets = scrapy.Field(
        input_processor = MapCompose(
            limpiar_saltos_lineas
        ),
        output_processor = TakeFirst()
    )
    launched = scrapy.Field()
    pass

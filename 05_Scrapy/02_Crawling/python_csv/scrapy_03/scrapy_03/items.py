# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'
    return texto.replace(cadena_a_reemplazar,url)

def transformar_string_a_float(precio):

    precio = precio[1:] 
    
    return float(precio)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()
    precio = scrapy.Field(
        input_processor = MapCompose(
            transformar_string_a_float
            ),
        output_processor = TakeFirst()
    )
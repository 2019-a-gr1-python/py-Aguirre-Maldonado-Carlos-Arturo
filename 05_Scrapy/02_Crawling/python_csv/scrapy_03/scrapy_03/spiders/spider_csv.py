import scrapy
from scrapy.spiders import CSVFeedSpider

# Spider
# CrawlSpider
# CSVFeedSpider

class VinosArania(CSVFeedSpider):
    name = 'vinos'

    start_urls = [
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    ]
    
    delimiter = ';'

    quotechar = '"'

    headers = [
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'quality'
    ]

    def parse_row(self, response, row):
        print('ph = ',row['pH'])

"""

url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    print('ASDASDAS') 
    return texto.replace(cadena_a_reemplazar,url)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen)
    )
    titulo = scrapy.Field()

from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo', titulo.extract_first())
il.load_item()
"""

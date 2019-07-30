import scrapy
from proyectoFinal.items import ProyectofinalItem2
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose

class AraniaProductosFybeca(scrapy.Spider):
    name = 'proyecto2'

    def start_requests(self):
        urls = [
        'https://coinmarketcap.com/all/views/all/'
        ]

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        tabla = response.css('tbody')
        for registro in tabla:
                          
            registro_loader = ItemLoader(
                    item = ProyectofinalItem2(),
                    selector = registro
            )
            registro_loader.default_output_processor = MapCompose()

            registro_loader.add_css(
                'supply',
                'td.no-wrap.text-right.circulating-supply > span::text'
            )           
            registro_loader.add_css(
                'volume',
                'td:nth-child(7) > a::text'
            )                       
            yield registro_loader.load_item()
            

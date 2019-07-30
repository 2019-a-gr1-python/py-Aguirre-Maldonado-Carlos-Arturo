import scrapy
from proyectoFinal.items import ProyectofinalItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose

class AraniaProductosFybeca(scrapy.Spider):
    name = 'proyecto'

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
                    item = ProyectofinalItem(),
                    selector = registro
                )
            registro_loader.default_output_processor = MapCompose()

            registro_loader.add_css(
                'name',
                'td.no-wrap.currency-name > a::text'
            )

            registro_loader.add_css(
                'market_cap',
                'td.no-wrap.market-cap.text-right::text'
            )
            registro_loader.add_css(
                'price', 
                'td:nth-child(5) > a::text'
            )
                           
            yield registro_loader.load_item()
            

import scrapy
from proyectoFinal.items import ProyectofinalItem2
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.loader.processors import MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

def generarUrls(self, url_inicial):
    url_auxiliar = ''
    grupo_urls = []
    grupo_urls.append(url_inicial)
    n=2

    for url in range(2):
        url_auxiliar = url_inicial+str(n)
        grupo_urls.append(url_auxiliar)
        n=n+1
            
    return grupo_urls

class SpiderCryptoExchange(scrapy.Spider):
    name = 'proyecto2'

    def start_requests(self):
        urls = generarUrls("", 'https://coinmarketcap.com/rankings/exchanges/')

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):

        tabla = response.css('tr')
        tabla = tabla[1:]
        for registro in tabla:
                          
            registro_loader = ItemLoader(
                    item = ProyectofinalItem2(),
                    selector = registro
            )
            registro_loader.default_output_processor = TakeFirst()

            registro_loader.add_css(
                'name',
                'td.no-wrap.currency-name > a::text'
            )           
            registro_loader.add_css(
                'volume24h',
                'td:nth-child(4) > a::text'
            )
            registro_loader.add_css(
                'volume7d',
                'td:nth-child(5) > a::text'
            )
            registro_loader.add_css(
                'volume30d',
                'td:nth-child(6) > a::text'
            )
            registro_loader.add_css(
                'markets',
                'td:nth-child(7) > a::text'
            )  
            registro_loader.add_css(
                'launched',
                'td:nth-child(10)::text'
            )                          
            yield registro_loader.load_item()
            

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_libros' # Heredado (conservar el nombre)
    allowed_domains = [
        'toscrape.com'
    ]
    start_urls = [ # Heredado (conservar el nombre)
        'http://books.toscrape.com/'
    ]
    regla_uno = ( # Heredado (conservar el nombre)
        Rule(LinkExtractor(), callback='parse_page'),
    )

    url_segmento_permitido = (
        'category/books/fiction_10',
        'category/books/fantasy_19'
    )

    #url_segmento_restringido = (
    #    'ar/sections',
    #    'zh/sections',
    #    'ru/sections'
    #)

    regla_dos = ( # Heredado (conservar el nombre)
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmento_permitido
        ), callback='parse_page')
        ,
    )

    regla_tres = ( # Heredado (conservar el nombre)
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmento_permitido,
        #    deny=url_segmento_restringido
        ), callback='parse_page')
        ,
    )

    rules = regla_dos

    def parse_page(self, response):
        lista_programas = response.css('article.product_pod > h3 > a::text').extract()

        for agencia in lista_programas:
            with open('libros_titulos.txt','a+') as archivo:
                archivo.write(agencia + '\n')
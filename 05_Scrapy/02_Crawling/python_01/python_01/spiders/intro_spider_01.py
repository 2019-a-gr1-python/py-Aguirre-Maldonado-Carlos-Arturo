import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedor = response.css('article.product_pod')

        titulos = etiqueta_contenedor.css('h3 > a::attr(title)').extract()

        stocks = etiqueta_contenedor.css('div.product_price > p.instock.availability::text').extract()

        precios = etiqueta_contenedor.css('div.product_price > p.price_color::text').extract()

        resultados_crawl = {
            'titulos': titulos,
            'stocks' : stocks,
            'precios': precios
        }

        #print(titulos)
        #print(stocks)
        #print(precios)

        #print(resultados_crawl)

        print(resultados_crawl['stocks'][1])

        #path = './resultados'
        #archivo_escritura_abierto = open(path,mode='a')
        #archivo_escritura_abierto.write(resultados_crawl['titulos'][0])
        #archivo_escritura_abierto.close()


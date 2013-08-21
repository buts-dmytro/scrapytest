from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapytest.items import ProductItem


class Hit24Spider(CrawlSpider):
    name = "hit24"
    allowed_domains = ["hit24.lviv.ua"]
    start_urls = ["http://hit24.lviv.ua/web/main.php"]

    rules = [
        #Extract only primary categories from main menu
        Rule(SgmlLinkExtractor(allow=("c\.php\?.+",), restrict_xpaths=["//ul[@id='main-menu']/descendant::*"]),
             callback="last_page")
    ]

    '''
    We have category page with 107 products, and each click on
    "more products" button requests next page which appends additional
    100 product to list. So here we, from total product count, calculate
    last page number which gives all products list.
    '''
    def last_page(self, response):
        hxs = HtmlXPathSelector(response)
        # Get total count in string format (123) and next convert to integer
        products_total = hxs.select("//small[@class='prodquan']/text()").extract()[0]
        products_total = int(products_total)
        # We subtract 7 because we have 107 products on first page
        page = (products_total - 7 - 1) / 100 + 1
        request = Request("http://hit24.lviv.ua/web/c.php?id=1&page=" + str(page),
                          callback=self.parse_item)
        return request

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        product_blocks = hxs.select("//ul[@class='prods']/li/div")
        for block in product_blocks:
            item = ProductItem()
            item["name"] = block.select("//b[@itemprop='name']/text()").extract()
            item["price"] = block.select("//span[@itemprop='price']/text()").extract()
            yield item


SPIDER = Hit24Spider()
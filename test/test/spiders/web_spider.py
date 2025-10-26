# spiders/site_crawler.py
from scrapy.spiders import SitemapSpider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request

class SiteCrawler(SitemapSpider):
    name = "web_spider"
    # allowed_domains = ["sltmobitel.lk"]  # set to the target domain
    sitemap_urls = ["https://www.slt.lk/robots.txt"]  # starting point(s)
    # sitemap_rules = [('', 'parse_page')]

    # rules = (
    #     # follow all internal links (you can narrow with allow=(), deny=(), etc.)
    #     Rule(LinkExtractor(allow_domains=allowed_domains, unique=True), follow=True, callback='parse_page'),
    # )

    def parse(self, response):
        # example: extract title and url
        print("--------response-----")
        print(response)
        yield {
            "url": response.url,
            "title": response.xpath("//title/text()").get(),
            # add other fields you want
        }

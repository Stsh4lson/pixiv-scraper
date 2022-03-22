import scrapy
from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider
from pixivScrape.items import PixivscrapeItem
import datetime
import json


class PixivSpider(scrapy.Spider):
    name = 'pixiv'
    
    def start_requests(self):
        start_days = 0
        end_days = 100
        # one day is equivalent of 500 images
        for days_back in range(start_days, end_days+1):
            date_num = datetime.date.today() - datetime.timedelta(days=days_back)
            date_num = str(date_num).replace('-', '')
            for page in range(1, 11):
                url = str(f"https://www.pixiv.net/ranking.php?mode=daily&p={page}&format=json&date={date_num}")
                req = scrapy.Request(url)
                yield req
        
    def parse(self, response):
        text_response = response.body.decode('utf-8')
        json_dict = json.loads(text_response)
        for item in json_dict['contents']:
            url = item['url']
            yield {'image_urls': url, 'sexual': item["illust_content_type"]['sexual']}
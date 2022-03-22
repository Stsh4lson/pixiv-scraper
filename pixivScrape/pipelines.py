# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        
        self.headers = {
            "referer": 'https://www.pixiv.net'
        } 
        
        image_url = item['image_urls'].replace('c/240x480/', '')
        # img_id = image_url.split('/')[-1][:8]
        yield scrapy.Request(image_url,
                             headers=self.headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
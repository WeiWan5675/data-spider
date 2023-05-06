# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DynamicsPipeline():

    def open_spider(self, spider):
        print("打开流水线拉!")
        return None


    def process_item(self, item, spider):
        print("流水线处理item拉!")
        print(item)
        return item
    

    def close_spider(self,spider):
        print('爬虫结束')
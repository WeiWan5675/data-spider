# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DynamicsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pub_time = scrapy.Field
    dynamic_id = scrapy.Field
    dynamic_type = scrapy.Field
    dynamic_pub_platform = scrapy.Field
    dynamic_content = scrapy.Field
    dynamic_url = scrapy.Field
    dynamic_image_url = scrapy.Field
    dynamic_image = scrapy.Field
    dynamic_video_url = scrapy.Field
    dynamic_video_title = scrapy.Field
    dynamic_video_desc = scrapy.Field
    dynamic_tags = scrapy.Field
    dynamic_pub_time = scrapy.Field
    update_time = scrapy.Field
    create_time = scrapy.Field
    pass

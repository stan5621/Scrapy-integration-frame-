# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy


#class SohuitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass

from scrapy.item import Item, Field
class SohuitItem(Item):
    url = Field()           #ç.
    title  = Field()        #?.?
    source = Field()        #?¥æ 
    createtime = Field()    #?.??¶é 
    author   = Field()      #ä.
    abstract = Field()      #?.?
    content = Field()       #正æ    commentnum = Field()    #è.?
    category  = Field()     #?.??.±»
    gettime  = Field()      #?..?¶é
    commentnum = Field()

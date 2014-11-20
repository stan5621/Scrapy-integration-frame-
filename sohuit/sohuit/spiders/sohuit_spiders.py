import time
import os
os.environ["DISPLAY"] = ":2.0"
import re
import json
import gtk
import webkit
import jswebkit
import warnings
warnings.filterwarnings('ignore')

from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor as sle


from sohuit.items import *


class SohuitSpider(CrawlSpider):
    name = "sohuit"
    allowed_domains = ["it.sohu.com"]
#    download_delay = 1
#    download_timeout = 15
    start_urls = [
 #   "http://it.sohu.com/teleguonei_%s.shtml" % d for d in range(1216,1314)
     "http://it.sohu.com/20141116/n406069974.shtml"
     ]


    rules = [

        Rule(sle(allow=("http://it.sohu.com/20[0-1][0-4].*.shtml")), callback='parse_item',follow=True),
#        Rule(sle(allow=("http://it.sohu.com/201[3-4].*.shtml")),callback='parse_item',follow=True),
    ]
   
#    def __init__(self):
#        super(SohuitSpider,self).__init__()
#        self.view = webkit.WebView()
#        self.websettings = self.view.get_property('settings')
#        self.websettings.set_property("auto-load-images", False)
#        self.websettings.set_property("enable-java-applet", False)
#        self.websettings.set_property('enable-plugins', False)
#        self.websettings.set_property('enable-page-cache', False)
       # self.view.connect( 'load-finished', lambda v,f: gtk.main_quit())


    def parse_item(self, response):
        items = []
        sel = Selector(response)
        base_url = get_base_url(response)
      #  print base_url
       
        item = SohuitItem()
        item['url'] = base_url
        if len(sel.css('h1').xpath('text()').extract())==0 :
            item['title'] = None
        else:
            item['title'] = sel.css('h1').xpath('text()').extract()[0]
        
        if  len(sel.css('.source .sc #media_span span').xpath('text()').extract())!=0 :
            item['source'] = sel.css('.source .sc #media_span span').xpath('text()').extract()[0]
        else:
            item['source'] = None
        if  len(sel.css('.time').xpath('text()').extract())!=0:
            item['createtime'] = sel.css('.time').xpath('text()').extract()[0]
        else:
            item['createtime'] = None
        if len(sel.css('.source #author_baidu').xpath('text()').extract())!=0 :
            item['author'] = sel.css('.source #author_baidu').xpath('text()').extract()[0]
        else:
            item['author'] = None
         #      item['author'] = None
        item['abstract'] = None
        if len(sel.xpath('//div[@id="contentText"]//p/text()').extract())!=0:
            contentarr = sel.xpath('//div[@id="contentText"]//p/text()').extract()  
            item['content'] = "".join(contentarr) 
        else:
            item['content'] = None
        if len(sel.xpath('//div[@id="channel-nav"]/div/span/a/text()'))!=0:
            categoryarr = sel.xpath('//div[@id="channel-nav"]/div/span/a/text()').extract()
            item['category'] = "/".join(categoryarr)
        else:
            item['category'] = None
     #   item['commentnum'] = None
     #   item['gettime'] = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        timeStamp = time.time()
        timeArray = time.localtime(timeStamp) 
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        item['gettime'] = otherStyleTime
    #    view = webkit.WebView()
    #    websettings = view.get_property('settings')
    #    websettings.set_property("auto-load-images", False)
    #    websettings.set_property("enable-java-applet", False)
    #    websettings.set_property('enable-plugins', False)
    #    websettings.set_property('enable-page-cache', False)
    #    view.connect( 'load-finished', lambda v,f: gtk.main_quit())
    #    view.load_uri(response.url)
    #    gtk.main()
#        view.execute_script("document.title=document.getElementById('changyan_parti_unit').innerHTML")
#        commentnum =  view.get_main_frame().get_title()
#        item['commentnum'] = commentnum
    #    js = jswebkit.JSContext( view.get_main_frame().get_global_context() )
#        time.sleep(1)
    #    try:
 #           commentnum = js.EvaluateScript("document.getElementById('changyan_parti_unit').innerHTML")

    #        item['commentnum'] = js.EvaluateScript("document.getElementsByClassName('red')[0].innerHTML")
    #    except:
    #        item['commentnum'] = None
       # item['commentnum'] = comme        
      #  selcommentnum = sel.xpath('//span[@class="f12"]/span[@class="red"]/text()')
        if(len(sel.xpath('//span[@class="f12"]/span[@class="red"]/text()'))!=0):
            item['commentnum'] = sel.xpath('//span[@class="f12"]/span[@class="red"]/text()')[0].extract()
        else:
            item['commentnum'] = None

        items.append(item)
        #print items
       # print item
   #     print items
        return items
       # open("test1","a").write(item+"\n")
        #item['source'] = response.xpath('//span[@class="source"]//span//span//span//text()')

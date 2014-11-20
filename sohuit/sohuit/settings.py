# -*- coding: utf-8 -*-

# Scrapy settings for sohuit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sohuit'

SPIDER_MODULES = ['sohuit.spiders']
NEWSPIDER_MODULE = 'sohuit.spiders'
DUPEFILTER_CLASS = 'sohuit.duplicate_filter.CustomFilter'


ITEM_PIPELINES = {
    'sohuit.pipelines.JsonWithEncodingPipeline': 200,
}
#SPIDER_MIDDLEWARES = {
#    'sohuit.spidermiddlewares.CustomSpiderMiddleware': 100,   #è.?..ä.件�?è.ä.ç}
#}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sohuit (+http://www.yourdomain.com)'
#import os
#os.environ["DISPLAY"] = ":2.0"
#CONCURRENT_REQUESTS = 100
COOKIES_ENABLED = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False
#DOWNLOAD_TIMEOUT = 15
#DOWNLOAD_DELAY = 20
LOG_LEVEL = 'INFO'
#AJAXCRAWL_ENABLED = True
DOWNLOADER_MIDDLEWARES = {
     'sohuit.downloadtimeout.DownloadTimeoutMiddleware': 1,
    'sohuit.downloadmiddlewares.WebkitDownloader': 10,
}
#DOWNLOAD_HANDLERS = {
#    'http': 'sohuit.dhandler.WebkitDownloadHandler',
#    'https': 'sohuit.dhandler.WebkitDownloadHandler',
#}




#DOWNLOADER_MIDDLEWARES_BASE = {
    # Engine side
#    'sohuit.downloadtimeout.DownloadTimeoutMiddleware': 350,
    # Downloader side
#}

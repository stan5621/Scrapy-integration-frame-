from scrapy import signals


class DownloadTimeoutMiddleware(object):

    def __init__(self, timeout=15):
        self._timeout = timeout

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings['DOWNLOAD_TIMEOUT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        self._timeout = getattr(spider, 'download_timeout', self._timeout)

    def process_request(self, request, spider):
        if self._timeout:
            print self._timeout,"huangfeng"
            request.meta.setdefault('download_timeout', self._timeout)

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals,log
from scrapy.xlib.pydispatch import dispatcher
from scrapy.http import Request
from scrapy.item import BaseItem
from scrapy.utils.request import request_fingerprint
import socket
import errno

class CustomSpiderMiddleware(object):
    def process_spider_output(self,response,result,spider):
        ret = []
        for x in result:
            if isinstance(x, Request):
                if not check_url(x.url):
                    ret.append(x)
            elif isinstance(x, BaseItem):
                ret.append(x)
        return ret;

	def check_url(self, url):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('10.210.90.74',8000))
			sock.send(url)
			rec = sock.recv(1)
			if rec == 't':
				return True
			else:
				return False
			sock.close()
		except:
			sock.close()
			return False
#		except socket.error, e:
#			if isinstance(e.args, tuple):
#                if e[0] == errno.EPIPE:
#                    sock.close()			

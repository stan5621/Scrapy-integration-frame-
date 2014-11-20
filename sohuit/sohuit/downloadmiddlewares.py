import os
os.environ["DISPLAY"] = ":2.0"
#import settings
from scrapy.http import HtmlResponse 
from scrapy.contrib.linkextractors import LinkExtractor as sle
import sys 
import gtk 
import webkit 
import jswebkit 
 
 
class WebkitDownloader( object ): 
 
  #   def __init__(self):
  #       self.g= gtk.Window(gtk.WINDOW_TOPLEVEL)
  #       self.g.move(0, 0)
  #       self.g.resize(gtk.gdk.screen_width()-200, gtk.gdk.screen_height()-200) 
     def stop_gtk(self):
         gtk.main_quit()
#         print "huangfeng56217899"
#         sys.exit(0)
 
 
     def _get_webview(self): 
         webview = webkit.WebView() 
         props = webview.get_settings() 
         props.set_property('enable-java-applet', False) 
         props.set_property('enable-plugins', False) 
         props.set_property('enable-page-cache', False)
         props.set_property("auto-load-images", False) 
         return webview 
 
 
     def process_request( self, request, spider ): 
#         if 'renderjs' in request.meta:
         webview = self._get_webview() 
        # subwindow = gtk.ScrolledWindow() 
        # subwindow.add(webview) 
         webview.load_uri(request.url)
         webview.connect('load-finished', self.load_finished)
         webview.connect('document-load-finished', self.document_load_finished)
         webview.connect('console-message', self.console_message) 
        # self.g.add(subwindow)
         gtk.main() 
         #gtk.main_quit()
         ctx = jswebkit.JSContext(webview.get_main_frame().get_global_context()) 
         url = ctx.EvaluateScript('window.location.href') 
         html = ctx.EvaluateScript('document.documentElement.innerHTML')
         #open("html1.html","wb").write(html)
         #commentnum=sel.xpath('//span[@id="changyan_parti_unit"]/text').extract() 
         #print commentnum
        # print "huangfeng1"
        # body=html.encode('utf-8')
        # print body
        # print  HtmlResponse(url, encoding='utf-8', body=html.encode('utf-8'))
        # print "huangfeng2"
#         print html
         return  HtmlResponse(url, encoding='utf-8', body=html.encode('utf-8')) 
         #return HtmlResponse(url,body=str(html))
     def load_finished(self, webview, webframe):
         print >> sys.stderr, "finished"
         self.stop_gtk()
     def document_load_finished(self, webview, webframe): 
         """ in case that page is not fully loaded, we set a timeout """
         script = """ 
 function timeout() { 
     clearTimeout(timeoutID); 
     throw('<!-- timeout -->'); 
 } 
 var timeoutID=setTimeout("timeout()", 15000); 
         """ 
         webview.execute_script(script) 
     
     def console_message(self, webview, msg, line, sourceid): 
         content = msg 
         if content.startswith('<!-- timeout -->'): 
             print >> sys.stderr, 'timeout'
             self.stop_gtk()
         return True 



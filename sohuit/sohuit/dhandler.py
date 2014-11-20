#import settings
import sys
import gtk 
import webkit 
import jswebkit 
from twisted.internet import defer 
 
 
from scrapy.core.downloader.handlers.http import HttpDownloadHandler 
from scrapy.http import HtmlResponse 
from scrapy import log 
 
 
#gtk.gdk.threads_init() 
 
 
class WebkitDownloadHandler(HttpDownloadHandler): 
     def stop_gtk(self):
         gtk.main_quit()
    
     def download_request(self, request, spider): 
  #        if 'renderjs' in request.meta: 
       #  while True:
             self.d = defer.Deferred() 
             self.d.addErrback(log.err, spider=spider) 
             webview = self._get_webview() 
             webview.connect('load-finished', self.load_finished)
             webview.connect('document-load-finished', self.document_load_finished)
             webview.connect('console-message',self.console_message) 
          #    win = gtk.Window() 
          #    win.add(webview) 
          #    win.show_all() 
          #    print "hu2"
             webview.open(request.url)
          #    webview.load_uri(request.url)
             gtk.main()
             # gtk.main()
        #     break
             return self.d 
  #        else: 
  #            return super(WebkitDownloadHandler, self).download_request(request, spider) 
 
 
     def _get_webview(self): 
         webview = webkit.WebView() 
         props = webview.get_settings() 
         props.set_property('enable-java-applet', False) 
         props.set_property('enable-plugins', False) 
         props.set_property('enable-page-cache', False) 
         #props.set_property('enable-frame-flattening', True) 
         return webview 
  
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
 
     def load_finished(self, view, frame): 
       #  if frame != view.get_main_frame(): 
       #      return
       #  ctx = jswebkit.JSContext(frame.get_global_context())
         ctx = jswebkit.JSContext(view.get_main_frame().get_global_context()) 
         url = ctx.EvaluateScript('window.location.href') 
         html = ctx.EvaluateScript('document.documentElement.innerHTML') 
         response = HtmlResponse(url, encoding='utf-8', body=html.encode('utf-8'))
         print "finished"
         self.stop_gtk()
         self.d.callback(response) 
 
 


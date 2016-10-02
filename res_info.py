# -*- coding: cp936 -*-
#urllib2.urlopen()后的对象的3个方法：geturl(),info(),getcode()之前有个read()方法
#后者返回对象的字典对象，该字典描述了获取的页面情况.通常是headers
from urllib2 import Request,urlopen,URLError,HTTPError
old_url='http://www.baidu.com'
req=Request(old_url)
res=urlopen(req)
print 'Info():'  
print res.info()
#res.getcode(),return the HTTP status code of the response

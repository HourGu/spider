# -*- coding: cp936 -*-
import urllib2
enable_proxy=True
proxy_handler=urllib2.ProxyHandler ({'http':'27.122.12.45:3128'})#代理ip从网上找，http://www.youdaili.net/
null_proxy_handler=urllib2.ProxyHandler({})
if enable_proxy:
    opener=urllib2.build_opener (proxy_handler)
else:
    opener=urllib2.build_opener(null_proxy_handler)
#urllib2.install_opener(opener)

req=urllib2.Request('http://www.baidu.com')
res=opener.open(req)
html=res.read()
print html

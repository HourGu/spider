# -*- coding: cp936 -*-
#url_error调取错误信息的reason属性：错误号+错误信息
import urllib2
req=urllib2.Request('http://www.baibai.com')

try:
    urllib2.urlopen(req)

except urllib2.URLError,e:
    print e.reason
    

"""
>>> ================================ RESTART ================================
>>> 
[Errno 11002] getaddrinfo failed
"""

# -*- coding: cp936 -*-
#url_error��ȡ������Ϣ��reason���ԣ������+������Ϣ
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

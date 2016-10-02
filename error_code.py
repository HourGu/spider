# -*- coding: cp936 -*-
#得到错误码
import urllib2
try:
    res=urllib2.urlopen ('http://bbs.csdn.net/why')
except urllib2.HTTPError,e:
    print e.code
'''
>>> 
403
>>> 
'''

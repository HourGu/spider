# -*- coding: cp936 -*-
#�õ�������
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

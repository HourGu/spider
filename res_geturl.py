# -*- coding: cp936 -*-
#urllib2.urlopen()后的对象的两个方法：geturl(),info(),之前有个read()方法
#前者得到重定向后的链接
from urllib2 import Request,urlopen,URLError,HTTPError
old_url='http://rrurl.cn/b1uZuP'
req=Request(old_url)
res=urlopen(req)
print 'Old url:'+old_url
print 'Real url'+res.geturl()

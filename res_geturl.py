# -*- coding: cp936 -*-
#urllib2.urlopen()��Ķ��������������geturl(),info(),֮ǰ�и�read()����
#ǰ�ߵõ��ض���������
from urllib2 import Request,urlopen,URLError,HTTPError
old_url='http://rrurl.cn/b1uZuP'
req=Request(old_url)
res=urlopen(req)
print 'Old url:'+old_url
print 'Real url'+res.geturl()

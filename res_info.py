# -*- coding: cp936 -*-
#urllib2.urlopen()��Ķ����3��������geturl(),info(),getcode()֮ǰ�и�read()����
#���߷��ض�����ֵ���󣬸��ֵ������˻�ȡ��ҳ�����.ͨ����headers
from urllib2 import Request,urlopen,URLError,HTTPError
old_url='http://www.baidu.com'
req=Request(old_url)
res=urlopen(req)
print 'Info():'  
print res.info()
#res.getcode(),return the HTTP status code of the response

# -*- coding: cp936 -*-
import urllib#����
import urllib2#get

url='http://www.someserver.com/register.cgi'

values={'name':'WHY',
        'location':'SDU',
        'language':'Python'}

data=urllib.urlencode(values)  #���빤��
req=urllib2.Request(url,data)  #��������ͬʱ��data��
response=urllib2.urlopen(req)  #���ܷ�������Ϣ
the_page=response.read()  #��ȡ��������Ϣ


##��header
import urllib  
import urllib2  

url = 'http://www.someserver.com/cgi-bin/register.cgi'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
values = {'name' : 'WHY',  
          'location' : 'SDU',  
          'language' : 'Python' }  

headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
req = urllib2.Request(url, data, headers)  
response = urllib2.urlopen(req)  
the_page= response.read()

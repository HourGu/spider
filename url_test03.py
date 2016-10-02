# -*- coding: cp936 -*-
import urllib#编码
import urllib2#get

url='http://www.someserver.com/register.cgi'

values={'name':'WHY',
        'location':'SDU',
        'language':'Python'}

data=urllib.urlencode(values)  #编码工作
req=urllib2.Request(url,data)  #发送请求同时传data表单
response=urllib2.urlopen(req)  #接受反馈的信息
the_page=response.read()  #读取反馈的信息


##含header
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

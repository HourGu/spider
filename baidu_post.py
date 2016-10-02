# -*- coding: utf-8 -*-
#还是没懂
import urllib
import urllib2
postdata=urllib.urlencode({
    'username':'saber丶丶酱',
    'password':'927192718gkf',
    'continueURI':'http://www.verycd.com/',#随便写
    'fk':'',
    'login_submit':'登录'
})
req = urllib2.Request(
    url = 'http://www.baidu.com/signin',
    data = postdata
)
result = urllib2.urlopen(req)
print result.read() 



import urllib2
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

"""
Name = BAIDUID
Value = 4AEA7BB96DB1C909371C63335E52D516:FG=1
Name = BIDUPSID
Value = 4AEA7BB96DB1C909371C63335E52D516
Name = H_PS_PSSID
Value = 1431_20972_12896_17944_21087_21188_21190_21161_20928
Name = PSTM
Value = 1474544861
Name = BDSVRTM
Value = 0
Name = BD_HOME
Value = 0
>>> 
"""

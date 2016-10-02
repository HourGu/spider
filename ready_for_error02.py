#ready for url error 01. http_error belongs to url_error,putting ahead.
from urllib2 import Request,urlopen,URLError,HTTPError

req=Request('http://bbs.csdn.net/callmewhy')

try:
    res=urlopen(req)


except URLError,e:
    if hasattr(e,'code'):
        print 'The server could not fulfill the request.'
        print 'Error code:',e.code
    elif hasattr(e,'reason'):
        print 'we failed to reach a server.'
        print 'reason:',e.reason

else:
    print 'No exception was raised.'
    #everything is fine
    

"""
>>> 
The server could not fulfill the request.
Error code: 403
>>> 
"""

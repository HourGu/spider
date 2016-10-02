#ready for url error 01. http_error belongs to url_error,putting ahead.
from urllib2 import Request,urlopen,URLError,HTTPError

req=Request('http://bbs.csdn.net/callmewhy')

try:
    res=urlopen(req)

except HTTPError,e:
    print 'The server could not fulfill the request.'
    print 'Error code:',e.code

except URLError,e:
    print 'we failed to reach a server.'
    print 'reason:',e.reason

else:
    print 'No exception was raised.'
    #everything is fine
    

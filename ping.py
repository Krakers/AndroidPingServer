import httplib
import time

httpServ = httplib.HTTPConnection("localhost", 8080)
httpServ.connect()

timeBeforeRequest = time.time()
httpServ.request('GET', "/")

response = httpServ.getresponse()
if response.status == httplib.OK:
    print "Output from request"
    print response.read()
    print time.time() - timeBeforeRequest
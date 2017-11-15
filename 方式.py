import urllib
import urllib2
 
values={}
values['username'] = "1242826034@qq.com"
values['password']="1976647h@tfz"
data = urllib.urlencode(values) 
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

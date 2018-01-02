# -*- coding:utf-8 -*-
import urllib
import urllib2
 
 
page = 1
url = 'http://search.51job.com/list/070400,000000,0000,00,9,99,web%25E5%2589%258D%25E7%25AB%25AF,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=' + str(page)
user_agent = 'Mozilla/4.0 (compatible: MSIE 5.5: Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

# -*- coding: utf-8 -*-
import urllib
import urllib2
import re


url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=5006000&sj=299&jl=%E5%8C%97%E4%BA%AC&sb=1&sm=0&p=1&isfilter=0&fl=530&isadv=0'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

        
content_pattern = re.compile('<a style=".*?" par=".*?" href=".*?" target="_blank">(.*?)</a>', re.S)
content_list = re.findall(content_pattern, html)


content_pattern1 = re.compile('<td class="zwyx">(.*?)</td>', re.S)
content_list1 = re.findall(content_pattern1, html)

content_pattern2 = re.compile('<td class="gzdd">(.*?)</td>', re.S)
content_list2 = re.findall(content_pattern2, html)

f = 0
for item in content_list:
    print "\n"
    print f+1
    print item
    for i in range(0,1):
        print content_list1[f]
        for i in range(0,1):
            print content_list2[f]
    f = f + 1

    input = raw_input()                                           
    if input == "e":       
        break
    print "-----------------------------The next : -------------------------- \n"

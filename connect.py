#!/usr/bin/python2.6
# coding=utf-8
import re
import urllib
import time
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

username='wanggaofei0325'
password='187962Aa'

headers = {
	'Host':'202.207.240.67:801',
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/45.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Referer':'http://202.207.240.67/a70.htm',
	'Connection': 'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	
        }
posturl='http://202.207.240.67:801/eportal/?c=ACSetting&a=Login&wlanuserip=null&wlanacip=null&wlanacname=null&port=&iTermType=1&mac=123456789012&ip=000.000.000.000&redirect=null'
body = {'DDDDD':username,'upass':password}
data = urllib.urlencode(body)   


type = sys.getfilesystemencoding()
str1='登录成功！'
str2='登录失败！'
str3='账号:'




request = urllib2.Request(posturl,data,headers)

try:

    response = urllib2.urlopen(request)
    print  '---------------------------------------'
    print  '---------------------------------------'

except  urllib2.HTTPError, e:

     print e.code


f= response.read()
unicodePage = f.decode('gb2312')

msg = re.findall('<title>(.*?)</title>', unicodePage)[0]
if  msg.encode('utf-8')== '登录成功':
	print str3,username,     str1
else:
	print str3,username,     str2
                

print  '---------------------------------------'

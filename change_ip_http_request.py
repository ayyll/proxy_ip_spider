# -*- coding=utf-8 -*-
from bs4 import BeautifulSoup
from lxml import etree
import requests
import sys
import bs4
import socket
import urllib
import os
# 检查url地址


def check_link(url):
    User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    header = {}
    header['User-Agent'] = User_Agent
    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！！！')


# 爬取资源
def get_contents(ulist, rurl):
    soup = BeautifulSoup(rurl, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
            # print td.string
        ulist.append(ui)

# 保存资源


def save_contents(urlist, proxy):
    for i in range(1, len(urlist)):
        proxy.append(urlist[i][11] + "://" + urlist[i][3] + ":" + urlist[i][5])
'''''
验证获得的代理IP地址是否可用
'''


def validateIp(proxy):
    url = "http://dddcc2.com/intr/c13a4715b1dfe3c1"
    socket.setdefaulttimeout(3)
    for i in range(0, len(proxy)):
	    try:
	    	if proxy[i][4] == 'S':
	    		proxy_temp = {"https": proxy[i]}
	    	else:
	    		proxy_temp = {"http": proxy[i]}
	        # params = {"bs":"study2017","vipid":"15157436","come_url":""}
	        # params = urllib.urlencode(params)
	        res = urllib.urlopen(url, proxies=proxy_temp).read()
	        print proxy[i]
	    except Exception, e:
	        print "The IP Address is Useless"


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    urli = []
    proxy = []
    url = "http://www.xicidaili.com/nn/1"
    rs = check_link(url)
    get_contents(urli, rs)
    save_contents(urli, proxy)
    validateIp(proxy)

main()
'''
import urllib2
import requests
from lxml import etree
 
proxy = {"http":"http://119.164.181.239:8118"}
test_url="http://aaaoo9.com/intr/c13a4715b1dfe3c1"   #ip网站测试 http://ip.filefab.com/index.php
resp=urllib2.urlopen(test_url).read()
response = etree.HTML(resp)
ip_addr = response.xpath('//div/h1[@id="ipd"]/span/text()')
print "Before switching the IP address:",ip_addr
# 使用代理IP地址之前的访问IP地址
try:
    response = requests.get(test_url)
    response = etree.HTML(resp)
    ip_addr = response.xpath('//div/h1[@id="ipd"]/span/text()')
    print response.text
    print "Now the IP ADDRESS IS:",ip_addr
    # 使用代理IP地址之后的访问IP地址
except Exception:
    print "The IP Address is Useless" #代理IP不可用

'''

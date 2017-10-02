# proxy_ip_spider
一个爬取网页上可用的代理ip的python爬虫。

几点说明：

1.爬虫用的是BeautifulSoup库，简洁小巧，其实用的字段不多，自己正则去一点一点截也可以。

2.模拟http请求用到了urllib以及requests，后者功能相对多一点，但是都差不多，其中一者即可满足本文需求。

3.还有一个问题就是爬取中文资源显示乱码的问题，可以导入sys，然后：

```
reload(sys)
sys.setdefaultencoding('utf8')
```

即可解决中文乱码问题。
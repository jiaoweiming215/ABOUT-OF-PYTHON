网络爬虫是一种自动化程序，搜索引擎技术里大量使用爬虫，爬下整个互联网的内容，存储在数据库里，做索引

爬虫思路
    每个网页都是一份HTML文档，是一种文本标记语言，规则如下：
<html>
    <head>
        <title>首页</title>
    </head>
    <body>
        <h1>我是标题</h1>
        <img src="xxx">
    </body>
</html>    

打开一个网页，即通过HTTP协议，对资源进行请求，我们可以模拟浏览器，发送一份请求，获得这份文档，再抽取我们需要的内容就好。

python语言做爬虫是因为python的网络库非常多，简单python如下：
import urllib2
response=urllib.urlopen("http://xxx.com")
print response.read()

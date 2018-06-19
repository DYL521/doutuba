#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """

import urllib
import urllib.request

## 方法二： 构造request-- 伪造浏览器的请求头发出请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept-Encoding': '' ## 没有压缩的
    }
url = 'http://www.qq.com/'
requset = urllib.request.Request(url=url, headers=headers)

respose = urllib.request.urlopen(requset)

print(respose.read().decode('gbk'))

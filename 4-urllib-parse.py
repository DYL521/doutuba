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
import urllib.parse
import urllib.request

url = 'https://www.baidu.com/s?wd=大傻子'

key = input('请输入查询的关键字：')

k = urllib.parse.unquote(key)
print(k)
url = 'https://www.baidu.com/s?wd=%s' % k

repose = urllib.request.urlopen(url=url)
print(repose.read().decode('utf-8'))

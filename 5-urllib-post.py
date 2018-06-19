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
import urllib.parse
import json
url = 'http://fanyi.baidu.com/sug'

key = input('请输入翻译的汉字：')

# k = urllib.parse.quote(key)
params = {'kw':key} ##  请求体字典
print(params)
params = urllib.parse.urlencode(params).encode('utf-8')
print(params)
response =  urllib.request.urlopen(url=url,data=params)

content = response.read().decode('utf-8')
content_ = json.loads(content)   ## 百度返回的是json，所以直接loads
print(content_)
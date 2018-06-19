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

## 方法1： 这个User-agent 是 Python-urllib/3.6
url = 'http://www.baidu.com/'
repose = urllib.request.urlopen(url=url)

content = repose.read().decode('utf-8')
print(content)

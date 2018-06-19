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
import urllib.response

## 下载图片
url = 'http://img1.gtimg.com/view/pics/hv1/64/219/2277/148117834.jpg'
## 下载视频
url_video = 'http://vf1.mtime.cn/Video/2015/03/20/mp4/150320094140850937_480.mp4'
urllib.request.urlretrieve(url=url_video, filename='.video.mp4')

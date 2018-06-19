#!/usr/bin/env python3  
# -*- coding: utf-8 -*-  
"""  
 @desc:  
 @author: DYL  
 @contact: chng547835@163.com  
 @site: www.xxxx.com  
 @software: PyCharm  @since:python 3.5.2 on 2016/11/3.10:49  
 """

import requests  # 请求网页
import time
from lxml import etree  # 解析网页

from urllib import request  # 下载内容

import os  # 系统包


def parse_page(url):
    # 2.1简单的反爬虫机制
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    # 2.2获取服务器响应
    # 获取请求响应的状态码
    response = requests.get(url, headers=HEADERS)
    # 2.3 从响应里提取出网页
    # 获取整个网页
    text = response.text
    # 将抓取的网页作为参数返回
    return text

## 解析数据
def page_list(text):

    html_tree = etree.HTML(text.encode('utf-8'))
    # image_list = html_tree.xpath('//div[@class="page-content text-center"/div[@class="col-xs-6 col-sm-3"]/img"]')
    image_list = html_tree.xpath('//div[@class="page-content text-center"]//a[@class="col-xs-6 col-sm-3"]/img')
    print(image_list)

    return image_list
def main():
    # 根据URL的规则对URL进行循环，获取多页URL，并传给parse_page()进行抓取数据
    for x in range(1, 1890):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        # 调用parse_page()函数并把url给进去
        text = parse_page(url)
        # print(text)
        # 接收parse_page()返回的网页，并传给page_list()函数进行解析
        imgs = page_list(text)
        # 3.3 对列表里的img对象进行提取
        for img in imgs:
            # try.... except    对程序进行异常处理，避免因为其他原因报错
            try:
                # 3.4获取所有表情的URL并保存在列表里
                imgurl = img.xpath(".//@data-original")
                # 3.5从列表里提取出表情的URL，至于为啥不取零，列表中有空值，取零报错
                for img_url in imgurl:
                    print('img_url = ',img_url)
                    # 分割后缀名：.jpg .png
                    # 3.6对表情的URL进行处理，提取出表情图片的格式，用于组成表情的名字
                    suffix = os.path.splitext(img_url)[1]
                    print('img_url = ', img_url)
                    suffix = suffix.split("!")[0]

                    # 3.7获取表情的名字
                    alt = img.xpath(".//@alt")[0]
                    # alt = re.sub(r'[，。？?,/\\·]','',alt)  #利用正则表达式对表情名字中存在的特殊字符进行处理
                    # 3.8用 alt+suffix组成表情的新名字
                    img_name = alt + suffix
                    time.sleep(1)
                    # 使用request.urlretrieve()对表情进行下载并保存在images文件里
                    # Python学习交流群：125240963，群内每天分享干货，欢迎各位小伙伴入群学习交流
                    request.urlretrieve(img_url, 'images/' + img_name)

                    # 打印出那些表情已经下载
                    print(img_name + '下载完毕！')

            except:
                print("表情报错")

        # 执行函数
if __name__ == '__main__':
    main()

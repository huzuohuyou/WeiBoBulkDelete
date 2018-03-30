__author__ = 'jishu12'
# coding:utf-8
import urllib
import http.cookiejar
import ssl
import requests
from bs4 import BeautifulSoup
import re
import codecs
import http.client
import datetime
import pickle
import os
import smtplib
import json 
'''
作者：吴海龙
OSC乱弹抢沙发
1.使用fiddler进行数据抓包获取header及cookie信息
2.使用python urllib https进行发送数据
'''

flag = False
id=None

def getmid(month):
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://weibo.com/p/1005053880709275/home?is_all=1&stat_date={month}&pids=Pl_Official_MyProfileFeed__20&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fp%2F1005053880709275%2Fhome%3Fis_all%3D1%26stat_date%3D201610%23feedtop&_t=FM_1522374871880272".format(month=month)
    postdata = urllib.parse.urlencode({
    }).encode('utf-8')
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"Origin": "https://my.oschina.net",
        #"X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://my.oschina.net/xxiaobian/blog/844061?p=3&temp=1487827633938",
        #"Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Referer":" https://weibo.com/p/1005053880709275/home?is_all=1&stat_date=201612",
        "Cookie": "UM_distinctid=15fc3c760bf71a-09a16f48df39cf-36624308-100200-15fc3c760c0782; SINAGLOBAL=2556702681594.6157.1510818144875; _s_tentry=news.ifeng.com; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; YF-Page-G0=fc0a6021b784ae1aaff2d0aa4c9d1f17; Apache=6290608352001.947.1522374372862; ULV=1522374373094:17:4:1:6290608352001.947.1522374372862:1520214623438; login_sid_t=ac9efaba7b4a71f433e26007d4893ccc; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; SSOLoginState=1522374633; SUB=_2A253ueeuDeRhGeVG41IW8CfOzDmIHXVUz15mrDV8PUNbmtBeLUPxkW9NT5mR9lZeA2JM0ohmGmF6viqb4YXQwBpl; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWw0GpizVuA7x8rMnw3RmZJ5JpX5KzhUgL.FoeR1h5Neh.ES0-2dJLoIEXLxKqL1h.L1KzLxKnLBK2LBKeLxK-LBKMLBK-LxKML1hnLBoMLxK-L1K-L122t; SUHB=02MvYHrFaQYvsK; ALF=1553910653; wvr=6; UOR=news.ifeng.com,widget.weibo.com,login.sina.com.cn; cross_origin_proto=SSL"
    }
    req = urllib.request.Request(url, postdata, header)
    html=urllib.request.urlopen(req).read()
    mids =re.findall('((?<=\\\"mid=).+?(?=\\\\\"|&))',str(html))
    for mid in mids:
        print(month+delmid(mid))
        
    
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    return r.read()



def delmid(mid):
    if '\\' in mid:
        return ""
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://weibo.com/aj/mblog/del?ajwvr=6 "
    postdata = urllib.parse.urlencode({
        "mid":mid
    }).encode('utf-8')
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"Origin": "https://my.oschina.net",
        #"X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "https://my.oschina.net/xxiaobian/blog/844061?p=3&temp=1487827633938",
        #"Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Referer":" https://weibo.com/p/1005053880709275/home?is_all=1&stat_date=201612",
        "Cookie": "UM_distinctid=15fc3c760bf71a-09a16f48df39cf-36624308-100200-15fc3c760c0782; SINAGLOBAL=2556702681594.6157.1510818144875; _s_tentry=news.ifeng.com; YF-V5-G0=46bd339a785d24c3e8d7cfb275d14258; YF-Page-G0=fc0a6021b784ae1aaff2d0aa4c9d1f17; Apache=6290608352001.947.1522374372862; ULV=1522374373094:17:4:1:6290608352001.947.1522374372862:1520214623438; login_sid_t=ac9efaba7b4a71f433e26007d4893ccc; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; SSOLoginState=1522374633; SUB=_2A253ueeuDeRhGeVG41IW8CfOzDmIHXVUz15mrDV8PUNbmtBeLUPxkW9NT5mR9lZeA2JM0ohmGmF6viqb4YXQwBpl; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWw0GpizVuA7x8rMnw3RmZJ5JpX5KzhUgL.FoeR1h5Neh.ES0-2dJLoIEXLxKqL1h.L1KzLxKnLBK2LBKeLxK-LBKMLBK-LxKML1hnLBoMLxK-L1K-L122t; SUHB=02MvYHrFaQYvsK; ALF=1553910653; wvr=6; UOR=news.ifeng.com,widget.weibo.com,login.sina.com.cn; cross_origin_proto=SSL"
    }
    req = urllib.request.Request(url, postdata, header)
    #html=urllib.request.urlopen(req).read()
    #print(str(html))
    #print(re.findall('((?<=\\\"mid=).+?(?=\\\\\"|&))',str(html)))
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    
    result=r.read().decode('utf-8')
    obj= json.loads(result)
    if obj['code']=="100000":
        print('{mid}删除成功；'.format(mid=mid))
    else:
        print("{mid}错误，删除失败；".format(mid=mid))
    return ""


if __name__ == '__main__':
    date=['201312'\
    '201402','201404','201411',\
    '201502','201503','201504','201505','201506','201506','201507',\
    '201606','201608','201609','201611','201612',\
    '201701','201702']
   
    for month in date:
        getmid(month)
    #getmid(2016,12)
    #print(delmid('4025481420584049\\'))
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:32:40 2020

@author: Zhenlin
"""

from bs4 import BeautifulSoup
import urllib.request
import xml.etree.ElementTree as ET
import configparser
from datetime import timedelta, date
import time
import urllib.parse
import socket
from socket import timeout

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
#values = {'name': 'Michael Foord',
#          'location': 'Northampton',
#          'language': 'Python' }
#data = urllib.parse.urlencode(values)
#data = data.encode('ascii')

keyword='编辑'


def get_one_page_news(page_url):
#    page_url='http://www.chinanews.com/scroll-news/2019/0801/news.shtml'
    root='http://www.chinanews.com'
    req = urllib.request.Request(page_url, headers = headers)
    
    try:
        response = urllib.request.urlopen(req, timeout=10)
        html = response.read()
    except socket.timeout as err:
        print('socket.timeout')
        print(err)
        return []
    except Exception as e:
        print("-----%s:%s %s-----"%(type(e),e.reason, page_url))
        return []
    
    soup = BeautifulSoup(html,"html.parser") # http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
    
    news_pool = []
    news_list = soup.find('div', class_ = "content_list")
    items = news_list.find_all('li')
    for i,item in enumerate(items):
#        print('%d/%d'%(i,len(items)))
        if len(item) == 0:
            continue
        
        a = item.find('div', class_ = "dd_bt").find('a')
        title = a.string
        url = a.get('href')
        if root in url:
            url=url[len(root):]
        
        category = ''
        try:
            category = item.find('div', class_ = "dd_lm").find('a').string
        except Exception as e:
            continue
        
        if category == '图片':
            continue
        
        year = url.split('/')[-3]
        date_time = item.find('div', class_ = "dd_time").string
        date_time = '%s-%s:00'%(year, date_time)
        
        news_info = [date_time, "http://www.chinanews.com"+url, title]
        news_pool.append(news_info)
    return news_pool

def get_news_pool(start_date, end_date):
    news_pool=[]
    delta = timedelta(days=1)
    while start_date <= end_date:
        date_str=start_date.strftime("%Y/%m%d")
        page_url='http://www.chinanews.com/scroll-news/%s/news.shtml'%(date_str)
        print('Extracting news urls at %s'%date_str)
        news_pool += get_one_page_news(page_url)
#        print('done')
        start_date += delta
    return news_pool

def crawl_news(news_pool, min_body_len, doc_dir_path, doc_encoding):
    i = 1
    for n, news in enumerate(news_pool):
        print('%d/%d'%(n,len(news_pool)))
        
        req = urllib.request.Request(news[1], headers = headers)
        try:
            response = urllib.request.urlopen(req, timeout=10)
            html = response.read()
#            response = urllib.request.urlopen(news[1])
        except socket.timeout as err:
            print('socket.timeout')
            print(err)
            print("Sleeping for 10 minute")
            time.sleep(600)
            continue
        except Exception as e:
            print("--1---%s:%s %s-----"%(type(e),e.reason, news[1]))
            print("Sleeping for 10 minute")
            time.sleep(600)
            continue
        
        soup = BeautifulSoup(html, "html.parser") # http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
        [s.extract() for s in soup('script')]
        
        try:
            ps = soup.find('div', class_ = "left_zw").find_all('p')
        except Exception as e:
            print("--2---%s: %s-----"%(type(e), news[1]))
            print("Sleeping for 10 minute")
            time.sleep(600)
            continue
        
        body = ''
        for p in ps:
            cur = p.get_text().strip()
            if cur == '':
                continue
            body += '\t' + cur + '\n'
        body = body.replace(" ", "")
        
        if keyword not in body: # 过滤掉乱码新闻
            continue
        
        if len(body) <= min_body_len:
            continue
        
        doc = ET.Element("doc")
        ET.SubElement(doc, "id").text = "%d"%(i)
        ET.SubElement(doc, "url").text = news[1]
        ET.SubElement(doc, "title").text = news[2]
        ET.SubElement(doc, "datetime").text = news[0]
        ET.SubElement(doc, "body").text = body
        tree = ET.ElementTree(doc)
        tree.write(doc_dir_path + "%d.xml"%(i), encoding = doc_encoding, xml_declaration = True)
        i += 1
        if i%500 == 0:
            print("Sleeping for 3 minute")
            time.sleep(180)
    
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('../config.ini', 'utf-8')
    
    delta = timedelta(days=-5)
    end_date = date.today()
    start_date = end_date + delta
    news_pool = get_news_pool(start_date, end_date)
    print('Starting to crawl %d news'%len(news_pool))
    crawl_news(news_pool, 140, config['DEFAULT']['doc_dir_path'], config['DEFAULT']['doc_encoding'])
    print('done!')
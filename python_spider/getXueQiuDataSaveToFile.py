# -*- coding: UTF-8 -*-

import time
import Queue
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import sys
import traceback
import re
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')

# 文章存储数据结构为：标题  作者  文章发布时间 阅读量  文章内容
#                    title  author  timestamp    read   content
class Article:
    title = ""
    url = ""
    author = ""
    timestamp = ""
    read = 0
    content = ""

    def __init__(self, title, url, author, timestamp, read, content):
        self.title = title
        self.url = url
        self.author = author
        self.timestamp = timestamp
        self.read = read
        self.content = content


        # 参数为：点击多少次"加载更多"


# 返回值为文章的url列表，数据总条数为：50 + 15 * num
def get_article_url(num):
    browser = webdriver.Chrome(r"D:\\develop_tools\\chromedriver.exe")
    browser.maximize_window()
    browser.get('https://xueqiu.com/#/hk')

    time.sleep(5)

    # 将屏幕下滑4次，之后会出现“加载更多”按钮——此时有50篇文章
    for i in range(1, 5):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)

        # 点击num次“加载更多”——每次点击会加载15篇新闻
    for i in range(num):
        # 找到加载更多按钮，点击
        browser.find_element(By.LINK_TEXT, "加载更多").click()
        print(i)
        if(i<40):
            time.sleep(3)
        if(i>=40&i<100):
            time.sleep(3)
        if(i>=100):
            time.sleep(5)

    soup = BeautifulSoup(browser.page_source)
    article_queue = parse_html(soup)
    browser.close()
    return article_queue

def parse_html(soup):
    article_queue = Queue.Queue()
    article_divs = soup.findAll('div', {'class': 'home__timeline__item'})
    if article_divs is not None:
        for article_div in article_divs:
            url = dict(article_div.h3.a.attrs)['href']
            article_url = 'https://xueqiu.com' + url
            article_title = article_div.h3.a.string
            article_author = article_div.find('a', {'class': 'user-name'}).string
            article_timestamp = article_div.find('span', {'class': 'timestamp'}).string
            article_read = article_div.find('div', {'class': 'read'}).string
            article_read = re.findall(r'(\d+(\.\d+)?)', article_read)
            tmp = article_read[0][0]
            article = Article(url=article_url, title=article_title, author=article_author,
                              timestamp=article_timestamp, read=tmp, content='')
            article_queue.put(article)
    return article_queue

class GetContentThread(threading.Thread):
    def __init__(self, article_queue):
        threading.Thread.__init__(self)
        self.url_queue = article_queue

    def run(self):
        count = 0;
        while 1:
            try:
                count += 1
                if count % 100 == 0:
                    print count
                article = self.url_queue.get()
                article_url = article.url
                article_url = article_url.encode('utf-8')
                try:
                    file1 = open('xueqiu_datas.txt', 'a')
                    file1.write(str("hk") + '   ')
                    file1.write(str(article.author) + '   ')
                    file1.write(str(article.title) + '   ')
                    file1.write(str(article.timestamp) + '   ')
                    file1.write(str(article.read) + '   ')
                    file1.write(str(article.url) + '\n')
                    file1.close()
                    print("save ok")
                except Exception, e:
                    self.url_queue.task_done()
                    self.url_queue.put(article)
                    print 'traceback.print_exc():';traceback.print_exc()
                self.url_queue.task_done()
            except Exception, e:
                self.url_queue.task_done()
                print 'get content wrong! ', e, '\n'
                if '404' in str(e):
                    print 'URL 404 Not Found:', article.url
                elif 'HTTP' or 'URL' or 'url' in str(e):
                    self.url_queue.put(article)
                    print "Let's make a comeback "
                    continue

def start():
    # 获得所有的文章,并将它们放入队列中
    article_queue = get_article_url(300)

    # 创建10个线程，获取所有文章的具体内容,并写入mongoDB数据库
    # for i in range(5):
    gct = GetContentThread(article_queue)
    gct.setDaemon(True)
    gct.start()

    # 等待队列中的所有任务完成
    article_queue.join()

def test():
    str='2.4'
    print(float(str))

if __name__ == '__main__':
    start()
    # test()
    # print(type('2.4'))
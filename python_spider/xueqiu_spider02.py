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

# �����ݿ�����
db = MySQLdb.connect("192.168.56.128","root","123456","xueqiu" )
db.set_character_set('utf8')
cursor = db.cursor()


# ���´洢���ݽṹΪ������  ����  ���·���ʱ�� �Ķ���  ��������
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


        # ����Ϊ��������ٴ�"���ظ���"


# ����ֵΪ���µ�url�б�����������Ϊ��50 + 15 * num
def get_article_url(num):
    browser = webdriver.Chrome(r"D:\\develop_tools\\chromedriver.exe")
    browser.maximize_window()
    # browser.get('https://xueqiu.com/#/financial_management')
    browser.get('https://xueqiu.com/today#/financial_management')

    time.sleep(1)

    # ����Ļ�»�4�Σ�֮�����֡����ظ��ࡱ��ť������ʱ��50ƪ����
    for i in range(1, 5):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)

        # ���num�Ρ����ظ��ࡱ����ÿ�ε�������15ƪ����
    for i in range(num):
        # �ҵ����ظ��ఴť�����
        browser.find_element(By.LINK_TEXT, "���ظ���").click()
        print(i)
        if(i<40):
            time.sleep(1)
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
                # headers = {
                #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
                # res = requests.get(article_url, headers=headers)
                # res.encoding = 'utf-8'
                # soup = BeautifulSoup(res.text)
                # content = soup.find('div', {'class': 'detail'})
                # article.content = content
                try:
                    print('article.read : %s' % article.read)
                    sql = "INSERT INTO topic_datas(url,type,title,author,timestamp,read_sum) VALUES ('%s', '%s', '%s', '%s', '%s','%f')" \
                      % (article.url, "financial_management", article.title, article.author, article.timestamp,float(article.read))
                    cursor.execute(sql)
                    db.commit()
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
    # ������е�����,�������Ƿ��������
    article_queue = get_article_url(300)

    # ����10���̣߳���ȡ�������µľ�������,��д��mongoDB���ݿ�
    # for i in range(5):
    gct = GetContentThread(article_queue)
    gct.setDaemon(True)
    gct.start()

    # �ȴ������е������������
    article_queue.join()

def test():
    str='2.4'
    print(float(str))

if __name__ == '__main__':
    start()
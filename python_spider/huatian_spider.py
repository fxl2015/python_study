# -*- coding: UTF-8 -*-

import requests as req
from bs4 import BeautifulSoup as bs
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def test():
    raw_cookies='__s_=1; user-from=https://www.baidu.com/link?url=fn3dB646aIu8uDSLpysxAjKFNQh9aNRSMvyTGPIjLGS&wd=&eqid=9d8c39550004ada5; from-page=https://www.baidu.com/link?url=fn3dB646aIu8uDSLpysxAjKFNQh9aNRSMvyTGPIjLGS&wd=&eqid=9d8c39550004ada500000005598d45a1; _ntes_nnid=4d32008e9b276508eb8f2300b1c9e54a,1502430556389; _ntes_nuid=4d32008e9b276508eb8f2300b1c9e54a; NTES_SESS=u8Y9cI7Zwr28fxCJRSnaiLTg2IcAM3Akeib3pWFnqCTKZhjsWZ8jzDS2yZ6UZg8aLtHvv2K0zJynmBXlcRuAYawEufzsyPz9TqtYqgdYhChlbtMdgwn09jYzEdfTEh6qXzZUvAVGFrYeJS2335IlsuWuDDwGTLH3M; S_INFO=1502430685|0|2&10##|wy201505131238; P_INFO=wy201505131238@163.com|1502430685|0|ht|00&99|jix&1502372540&ht#hub&420100#10#0#0|&0|ht|wy201505131238@163.com'
    cookies = {}
    for line in raw_cookies.split(';'):
        key, value = line.split('=', 1)  # 1代表只分一次，得到两个数据
        cookies[key] = value
    testurl = 'https://love.163.com/'
    s = req.get(testurl, cookies=cookies)
    file1 = open('../datas/huatian_data_08111705.txt', 'a')
    file1.write(s.text)
    file1.close()
    print(s.text)

def test2():
    with open("../datas/huatian_data_08111354.txt", "r") as foo_file:
        soup = bs(foo_file)
        article_divs = soup.findAll('div', {'class': 'vipBanner-user-item'})
        if article_divs is not None:
            for article_div in article_divs:
                name = article_div.find('span', {'class': 'u-vertical-m'}).string
                address = article_div.find('dd', {'class': 'vipBanner-user-bid'})
                tmp_res = re.compile(r'\d+')
                age = tmp_res.findall(str(address))
                # print address
                print("name : %s" % name)
                print("age : %s" % age[0])
                print("address : %s" % address.span.string)
                # for a in address:
                #     b = repr(a).decode("unicode-escape").encode('utf8')
                #     print(b)
                    # print("address : %s" % b(0))
                    # print("age : %s" % b(1))
                # print("address : %s" % address)
                print('\n')

def test3():
    with open("../datas/huatian_data_08111705.txt", "r") as foo_file:
        soup = bs(foo_file)
        article_divs = soup.findAll('div', {'class': 'vipBanner-user-item'})
        if article_divs is not None:
            for article_div in article_divs:
                name = article_div.find('span', {'class': 'u-vertical-m'}).string
                address = article_div.find('dd', {'class': 'vipBanner-user-bid'})
                tmp_res = re.compile(r'\d+')
                age = tmp_res.findall(str(address))
                tmp_res = re.compile(r'https:.+?"')
                img = tmp_res.findall(str(article_div))
                # print address
                print("name : %s" % name)
                print("age : %s" % age[0])
                print("address : %s" % address.span.string)
                print("img : %s" % img[0])
                print('\n')
                file1 = open('huatian_datas.txt', 'a')
                file1.write(str(name) + '   ')
                file1.write(str(age[0]) + '   ')
                file1.write(str(address.span.string) + '   ')
                file1.write(str(img[0]) + '\n')
                file1.close()

if __name__ == '__main__':
    test()
    # test2()
    test3()
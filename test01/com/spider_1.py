# -*- coding:utf-8 -*-

# Created by fxl on 2017-5-4.

# import urllib2
# response=urllib2.urlopen("http://www.360.com")
# print response.read()
#
# import urllib2
# request=urllib2.Request("http://www.360.com")
# response=urllib2.urlopen(request)
# print response.read()

import urllib
import urllib2

# values={}
# values["userNo"]="admin"
# values["password"]=1
# data=urllib.urlencode(values)
# url="http://192.168.1.232/productionCenter2.0/"
# request=urllib2.Request(url,data)
# response=urllib2.urlopen(request)
# print response.read()

# import urllib2
# try:
#     response=urllib2.urlopen("http://192.168.1.232/productionCenter20.0/")
#     print response.read()
# except urllib2.URLError,e:
#     print e.reason

# import urllib
# import urllib2
#
# page=1
# url_1="http://www.qiushibaike.com/"
# url_2="http://www.qiushibaike.com/8hr/page/3/?s=4979605"
# user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
# headers={"User-Agent":user_agent}
# try:
#     req=urllib2.Request(url_2,headers=headers)
#     rsp=urllib2.urlopen(req)
#     content = rsp.read()
#     file_path = "C:\\Users\\fxl\\Desktop\\python_files\\file_0.txt"
#     f = open(file_path,'w')
#     f.write(content)
#     f.close()
#     print "end"
# except urllib2.URLError,e:
#     if hasattr(e,"code"):
#         print e.code
#     if hasattr(e,"reason"):
#         print e.reason

import urllib
import urllib2
import re
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("192.168.56.11","root","123456","test" )
db.set_character_set('utf8')
# db.execute('SET NAMES utf8;')
# db.execute('SET CHARACTER SET utf8;')
# db.execute('SET character_set_connection=utf8;')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

for i in range(50000):
    time.sleep(2)
    page=i+1
# url="http://www.qiushibaike.com/8hr/page/3/?s=4979605"
#     http: // www.qiushibaike.com / text / page / 2 /?s = 4979905
    url="http://www.qiushibaike.com/text/page/"+str(page)+"/?s=4979905"
    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    headers={"User-Agent":user_agent}
    try:
        req=urllib2.Request(url,headers=headers)
        rsp=urllib2.urlopen(req)
        content=rsp.read().decode('utf-8')
        # print content
        # pattern=re.compile('<div class="author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<a.*?'+
        #                    '<h2>(.*?)</h2></div>.*?<span>(.*?)</span>',re.S)
        pattern = re.compile(u'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
        items=re.findall(pattern,content)
        # print items
        # f=open("C:\\Users\\fxl\\Desktop\\python_files\\file_1.txt",'a+')
        for item in items:
            # f.write(item[0]+"\n")
            # f.write(item[1]+"\n")
            # f.write(item[2]+"\n")
            # f.write("\n\n\n")
            sql = "INSERT INTO jokes(name, \
               content,good) \
               VALUES ('%s', '%s', '%d')" % \
              (item[0],item[1],int(item[2]))
            cursor.execute(sql)
        print page,": end"
        db.commit()
        # f.close()
    except urllib2.URLError,e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason



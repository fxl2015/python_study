# -*- coding:utf-8 -*-

# Created by fxl on 2017-5-8.

import urllib
import urllib2
import re
import sys
import time
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')

# 打开数据库连接
db = MySQLdb.connect("192.168.56.11","root","123456","test" )
db.set_character_set('utf8')
cursor = db.cursor()

for i in range(50000):
    time.sleep(2)
    page=i+1
    url="http://www.qiushibaike.com/textnew/page/"+str(page)+"/?s=4980691"
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
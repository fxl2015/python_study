# -*- coding:utf-8 -*-

# Created by fxl on 2017-5-4.

import re

# s1='hello world'
# s2='Hello World'
# regex=re.compile(s1,re.I)
# print regex.match(s2).group()

s='''aaa
bbb
ccc
'''
regex=re.compile('^\w+',re.M)
print regex.findall(s)

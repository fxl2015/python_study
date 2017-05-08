# print "121212"
# print("sasas")


# a=10
# if a>100:
#     print a
# else:
#     print -a

# print 'i\'m ok'
# print 'amamm\n\n\n\n\n'

# print '''wqwq
# rere
# gfgfgf
# kjkjkjk
# '''

# print True and False

# print None
# PI=3.1415926
# print 10/3.0
# print ord('a')
# print chr(102)
#
# a='hhhhh'
# print "hello,%s"%a

# classmates=['a','b','c']
# print classmates
# print len(classmates)
# classmates.append('d')
# print classmates[3]
# classmates.pop()
# print classmates


# l=[11,True,None,'aaa',"qqq"]
# print l


# l=[]
# print len(l)


# t=(1,2,3,4)
# print t

# t=(1,["a","b","c",None])
# print t

# t=[1,"aaa",'b',True,None,3.23]
# for i in t:
#     print i

# print range(16)
# sum=0
# for i in range(100):
#     if i>98:
#         print i
#     sum=sum+i
# print sum


# d={'a':100,'b':80,'c':60}
# d['a']=112
# print d['a']
# print 'c' in d

# l=[1,2,3,4,5]
# # l.add(22)
# s=set(l)
# s.add(321)
# print s
# s.remove(3)
# print s
# s=str(11.23)
# print s
# print type(s)
# print bool(0)

# def my_abs(x):
#     if x>=0:
#         return x,1
#     else:
#         return -x,-1
#
# print my_abs("wqwqwqw")

# def pass_func():
#     pass

# print pass_func()

# def enroll(name,gender,age=6,city="wuhan"):
#     print 'name:',name
#     print 'gender:',gender
#     print 'age:',age
#     print 'city:',city
# enroll("john",'Female',5,'beijing')

# def add_end1(l=[]):
#     l.append('end')
#     return l
#
# print add_end1()
# print add_end1()
# print add_end1()
#
# print "---------------------"
#
# def add_end2(l=None):
#     if l is None:
#         l=[]
#     l.append('end')
#     return l
#
# print add_end2()
# print add_end2()
# print add_end2()

# t=(1,2,3)
# print t[1]

# def fact(x):
#     if x==1:
#         return 1
#     return x*fact(x-1)
# print fact(1100)

# def fact(n):
#     if n==1:
#         return 1
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num==1:
#         return product
#     return fact_iter(num-1,num*product)
#
# print fact(1000)

# t=(1,2,3,4,5)
# print t[1:3]

# print range(11,22)

# l=[1,2,3,4,5]
# def get_(x):
#     print 'x=',x
# print map(get_,l)
#
# def add_(a,b):
#     print "a=",a
#     print "b=",b
#     return a+b
#
# print reduce(add_,l)
# l=[11,2,13,4,5]
# def filter_(x):
#     if x>5:
#         print x
#         return x
#
# print filter(filter_,l)
# print sorted(l)
# f=lambda x:x*x*x
# print f(20)

# def now():
#     print "2017-05-02"
# f=now
# print f.__name__

# import sys
# print sys.path

# class Student(object):
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def getInfo(self):
#         print 'name:',self.__name
#         print 'age:',self.__age
#
#
# s=Student("aa",11)
# s.getInfo()
# s.name="sss"
# s.getInfo()

# class Dog():
#     def run(self):
#         print "dog run"
#
# a=Dog()
# b=[1,2,3]
# c=(1,2,3)
# d={"1":1,"2":2}
#
# print isinstance(a,Dog)
# print isinstance(b,list)
# print isinstance(c,tuple)
# print isinstance(d,dict)

# print type({1:2})
# print dir(list)

# class Student(object):
#     def __init__(self,name):
#         self.name=name
#
#     def getInfo(self):
#         return self.name
#
# s=Student("hike")
# print isinstance(s,Student)
# a=s.getInfo()
# print "a=",a
# s.name="sss"
# print s.getInfo()

# class Animal(object):
#     def run(self):
#         print "running..."
#
# class Cat(Animal):
#     pass
#
# class Dog(Animal):
#     pass

# a=Animal()
# c=Cat()
# d=Dog()
# c.run()
# d.run()

# class Student(object):
#     pass
#
# s=Student()
# s.name="abc"
# print s.name
#
# def set_age(self,age):
#     self.age=age
#
# from types import MethodType
# s.set_age=MethodType(set_age,None,Student)
# s.set_age(22)
# print s.age
#
# s2=Student()
# print s2.age

# try:
#     print 'try...'
#     r=1/0
#     print 'result=',r
# except ValueError,e:
#     print 'ValueError:',e
# except ZeroDivisionError,e:
#     print 'except:',e
# finally:
#     print 'finally...'
#     # raise ZeroDivisionError
# print 'end'

# import logging
# logging.basicConfig(level=logging.INFO)
# s='0'
# n=int(s)
# logging.info('n=%d' % n)
# print 10/n

# try:
#     readFile=open('C:\\Users\\fxl\\Desktop\\20170502\\msgsqlserver.log','rb')
#     # print readFile.read()
#     lines=readFile.readlines()
#     a=0
#     for line in lines:
#         if a<5:
#             print line.strip()
#         a=a+1
# except IOError,e:
#     print 'IOError:',e
# finally:
#     if readFile:
#         readFile.close()
#     print 'end'


# try:
#     wr=open('C:\\Users\\fxl\\Desktop\\20170502\\hello.txt','w')
#     wr.write("hello world!!!")
# except IOError,e:
#     raise
# finally:
#     if wr:
#         wr.close()

# import os
# print os.name
# print os.uname

# try:
#     import cPickle as pickle
# except:
#     import pickle

# try:
#     d=dict(name='bob',age=20,score=90)
#     f=open('C:\\Users\\fxl\\Desktop\\20170502\\hello.txt','wb')
#     pickle.dump(d,f)
# except IOError,e:
#     raise
# finally:
#     if f:
#         f.close()

# f=open('C:\\Users\\fxl\\Desktop\\20170502\\hello.txt','rb')
# d=pickle.load(f)
# f.close()
# print d

# import json
#
# d={"name":"john","age":19}
# json.dumps(d)

# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print 'Run child process %s (%s)...' % (name,os.getpid())
#
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p=Process(target=run_proc,args=('test',))
#     print 'Process will start.'
#     p.start()
#     p.join()
#     print 'Process end.'

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)


app = Application()
app.master.title('Hello World')
app.mainloop()













































# -*- coding: utf-8 -*-
"""
--------------------------------------- 
   程序：百度贴吧小说爬虫 
   版本：0.1 
   作者：gkf
   日期：2016-09-25 
   语言：Python 2.7 
   操作：输入你想读的页码 
   功能：看小说：《少年，私奔可好》 
--------------------------------------- 
"""  
 
import urllib2

import re
 
#----------- 加载处理糗事百科 -----------  
class HTML_Model:  
      
    def __init__(self):  
        self.page = 1  
        self.pages = {}  
        self.enable = False

  
    # 将所有的段子都扣出来，添加到列表中并且返回列表  
    def GetPage(self,page):  
        myUrl = "http://tieba.baidu.com/p/3091392292?see_lz=1&pn=" + page  
        myResponse  = urllib2.urlopen(myUrl)  
        myPage = myResponse.read()  
        #encode的作用是将unicode编码转换成其他编码的字符串  
        #decode的作用是将其他编码的字符串转换成unicode编码  
        unicodePage = myPage.decode("utf-8")  
  
        # 找出所有class="content"的div标记  
        myItems = re.findall('<div id=.*?class="d_post_content j_d_post_content ">\s{12}(.*?)</div>',unicodePage,re.S)
        return myItems

    #缓存
    def Cache(self,cache_page):
        
        self.pages[cache_page]=self.GetPage(str(cache_page))

    #读取   
    def Read(self):
        self.enable=True
        read_page=input("you want to read ? page:")
        self.page=read_page
        self.Cache(self.page)
        
        now_page=self.pages[self.page]
        
        for x in now_page:
                x=re.sub("<a.*?>|</a>|<img.*?>","",x)
                x=x.replace("<br>","\n")
                if x.find('<.*?>')==-1:
                       print '\n\n\n',x
    #循环页码
    def Start(self):
        self.enable=True
        while self.enable:
            self.Read()
            want_or_not=raw_input("want continue? Y/N:")
            if want_or_not=='Y':
                pass
            else:
                self.enable=False
                break
                
            
            


        
  
  
#----------- 程序的入口处 -----------  
print u""" 
--------------------------------------- 
   程序：百度贴吧小说爬虫 
   版本：0.1 
   作者：gkf
   日期：2016-09-25 
   语言：Python 2.7 
   操作：输入你想读的页码 
   功能：看小说：《少年，私奔可好》 
--------------------------------------- 
"""  
  
  
print u'少年，私奔可好？'    
myModel = HTML_Model()  
myModel.Start()  

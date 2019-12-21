# -*- coding: utf-8 -*-
import scrapy
import re
import json
from scrapy.http import FormRequest

class SjtuSpider(scrapy.Spider):
    name = 'sjtu'
    allowed_domains = ['sjtu.edu.cn']
    global urls,course,courselist
    course = {}
    courselist=[]
    urls=[]
    t={}
    def start_requests(self):
        f= open("D:\\19aw\\spider\\sjtuSpider\\MajorUrl.json","r");
        urls1 = f.read()
        f.close()
        urls1 = json.loads(urls1)
        for url1 in urls1:
            yield scrapy.Request(url1["Majorname"],self.parse)
    def parse(self, response):
        selectors = response.xpath('//a[@href]')
        courseClass=[]
        thisUrl = response.xpath("//form[@id='PyjhQuery_Jb']/@action").get()
        for selector in selectors:
            js=selector.xpath('./@href').get()
            text=selector.xpath('./text()').get()
            id=selector.xpath('./@id').get()
            courseClass.append({'js':js,'text':text,'id':id})
        VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").get()
        EVENTVALIDATION = response.xpath("//input[@name='__EVENTVALIDATION']/@value").get()
        for course in courseClass:
            if(course and course['id'][3]>='0' and course['id'][3]<='9'):
                url="http://electsys.sjtu.edu.cn/edu/pyjh/"+thisUrl
                form_data={
                    '__EVENTTARGET': course['id'],
                    '__EVENTARGUMENT': '',
                    '__VIEWSTATE': VIEWSTATE,
                    '__VIEWSTATEGENERATOR': 'D24CB33A',
                    '__EVENTVALIDATION': EVENTVALIDATION
                }
                yield FormRequest(url,formdata=form_data,callback=self.getUrl)
    def getUrl(self,response):
        selectors = response.xpath('//head//script')
        url = selectors.xpath('./text()').get()
        url = url[13:-2]
        url = 'http://electsys.sjtu.edu.cn/edu/pyjh/'+url
        yield scrapy.Request(url,callback=self.getCourse)
    def getCourse(self,response):
        selectors=response.xpath('//tr[@class="tdcolour1"]|//tr[@class="tdcolour2"]')
        course = {}
        for selector in selectors:
            id = selector.xpath('./td[2]/a/text()').get()
            name = selector.xpath('./td[3]/text()').get()
            if(id):
                course['id']=id
                course['name']=name
                yield course
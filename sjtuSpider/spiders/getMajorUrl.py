# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest

class GetmajorurlSpider(scrapy.Spider):
    name = 'getMajorUrl'
    allowed_domains = ['sjtu.edu.cn']
    start_urls = ['http://electsys.sjtu.edu.cn/edu/pyjh/pyjhQueryNew.aspx']
    Majorname = ""
    def parse(self, response):
        url="http://electsys.sjtu.edu.cn/edu/pyjh/pyjhQueryNew.aspx"
        form_data={
            'dpRxnd': '2019',
            'dpJhlx': '1',
            'btnQuery.x':'51',
            'btnQuery.y':'15',
            '__VIEWSTATE': '/wEPDwUKLTgyODYyMTA1Mg9kFgICAQ9kFgYCAw8QDxYGHg1EYXRhVGV4dEZpZWxkBQRyeG5kHg5EYXRhVmFsdWVGaWVsZAUEcnhuZB4LXyFEYXRhQm91bmRnZBAVEwQyMDE5BDIwMTgEMjAxNwQyMDE2BDIwMTUEMjAxNAQyMDEzBDIwMTIEMjAxMQQyMDEwBDIwMDkEMjAwOAQyMDA3BDIwMDYEMjAwNQQyMDA0BDIwMDMEMjAwMgQyMDAxFRMEMjAxOQQyMDE4BDIwMTcEMjAxNgQyMDE1BDIwMTQEMjAxMwQyMDEyBDIwMTEEMjAxMAQyMDA5BDIwMDgEMjAwNwQyMDA2BDIwMDUEMjAwNAQyMDAzBDIwMDIEMjAwMRQrAxNnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZGQCBg8PFgIeBFRleHRlZGQCCg88KwALAGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFCGJ0blF1ZXJ5BCKjF3wQqjtso89iaFf0EYD1xVY=',
            '__VIEWSTATEGENERATOR': '8621C13A',
            '__EVENTVALIDATION': '/wEWFwL++qjiAgL5qInBBQL4qInBBQLj6bOtBALj6c/BDALj6ZupDgLj6bfOBgLj6cPiDQLj6d+HBALj6eu8AwLj6YfRCwLj6ZP2AgLj6a+rCQKI0J2yDgKI0KnXBgKI0IU+AojQkdMIAojQrYgHAojQua0OAojQ1cEGAojQ4eYNAojQ/ZsEAu+OvL8Fc7yLUdtP/NlsYgowHNuGK9zBbzA=',
            }
        yield FormRequest(url,formdata=form_data,callback=self.getList)
        
    def getList(self,response):
        f= open("D:\\19aw\\spider\\sjtuSpider\\sjtuSpider\\spiders\\str.txt","r")
        viwestate=f.read()
        f.close()
        selectors = response.xpath("//form[@id='examArrangeForTeacher']//table[@id='grdJxjh']//tr[@class='tbshowlist']")
        for selector in selectors:
            aa = selector.xpath(".//a[@href]")
            for a in aa:
                self.Majorname = a.xpath("./text()").get()
                if(self.Majorname!=''):
                    str = a.xpath("./@href").get()
                    str = str[25:-5]
          #          print(123,Majorname,str)
                    url="http://electsys.sjtu.edu.cn/edu/pyjh/pyjhQueryNew.aspx"
                    form_data={
                        '__EVENTTARGET': str,
                        '__VIEWSTATE': viwestate,
                        '__EVENTARGUMENT': '',
                        '__VIEWSTATEGENERATOR': '8621C13A',
                        '__EVENTVALIDATION': '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',
                        'dpJhlx': '1',
                        'dpRxnd': '2019'
                    }
                    yield FormRequest(url,formdata=form_data,callback=self.getUrl)

    def getUrl(self,response):
        url = response.xpath("//head//script/text()").get()
        url = url[13:-3]
    #    print(123,url)
        urlList = {}
        print(self.Majorname)
        urlList[self.Majorname] = 'http://electsys.sjtu.edu.cn/edu/pyjh/'+url
        yield urlList
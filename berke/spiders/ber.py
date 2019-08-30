# -*- coding: utf-8 -*-
# import scrapy
#
#
# class BerSpider(scrapy.Spider):
#     name = 'ber'
#     allowed_domains = ['berkeley.edu']
#     start_urls = ['http://berkeley.edu/']
#
#     def parse(self, response):
#         pass
# -*- coding: utf-8 -*-
import scrapy
import pymysql
from berke.items import BerkeItem
from scrapy_redis.spiders import RedisSpider, Spider
import json

# connect = pymysql.connect(
#     host='127.0.0.1',
#     user='root',
#     passwd='123',
#     db='test1',
#     charset='utf8'
# )
#
# cursot = connect.cursor()

school_name = 'University of California, Berkeley'


class UscSpider(Spider):
    name = 'ber'
    allowed_domains = ['berkeley.edu']
    num = 0
    url = 'https://classes.berkeley.edu/search/class?page='
    start_urls = (
        url + str(num) + "&f%5B0%5D=im_field_term_name%3A851",
    )

    def parse(self, response):
        ber_list = response.xpath('//li[@class="search-result"]')
        # print(ber_list)
        # ber_list = response.xpath('//h2[@class="ls-course-title fmpbook"]')
        # print(ber_list)

        for i in ber_list:
            item = BerkeItem()

            item['school'] = school_name
            # 上课日期
            json1 = i.xpath('./div/@data-json').extract_first()
            json1 = json.loads(json1)
            # # 上课类型
            item['type'] = json1['component']['description']

            # 课程简称
            course_title = json1['displayName']
            # print(course_title)
            course_title = course_title.split(" ")[2]
            item['course_title'] = course_title

            # 课程编号
            course_number = json1['displayName']
            course_number = course_number.split(" ")[3]
            item['course_number'] = course_number

            # 院系
            dept = json1['academicOrganization']['description']
            item['dept'] = json1['academicOrganization']['description']

            # 课程简介

            introduce = json1['course']["description"]
            introduce1 = introduce.strip("\n").replace("\n", "").replace("\t", "")
            if introduce != '':
                item['introduce'] = introduce1
            else:
                item['introduce'] = "NULL"

            # 课程名称
            try:
                item['name'] = json1['course']['title']
            except KeyError as e:
                print(e)
                item['name'] = "NULL"

            # 学分
            try:
                item['units'] = json1['course']['credit']['value']['fixed']['units']
            except KeyError as e:
                print(e)
                item['units'] = json1['course']['credit']['value']['range']['maxUnits']
            except IndexError as e:
                item['units'] = "NULL"
            # 上课地点
            # k2 = "meetings"
            # if k2 in json1:
            try:
                meetings = json1["meetings"]
                # print(meetings)
                for a in meetings:
                    start_time = a['startTime']
                    end_time = a['endTime']
                    item['time'] = str(start_time + "-" + end_time)

                    try:
                        item['week'] = a['meetsDays']
                    except KeyError as e:
                        print(e)
                        item['week'] = "NULL"

                    try:
                        item['location'] = a["location"]["description"]
                    except (KeyError, TypeError) as e:
                        print(e)
                        item['location'] = "NULL"

                    instructor = []
                    try:
                        for b in a["assignedInstructors"]:
                            # print(b["instructor"]["names"])
                            for c in b["instructor"]["names"]:
                                instructor1 = (c["formattedName"]).replace(".", "")
                                instructor.append(instructor1)
                                instructor2 = set(instructor)
                                instructor2 = ",".join(instructor2)
                                # print("111111111111111111111111111111111111111111111111111111111", instructor)
                        item['instructor'] = instructor2
                    except (KeyError, TypeError) as e:
                        item['instructor'] = "NULL"

            except KeyError as e:
                print(e)
                # item['instructor'] = ",".json(instructor)
                # print("1111111111111111111111111111111111111111111111111111",c["formattedName"])
                # print(a["names"])
                # for b in a:
                #     print(b['names'])
                # print(a['names'])
                # json2 = i.xpath('./div/@data-term-details').extract_first()
            # json2 = json.loads(json2)
            # json3 = i.xpath('./div/@data-enrollment').extract_first()
            # json3 = json.loads(json3)
            json4 = i.xpath('./div/@data-node').extract_first()
            json4 = json.loads(json4)

            # 上课地点URL
            location_url = json4['buildingURL']
            if location_url != '':
                item['location_url'] = location_url
            else:
                item['location_url'] = "NULL"
            # 详情URL
            item['info'] = "https://classes.berkeley.edu" + json4['nodeURL']


            yield item

            if self.num < 360:
                self.num += 1
                yield scrapy.Request(self.url + str(self.num) + str("&f%5B0%5D=im_field_term_name%3A851"),
                                     callback=self.parse)



# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class BerkeItem(Item):

    # 上课日期
    week = Field()

    # 学分
    units = Field()

    # 上课时间
    time = Field()

    # 教授
    instructor = Field()

    # 学校院系
    dept = Field()

    # 课程简称
    course_title = Field()

    # 课程编号
    course_number = Field()

    # 课程类型
    type = Field()

    # 上课地点
    location = Field()

    # 地图链接
    location_url = Field()

    # 简介
    introduce = Field()

    # 课程名称
    name = Field()

    # 详情URl
    info = Field()

    # 学校
    school = Field()



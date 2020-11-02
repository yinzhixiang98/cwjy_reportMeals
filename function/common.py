# coding: utf-8
# description: 常用函数，在debugtalk.py 中直接调用

import time
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random
import calendar as cla
import datetime

def getAllTitle(mes):  # mes 是一个包含多个字典的list
    allTitle = []
    for i in list(mes):
        allTitle.append(i['title'])
    return allTitle


def nSecondDelay(n, begin=True):  # 放回延迟n秒后的时间戳, begin 默认当前时间
    if begin:
        now = int(time.time() * 1000)
    else:
        now = int(begin)  # 非默认当前时间，begin是13位的时间戳

    return now + n * 1000


def date2timeStamp(date_and_time):
    timeArray = time.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
    return int((time.mktime(timeArray)) * 1000)  # 毫秒级 13位时间戳


def title2Id(mes):  # 由会议/培训名称获取id, 若名称相同，则会随机获取其中一个的id
    title_id = {}
    for i in list(mes):
        title_id[i["title"]] = i["itemId"]
    return title_id


def findIdByTitle(title, title_id):
    # title_id = json.loads(title_id)
    return title_id[title]


def getLearningId(title, mes):
    id = "NULL"
    for i in list(mes):
        if i["content"] == title:
            id = i["id"]
    return id


def getLearningGId(title, mes):
    id = "NULL"
    for i in list(mes):
        if i["content"] == title:
            id = i["gid"]

    return id


def collectValuesOfSameKey(key, dictList):  # 获取一个字典列表下某一个相同key的所有值
    values = []
    for dic in list(dictList):
        values.append(dic[key])
    return values


def findTargetByKey(key, value, dataList, targetKey):  # 在字典列表中查找是指定key值键值为value的对象，返回这个元素的targetKey属性
    rtTarget = None
    for data in list(dataList):
        if data[key] == value:
            rtTarget = data[targetKey]
    return rtTarget


def findTargetsByKey(key, value, dataList):           # 在字典列表中查找是指定key值键值为value的对象，返回这个元素的targetKey属性
    rtTarget = []
    for data in list(dataList):
        if data[key] == value:
            rtTarget.append(data)
    return rtTarget


def getPicId(env_type):
    if env_type == "test":
        picId = "a78a1a18d0f94b82bf78b0a47d920b35"
    else:
        picId = "85db7570d9044cbaa088f91907c826f9"
    return picId


def imageInfoEncoder():
    code = MultipartEncoder(
        fields={
            'file': ("1.png", open("C:/Users/xiaojianwei/Desktop/zx1.jpg", 'rb'), 'image/jpeg')
        },
        boundary="----WebKitFormBoundary" + str("123789xyz678")
    )
    return [code.to_string(), code.content_type]


def getAttachId(env_type):  # 制度部分附件id
    if env_type == "test":
        return "dbf395fac9a84f398190325f83c25912"
    else:
        return "e69f5a321acd44d3ac98f1a7618df449"


def stamp2Time(stamp):
    stamp = int(stamp)
    stamp = int(stamp/1000)
    timeArray = time.localtime(stamp)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


def timeMinDiff(time1, time2):                 # 计算两个时间之间的分钟数  time1/time2: %Y-%m-%d %H:%M:%S
    stamp1 = date2timeStamp(time1)
    stamp2 = date2timeStamp(time2)
    return int((stamp2 - stamp1)/60000)       # ms 转换成 min


def getFirstOrLastDayOfMonth(day_type):      # 获取该月第一天与最后一天时间
    thisYear = datetime.datetime.now().year
    thisMonth = datetime.datetime.now().month
    d = cla.monthrange(thisYear, thisMonth)
    if day_type == "last":
        return "%d-%d-%d %.2d:%.2d:%.2d"%(thisYear, thisMonth, d[1], 23, 59, 59)
    if day_type == "first":
        return "%d-%d-%d %.2d:%.2d:%.2d" % (thisYear, thisMonth, 1, 00, 00, 00)


def getToday1(isYear=True):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    if isYear:
        return str(year)+"年"+str(month)+"月"+str(day)+"日"
    else:
        return str(month)+"月"+str(day)+"日"


def afterNDays(n):
    nowTime = time.time()
    seconds = int(n)*86400                        # 一天86400秒
    date = time.localtime(int(nowTime+seconds))
    return "%d-%d-%d" %(date.tm_year, date.tm_mon, date.tm_mday)

# print(afterNDays(30))


def getDayOfWeek(type):                        # 0返回本周周日的日期， 1返回本周周六的日期
    dayOfWeek = datetime.datetime.today().weekday()
    today = datetime.date.today()
    sunday = today - datetime.timedelta(dayOfWeek)
    saturday = today + datetime.timedelta(6-dayOfWeek)
    if type == 0:
        return sunday
    if type == 1:
        return saturday



def getRandomPicId():
    picids = ['a78a1a18d0f94b82bf78b0a47d920b35', '37a0bb37cd8a4695916ef279da153199', 'c18403c798ae46f7984d5684260f24ae','24438b6a3f5e4586b0cf562228241086', '8db9bfc6dade4eca9a44c3617df5cd78',\
              '98b3ec0dd150430c9f5bbc58d5b1e3ca', '6602ad8666a0452fa3eae20db1f36d69']
    return random.choice(picids)

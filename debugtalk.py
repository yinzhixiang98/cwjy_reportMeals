import time
import random
# from testcases import test
import calendar
import datetime
from function import common
from function import adminCommon
import os
import re


def sleep(cls):
    return time.sleep(cls)

def get_num(begin,end)->int:
    num = end - begin
    return num

def get_addnum(begin):
    num = int(begin) + 1
    return num

def rendom_num():
    rm=random.randint(0, 100)
    return rm

def ENV(keyname):
    '''
    获取环境keyname对应的值
    :return:
    '''
    value = os.environ.get(keyname, '')
    return value


def get_base_url(env_type="test"):
    if env_type == "test":
        return "https://im.ygsoft.com/testing/ecs"
    elif env_type == "release":
        return "https://im.ygsoft.com/release/ecs"
    else:
        return "https://im.ygsoft.com/move/ecs"


def get_timestamp(get_time="start"):
    ts = calendar.timegm(time.gmtime())
    ts1 = ts + 10000
    if get_time == "start":
        return (int(round(ts * 1000)))
    else:
        return (int(round(ts1 * 1000)))


def Catch_PicId():
    return test.catch_pic_ID()


def get_date(get_datatime="tody"):
    today = datetime.date.today()
    delta = datetime.timedelta(days=7)
    n_days = today + delta
    if get_datatime == "tody":
        return today
    else:
        return n_days


# 生成随机电话号码
def phoneNORandom():
    return adminCommon.phoneNORandom()


# 随机生成新增组织name
def get_org_name():
    return adminCommon.get_org_name()


def getCurrentDateTime():  # 获取当前时间
    return adminCommon.getCurrentDateTime()


# admin update-org
def get_orgKind():
    return adminCommon.get_orgKind()


# begin和end都包含
def getRandNum(begin, end):
    return adminCommon.getRandNum(begin, end)


def getAlluserName(data):
    return adminCommon.getAlluserName(data)


def getAllPhone(data):
    return adminCommon.getAllphone(data)


def getpostGid(data):
    return adminCommon.getPostGid(data)


def getAllorgGid(data):  # data 是一个包含多个字典的list
    return adminCommon.getAllorgGid(data)


def getRandomOne(data):  # data是一个list，随机获取list中的一个数据
    return adminCommon.getRandomOne(data)



#  ********************  PC   begin  *****************************************

def title2Id(mes):
    return common.title2Id(mes)


def findIdByTitle(title, title_id):                       # 获取id（通用查询）
    return common.findIdByTitle(title, title_id)


def getLearningId(title, mes):                            # 培训id（专用）
    return common.getLearningId(title, mes)


def getLearningGid(title, mes):                           # 培训gid（专用）
    return common.getLearningGId(title, mes)


def collectValuesOfSameKey(key, dictList):               # 获取一个字典列表下某一个相同key的所有值
    return common.collectValuesOfSameKey(key, dictList)


def findTargetByKey(key, value, dataList, targetKey):     # 在字典列表中查找是指定key值键值为value的对象，返回这个元素的targetKey属性
    return common.findTargetByKey(key, value, dataList, targetKey)


def findTargetsByKey(key, value, dataList):     # 类似findTargetByKey, 不过返回值为列表，多个值
    return common.findTargetsByKey(key, value, dataList)


def getTheNthOne(n, dataList):                            # 获取列表中第N个元素
    if n < len(dataList):
        return dataList[n]
    else:
        return dataList[0]


def imageInfoEncoder():
    data = common.imageInfoEncoder()
    return str(data[0])


def getPicId(env_type):                                   # 返回一张图片id， testing中与release中的不同
    return common.getPicId(env_type)


def getLength(dataList):                                  # 获取字典长度
    return len(list(dataList))


def sub(a, b):
    return a - b


def getAttachId(env_type):                                # 制度部分附件id
    return common.getAttachId(env_type)


def getAllTitle(mes):                                     # mes 是一个包含多个字典的list
    return common.getAllTitle(mes)




# *************************  时间与日期处理 **************************************

def timeMinDiff(time1, time2):                           # 计算两个时间之间的分钟数
    return common.timeMinDiff(time1, time2)              # 计算两个时间之间的分钟数  time1/time2: %Y-%m-%d %H:%M:%S


def getFirstOrLastDayOfMonth(day_type):                  # 获取该月第一天与最后一天时间 格式：2020-08-01 00:00:00  或 2020-08-31 23:59:59
    return common.getFirstOrLastDayOfMonth(day_type)     # day_type: first, last


def stampDiff2Min(s1, s2):                               # 两个时间戳之间相差的分钟数
    return int((s2 - s1) / 60000)


def getToday():                                          # 获取当天日期 格式： 2020-08-23
    return time.strftime("%Y-%m-%d", time.localtime())


def getToday1(isYear=True):                              # 获取当天日期 格式：
    return common.getToday1(isYear)                      # isYear=True     2020年8月24日
                                                         # isYear=False    8月24日


def afterNDays(n):                                       # 获取当前日期N天后的日期
    return common.afterNDays(n)


def firstSecondOfADay(date):                             # 返回 2020-08-23 00:00:00 类似零时时刻
    return str(date)+" 00:00:00"


def lastSecondOfADay(date):                              # 返回 2020-08-23 23:59:59 类似最后时刻
    return str(date)+" 23:59:59"


def getDayOfWeek(type):                                  # 0返回本周周日(第一天)的日期， 1返回本周周六(最后一天)的日期
    return common.getDayOfWeek(type)


def stamp2Time(stamp):                                   # 时间戳(13位)转换成时间 格式： 2020-7-22 12：10：00
    return common.stamp2Time(stamp)



def date2timeStamp(date_and_time):                        # date_and_time格式： 2020-7-22 12：10：00
    return common.date2timeStamp(date_and_time)           # 13位时间戳



def nSecondDelay(n, begin=True):                          # n秒延迟后的时间戳, begin=True则默认当前时间作为延时开始点
    return common.nSecondDelay(n, begin=begin)


def getUTCTime():                                         # 获取UTC格式的时间
    return adminCommon.getUTCTime()


def getCurrentDayofWeek(weektype,type): # 根据当前日期获取，工作计划和工作总结时间戳;用于PC端工作周报管理

    return adminCommon.getCurrentDayofWeek(weektype, type)

def getRandomPicId():                                     # 随机获取一张图片id
    return common.getRandomPicId()

def sleep():
    time.sleep(2)


def get_file(path):                                       # 读取文件数据
    return open(path, "rb")



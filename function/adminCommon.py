import random
import time
import datetime
from function import common
# 生成随机电话号码
def phoneNORandom():
    prelist = ["130", "136", "150", "138", "139", "159"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


# 随机生成新增组织name
def get_org_name():
    prelist = ["南昌", "萍乡", "井冈山", "鄱阳", "景德镇", "新余", "樟树", "丰城"]
    return random.choice(prelist) + "".join(random.choice("123456789") for i in range(2))


# update接口获取postName
def get_postName():
    prelist = ["局长", "副局长", "处长", "副处长", "科长", "副科长", "无"]
    return random.choice(prelist)


def getCurrentDateTime():  # 获取当前时间
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

#admin update-org
def get_orgKind():
    prelist=["DEFAULT","STUDENT","PARTNER","CUSTOMER","OTHER"]
    return random.choice(prelist)

#begin和end都包含
def getRandNum(begin, end):
    return random.randint(begin, end)

def getAlluserName(data):  # data 是一个包含多个字典的list
    AlluserName = []
    for i in list(data):
        AlluserName.append(i['userName'])
    return AlluserName

def getAllphone(data):  # data 是一个包含多个字典的list
    Allphone = []
    for i in list(data):
        Allphone.append(i['phone'])
    return Allphone

def getAllorgGid(data):  # data 是一个包含多个字典的list
    AllorgGid = []
    for i in list(data):
        AllorgGid.append(i['orgGid'])
    return AllorgGid

def getPostGid(data):
    AllpostGid=[]
    for i in list(data):
        AllpostGid.append(i['gid'])
    return random.choice(AllpostGid)

def getRandomOne(data):    #data是一个list，随机获取list中的一个数据
    return random.choice(data)

def getUTCTime(): #返回UTC格式的时间
    local = datetime.datetime.now()
    return datetime.datetime.strftime(local, "%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'

def getCurrentDayofWeek(weektype,type):         #weektype为last表示上周，current表示本周; type Mon表示返回当前工作周的周一,Sun表示返回当前工作周的周日
    dayOfWeek = datetime.datetime.today().weekday()   #返回当前日期的星期;0为星期一，依次到6表示星期日
    today = datetime.date.today()
    monday = today - datetime.timedelta(dayOfWeek)
    mondayTime = str(monday) + " 00:00:00"
    mondayTimeArray=time.strptime(mondayTime,"%Y-%m-%d %H:%M:%S")
    mondayTimeStamp = int((time.mktime(mondayTimeArray)) * 1000)

    lastmonday = today - datetime.timedelta(dayOfWeek+7)
    lastmondayTime = str(lastmonday) + " 00:00:00"
    lastmondayTimeArray = time.strptime(lastmondayTime, "%Y-%m-%d %H:%M:%S")
    lastmondayTimeStamp = int((time.mktime(lastmondayTimeArray)) * 1000)

    sunday = today + datetime.timedelta(6 - dayOfWeek)
    sundayTime = str(sunday) + " 23:59:59"
    sundayTimeArray = time.strptime(sundayTime, "%Y-%m-%d %H:%M:%S")
    sundayTimeStamp = int((time.mktime(sundayTimeArray)) * 1000) + 999

    lastsunday = today - datetime.timedelta(dayOfWeek + 1)
    lastsundayTime = str(lastsunday) + " 23:59:59"
    lastsundayTimeArray = time.strptime(lastsundayTime, "%Y-%m-%d %H:%M:%S")
    lastsundayTimeStamp = int((time.mktime(lastsundayTimeArray)) * 1000) + 999

    if weektype == "last" and type == "Mon":
        return lastmondayTimeStamp
    if weektype == "last" and type == "Sun":
        return lastsundayTimeStamp
    if weektype == "current" and type == "Mon":
        return mondayTimeStamp
    if weektype == "current" and type == "Sun":
        return sundayTimeStamp



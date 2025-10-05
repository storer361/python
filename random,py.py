import random
import time
def getRandomdate(stardate,endDate):
    print("Random date between",stardate,"and",endDate)
    randomGenerator = random.random()
    dateformat = '%m/%d/%Y'
    stime = time.mktime(time.strptime(stardate,dateformat))
    etime = time.mktime(time.strptime(endDate,dateformat))
    randomTime = stime + randomGenerator * (etime - stime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
print("random Date =",getRandomdate("1/1/2016","12/12/2018"))
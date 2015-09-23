import os
import datetime
import time

count = 1
num = 0
usetime = []
closetime = []
while (count < 11):
    print('开始启动......')
    if os.popen('"C:\\Program Files (x86)\\Droid4X\\droid4x.exe"'):
        time1 = datetime.datetime.now()
    print('第%d次启动开始...'%count)
    a = input('启动完成请打点...')
    if a == '1':
        time2 = datetime.datetime.now()
    # time.sleep(3)
    if os.popen('taskkill /im droid4x.exe'):
        time3 = datetime.datetime.now()
    # print(time1,time2)


    while(True):
        info = os.popen('tasklist | find /i "droid4x.exe"').read()
        if info == '':
            time4 = datetime.datetime.now()
            break


    t = time2 - time1
    t1 = time4 - time3
    
    usetime.append(t.seconds)
    closetime.append(t1.seconds)
    print('第%d次启动用时:'%count,usetime[num],t)
    print('第%d次关闭用时:'%count,closetime[num],t1)
    count = count + 1
    # time.sleep(10)


a = 0
for i in usetime:
    a = a + i
print('启动平均时间:',a/10)
for i in closetime:
    a = a + i
print('关闭平均时间:',a/10)

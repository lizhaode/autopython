# coding=gbk
# 使用paramiko库进行SSH链接和下载文件
import re
import time
import os
import paramiko
from paramiko import util


# 选择统计项目并下载相应文件
def tjchoose(choose, localpath):

    date = time.strftime('%Y%m%d%H')         # 获取当前时间来确定文件名称
    if choose == '1':
        remotepath = '/data/log/launchlog/launch.log.' + date
        localpath = localpath+'\launch.log.'+date
        sftp.get(remotepath, localpath)
        print('文件传输成功！')
        return localpath
    elif choose == '2':
        remotepath = '/data/log/launchlog/close.log.' + date
        localpath = localpath+'\lclose.log.'+date
        sftp.get(remotepath, localpath)
        print('文件传输成功！')
        return localpath
    else:
        remotepath = '/data/log/launchlog/time.log.' + date
        localpath = localpath+'\ltime.log.'+date
        sftp.get(remotepath, localpath)
        print('文件传输成功！')
        return localpath

# 统计内容过滤
def tjsearch(tjcondition, filepath):
    if os.path.exists(filepath):
        fp = open(filepath,encoding='utf-8')    # 不定义encoding win下会编码错误
        for i in fp.readlines():
            result = re.findall(tjcondition, i)
            if result != []:
                print(i)
        if result == []:
            print('未找到相应的统计内容！')
    else:
        print('文件不存在，请检查！')


# 输入服务器信息创建连接
IP = input('请输入IP（默认120.26.14.118）')
if IP == '':
    IP = '120.26.14.118'
ID = input('请输入用户名（默认root）')
if ID =='':
    ID = 'root'
Password=input('请输入密码（默认120.26的密码）')
if Password == '':
    Password = 'M4tHob1c{'
port= input('请输入端口号（默认2299）')
if port == '':
    port = 2299
# 获取统计项目
localpath = input('统计日志存放在哪个目录下:')
if not os.path.exists(localpath):                             # 创建本地存放log的路径
    os.mkdir(localpath)
util.log_to_file(localpath+'\debugssh.log')                                                      # 创建连接日志
# 开始连接
ssh = paramiko.Transport((IP, port))
ssh.connect(username=ID, password=Password)
# 创建SSH传输通道
sftp = paramiko.SFTPClient.from_transport(ssh)
if sftp:
    print('服务器连接成功！')                                         # 开始连接服务器
choose = input('请选择统计项目 1:启动 2:退出 3:时间\n')
filepath = tjchoose(choose,localpath)
# 对获取到的统计数据进行筛选
glselect = input('请输入筛选的内容:')
tjsearch(glselect, filepath)

# 关闭连接
sftp.close()

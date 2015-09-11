# coding=gbk
# 使用paramiko库进行SSH链接和下载文件
import re
import time
import os
import paramiko
from paramiko import util

# 相关数据的定义
IP = '120.26.14.118'
port = 2299
ID = 'root'
Password = 'M4tHob1c{'
choose = input('请输入要选择的统计项目，1:启动 2:退出 3:时间\n')
filterchar = '11:11:11:11:11'

util.log_to_file('/Users/lizhao/Downloads/debugssh.log')

# 开始连接
ssh = paramiko.Transport((IP, port))
ssh.connect(username=ID, password=Password)

# 创建SSH传输通道
sftp = paramiko.SFTPClient.from_transport(ssh)

# 显示服务器上指定目录的文件
# sftp.chdir(path='/data/log/launchlog/')
# path = sftp.getcwd()
# print('Current patch:', path)
# path = sftp.listdir()
# for i in path:
#     print(i)

# 下载文件
# 创建本地存放log的路径
if os.path.exists('/Users/lizhao/Downloads/launchlog/') == False:
    os.mkdir('/Users/lizhao/Downloads/launchlog/')
# 获取当前日期时间，确定要获取的文件
date = time.strftime('%Y%m%d%H')
# 选择启动、退出、时间统计
if choose == '1':
    remotepath = '/data/log/launchlog/launch.log.' + date
    localpath = '/Users/lizhao/Downloads/launchlog/launch.log.' + date
    sftp.get(remotepath, localpath)
elif choose == '2':
    remotepath = '/data/log/launchlog/close.log.' + date
    localpath = '/Users/lizhao/Downloads/launchlog/close.log.' + date
    sftp.get(remotepath, localpath)
else:
    remotepath = '/data/log/launchlog/time.log.' + date
    localpath = '/Users/lizhao/Downloads/launchlog/time.log.' + date
    sftp.get(remotepath, localpath)
# 关闭连接
sftp.close()

# 打开下载的文件
fp = open(localpath)
for i in fp.readlines():
    result = re.findall(filterchar, i)
    if result != []:
        print(result)

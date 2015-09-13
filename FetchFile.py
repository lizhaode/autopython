# coding=gbk
# 使用paramiko库进行SSH链接和下载文件
import re
import time
import os
import paramiko
from paramiko import util


# 服务器的相关信息
def getserver(IP='120.26.14.118', ID='root', Password='M4tHob1c{', port=2299):
    util.log_to_file('/Users/lizhao/Downloads/debugssh.log')

    # 开始连接
    ssh = paramiko.Transport((IP, port))
    ssh.connect(username=ID, password=Password)

    # 创建SSH传输通道
    sftp = paramiko.SFTPClient.from_transport(ssh)
    if sftp:
        print('服务器连接成功！')

# 选择统计项目并下载相应文件
def tjchoose(choose, localpath):
    date = time.strftime('%Y%m%d%H')         # 获取当前时间来确定文件名称
    if choose == '1':
        remotepath = '/data/log/launchlog/launch.log.' + date
        if sftp.get(remotepath, localpath):
            print('文件传输成功！')
    elif choose == '2':
        remotepath = '/data/log/launchlog/close.log.' + date
        if sftp.get(remotepath, localpath):
            print('文件传输成功！')
    else:
        remotepath = '/data/log/launchlog/time.log.' + date
        if sftp.get(remotepath, localpath):
            print('文件传输成功！')

# 统计内容过滤
def tjsearch(tjcondition, filepath):
    if os.path.exists(filepath):
        fp = open(filepath)
        for i in fp.readlines():
            result = re.findall(tjcondition, i)
            if result != []:
                print(i)
        if result == []:
            print('未找到相应的统计内容！')
    else:
        print('文件不存在，请检查！')

# 输入服务器信息创建连接
if input('请输入IP（默认120.26.14.118）') != '':
    IP =
ID = input('请输入用户名（默认root）')
Password=input('请输入密码（默认120.26的密码）')
port= input('请输入端口号（默认2299）')
getserver(IP,ID,Password,port)

# 获取统计项目
localpath = input('统计日志存放在哪个目录下:')
if not os.path.exists(localpath):                                # 创建本地存放log的路径
    os.mkdir(localpath)
choose = input('请选择统计项目 1:启动 2:退出 3:时间\n')
tjchoose(choose,localpath)

# 对获取到的统计数据进行筛选
glselect = input('请输入筛选的内容:')
tjsearch(glselect, localpath)

# 关闭连接
sftp.close()


# 下载文件
# 创建本地存放log的路径
# if not os.path.exists('/Users/lizhao/Downloads/launchlog/'):
#     os.mkdir('/Users/lizhao/Downloads/launchlog/')
# 获取当前日期时间，确定要获取的文件
# date = time.strftime('%Y%m%d%H')
# 选择启动、退出、时间统计
# if choose == '1':
#     remotepath = '/data/log/launchlog/launch.log.' + '2015091321'
#     localpath = '/Users/lizhao/Downloads/launchlog/launch.log.' + '2015091321'
#     sftp.get(remotepath, localpath)
# elif choose == '2':
#     remotepath = '/data/log/launchlog/close.log.' + date
#     localpath = '/Users/lizhao/Downloads/launchlog/close.log.' + date
#     sftp.get(remotepath, localpath)
# else:
#     remotepath = '/data/log/launchlog/time.log.' + date
#     localpath = '/Users/lizhao/Downloads/launchlog/time.log.' + date
#     sftp.get(remotepath, localpath)

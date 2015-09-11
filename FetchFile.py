#使用paramiko库进行SSH链接和下载文件
import paramiko

#定义服务器的地址，账号，密码
IP = '120.26.14.118'
port = 2299
ID = 'root'
Password = 'M4tHob1c{'

#开始连接
ssh = paramiko.Transport((IP,port))
ssh.connect(username=ID,password=Password)
#这句不知道是干嘛的，看paramiko的demo中有这句
sftp = paramiko.SFTPClient.from_transport(t)
#显示服务器上的目录
dirlist = sftp.listdir('.')
print('Dirlist：',dirlist)

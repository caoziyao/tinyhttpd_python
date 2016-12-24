
import socket

"""
TCP客户端:
1 创建套接字，连接远端地址
       # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()
2 连接后发送数据和接收数据          # s.sendall(), s.recv()
3 传输完毕后，关闭套接字          #s.close()
"""

HOST = '127.0.0.1'
PORT = 40001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # 定义socket类型，网络通信，TCP
s.connect((HOST, PORT))           # 要连接的IP与端口

while True:
    cmd = input("please input cmd: ")
    cmd = cmd.encode('utf-8')
    s.sendall(cmd)              # 把命令发送给对端
    data = s.recv(1024)         # 把接收的数据定义为变量
    
    print('client recv data', data)    

s.close()   #关闭连接
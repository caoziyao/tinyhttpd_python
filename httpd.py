
import socket
import threading

"""
socket编程思路
TCP服务端：
1 创建套接字，绑定套接字到本地IP与端口
   # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()
2 开始监听连接                   #s.listen()
3 进入循环，不断接受客户端的连接请求              #s.accept()
4 然后接收传来的数据，并发送给对方数据         #s.recv() , s.sendall()
5 传输完毕后，关闭套接字                     #s.close()

TCP客户端:
1 创建套接字，连接远端地址
       # socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()
2 连接后发送数据和接收数据          # s.sendall(), s.recv()
3 传输完毕后，关闭套接字          #s.close()
"""

def log(*argv, **kwargs):
    """
    格式化输出
    """
    print(*argv, **kwargs)

def startup(host, port):
    """
    初始化服务器 socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 定义socket类型，网络通信，TCP
    s.bind(host, port)  # 套接字绑定的IP与端口
    s.listen(5)         # 开始TCP监听


def accept_request(conn, addr):
    """
    处理客户端请求
    """
    print('thread is running', threading.current_thread().name)
    #while True:
    # print(conn, addr)
    while True:
        data = conn.recv(1024)
        if len(data) < 2:
            break
        print('server data', data)
        # status, result = 
        conn.sendall(data)

def main():
    """
    开始函数，初始化 socket
    """
    server_socket = -1
    port = 40001
    host = '127.0.0.1'
    client_socket = -1

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 定义socket类型，网络通信，TCP
    server_socket.bind((host, port))  # 套接字绑定的IP与端口
    server_socket.listen(5)         # 开始TCP监听

    while True:
        conn, addr = server_socket.accept()     #接受TCP连接，并返回新的套接字与IP地址
        print('Connected by', addr)

        # 接受TCP链接后，开一个线程处理
        t = threading.Thread(target=accept_request, args=(conn, addr, ))
        t.start()
        t.join()
        print('end threading')

main()
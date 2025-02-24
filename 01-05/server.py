# socket 反复连接
# https://blog.51cto.com/u_15726470/10131125

import socket

# 创建一个TCP/IP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定套接字到一个端口
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# 开始监听传入的连接
sock.listen(1)

while True:
    # 等待连接
    print('waiting for a connection')
    try:
        connection, client_address = sock.accept()
    except KeyboardInterrupt:
        print('server terminated')
        break
    except Exception as e:
        print('error accepting connection:', e)
        continue

    try:
        print('connection from', client_address)
        
        # 接收数据
        data = connection.recv(1024)
        print('received {!r}'.format(data))

        # 发送数据
        print('sending data back to the client')
        connection.send(b"HTTP/1.1 200 OK\r\n\r\nHello, World!")

    finally:
        # 关闭连接
        connection.close()
        
# 关闭套接字
sock.close()

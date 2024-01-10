import socket

Host = "127.0.0.1"
port = 9997

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""

s.connect(("www.qdu.edu.cn", 80))  # 里层括号为了传入'address:port'
s.send(b"GET / HTTP/1.1\r\nHost: www.qdu.edu.cn\r\nConnection: close\r\n\r\n")
"""
s.sendto(b"send by client", (Host, port))

"""
这么写，跟recvfrom相比，就需要在数据中单独传送地址

buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b"".join(buffer)
"""
buffer, addr = s.recvfrom(8192)
s.close()
print(buffer)  #
"""
header, body = data.split(b"\r\n\r\n", 1)
print(header.decode("utf-8"))
with open("qdu.html", "wb") as f:
    f.write(body)
"""

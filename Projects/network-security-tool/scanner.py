import socket

target = "127.0.0.1"

port = 80 #can i connect to port 80 on 127.0.0.1

s = socket.socket() #creates networking tool

try:
    s.connect((target, port)) #tells it where to connect
except Exception:
    print("PORT IS CLOSED")
else:
    print("PORT IS OPEN")
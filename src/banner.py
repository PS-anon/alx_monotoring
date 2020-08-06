import argparse
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument("--host", metavar="", dest="host", default="localhost", help="Name of host for database.  Default is 'localhost'.")
args = parser.parse_args()
ports = [22, 80 ,443]
host =  args.host
print(host)
sock.connect((host,80))
sock.send('GET HTTP/1.1 \r\n')
ret = sock.recv(1024)
print '[+]' + str(ret)

f= open("banner.txt","a")
f.write(ret)
f.close() 
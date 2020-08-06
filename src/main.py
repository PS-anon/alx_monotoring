from fuzzer import resp
from port_scan import p_scan
import os
import socket

print ("https://github.com/danielmiessler/SecLists/tree/master/Fuzzing -- wordlist")
a = input("Hey , website (www.example.com)~> ")
print("website ~> " + a)
b = "https://" + a
ip =  socket.gethostbyname(a)
print("ip ~>" + ip)
bn = "[ ]" * 20
print("Starting ! \n [+] \n" + bn)
resp(b)
p_scan(b)
os.system("python2 banner.py --host " + ip)
print("Open main.html to see your results ! Thanks!")
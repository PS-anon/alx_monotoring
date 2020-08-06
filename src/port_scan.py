import threading
import socket
#inspired by https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
def p_scan(target):
  def portscan(port):

      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(0.5)# 

      try:
          con = s.connect((target,port)) 
          f= open("p_scan_res.txt","a")
          f.write("\nOpen ~> " + str(port))
          f.close()  
          con.close()

      except: 
          pass
  r = 1 
  for x in range(1,100): 

      t = threading.Thread(target=portscan,kwargs={'port':r}) 
      r += 1     
      t.start()

#p_scan(target)
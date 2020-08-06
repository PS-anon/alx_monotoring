import urllib.request
import urllib.error
import sys
def resp(url):
        with open('fuzz.txt','r') as file:
                words = file.read().splitlines()
        for i in words:
                f_url = url + i
                print("~>" + f_url)
                try :
                  response = urllib.request.urlopen(f_url)
                  print(response.getcode())
                  a = response.getcode()
                  if a == 200 :
                    c = open("results_fuzz.txt", "w")
                    c.write("")
                    c.close
                    f= open("results_fuzz.txt","a")
                    f.write("\n(200)Exists ~> " + f_url )
                    f.close() 

                except KeyboardInterrupt:
                  sys.exit()
                except :
                  continue


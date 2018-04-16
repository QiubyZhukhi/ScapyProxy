import re
import requests
import sys
import socket
from threading import Thread
import os
import time
reload(sys)
str.title("SCRAPY PROXY")
sys.setdefaultencoding('utf8')
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
os.system("clear")

#LOG
file = "/storage/emulated/0/a/log.txt"
host = "ping.eu"
timeout = 3 #3 detik
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(9./90)
slowprint("""
	Author: """+R+
		"""QIUBY """+W+
			"""ZHUKHI"""+O+
				"""\n\t-= [PBM] =- TEAM"""+W+"""\nThanks To: """+C+
					"""Ibnu Wahyudi"""+W+GR+
						"""\nand All Member Pys60""")

cek = requests.session()
url = "https://www.sslproxies.org/"
print "--- MENGUNJUNGI SITE ---"
print url
page = cek.get(url).text

def pepong():
    print "\n--- Mencari Proxy:Port ---"
    dic = {}
    proxy = re.findall(r"\d+\.\d+\.\d+\.\d+",page)
    port = re.findall(r"\**<td>\d+</td>", page)
    print "--- Proxy Di Temukan ---"
    for i in range(len(proxy)):
        ports = port[i].replace("<td>", "").replace("</td>", "")
        print B+proxy[i]+":"+str(ports)+W
        dic.update({proxy[i]:str(ports)})        
    return dic
pepong = pepong()
threading = []
print "\r\n--- Analisa Proxy ---"

def TES(proxy, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    sock.connect((proxy,port))
    sock.sendall("CONNECT %s HTTP/1.0\r\nProxy-Authorization: Basic\r\nencoded-credentials\r\n\r\n" %(host))
    reps = sock.recv(1080).split("\n")[0]
    if reps:
        print C+reps+W
        save = open(file, "a+")
        save.write("%s:%s %s\n" % (proxy,port,reps))
if __name__ == "__main__":
    for proxy,port in pepong.items():
        print O+proxy,port+W
        try:
            threading.append(Thread(target=TES(str(proxy),int(port)), args=(proxy,port)))                  
        except socket.timeout, e:
            print e
        except socket.error, e:
            print e
    for i in threading:
        i.start()            
    print "Selesai"

''':'
python3 $0 $@
exit
':'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.request import urlopen as u
from urllib.parse import unquote as uqu
from sys import argv
from json import loads as l
import os
import random

def dlistdir(q):
 return [w for w in os.listdir(q) if w != '...']
os.chdir('/'.join(argv[0].split('/')[:-1]))
os.system('rm exit')
a=l(open('0/...').read())
for w in list(a.keys()):
 if not os.path.exists(w):
  del(a[w])
 elif a[w] != os.path.getsize(w):
  del(a[w])
  os.remove(w)
for w in dlistdir('../0f/'):
 if os.path.isfile(w):
  a[w]=os.path.getsize(w)
open('0/...','w').write(str(a).replace("'",'"'))

q=[w.split() for w in os.popen('ifconfig').read().split('\n')]
q=[w[1] for w in q if len(w) and w[0] == 'inet']
q=[w[([int(ww in '1234567890') for ww in w]+[1]).index(1):] for w in q]
q=[w[:([int(ww not in '1234567890.') for ww in w]+[1]).index(1)] for w in q]
print('='*10,*enumerate(q),sep='\n')
if len(argv) > 1:
 argv1=argv[1]
 if argv1 in [w[:len(argv1)] for w in q]:
  q=[w for w in q if w[:len(argv1)] == argv1]
print('='*10,*enumerate(q),sep='\n')
if len(argv) > 2:
 port=int(argv[2])
else:
 port=9000
if len(q) > 1:
 e=int(input())
else:
 e=0
q=q[e]
hostName = q
hostPort = port
def exex():
 global hostName
 global hostPort
 #print(1234)
 #port=os.system('echo "123" && ./fileserverstarter '+hostName+' '+str(hostPort))
 #print('='*2)
 port=os.popen('./fileport.py '+hostName+' '+str(hostPort)+' 0').read().split('='*9)[-1][1:]
 #print('='*3,port)
 return port[:-1]
class MyServer(BaseHTTPRequestHandler):
 def do_GET(self):
  if os.path.exists('hexit'):
   raise KeyboardInterrupt
  if self.path=='/favicon.ico':
   pass
  else:
   if os.path.exists('exit'):
    raise KeyboardInterrupt
   #print('start')
   self.send_response(200)
   path=uqu(self.path)
   #print(path)
   global hostName
   global hostPort
   global exex
   port=exex()
   #print(hostPort,hostName)
   #print(1)
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   #print(":"*8,port,path)
   self.wfile.write(bytes('''
   <html>
   <head>
   <meta http-equiv="refresh" content="1;URL=http://'''+hostName+':'+port+'''/0/">
   </meta>
   </head>
   </html>''', "utf-8"))

st=1
while st:
 try:
  myServer = HTTPServer((hostName, hostPort), MyServer)
  st=0
 except:
  hostPort+=1
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass
os.system('touch exit')
myServer.server_close()
print()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

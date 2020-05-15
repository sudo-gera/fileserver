''':'
python3 $0 $@
exit
':'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.request import urlopen as u
from urllib.parse import unquote as uqu
from sys import argv
import os
import random

def dlistdir(q):
 return [w for w in os.listdir(q) if w != '...']
os.chdir('/'.join(argv[0].split('/')[:-1]))
q=[w.split() for w in os.popen('ifconfig').read().split('\n')]
q=[w[1] for w in q if len(w) and w[0] == 'inet']
q=[w[([int(ww in '1234567890') for ww in w]+[1]).index(1):] for w in q]
q=[w[:([int(ww not in '1234567890.') for ww in w]+[1]).index(1)] for w in q]
#q=[w[1].split(':')[1] for w in q if len(w) and w[0] == 'inet']
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
ngrok='0'
if len(argv)>3:
 ngrok=argv[3]

class MyServer(BaseHTTPRequestHandler):
 def do_GET(self):
  pass
 def do_POST(self):
  pass
st=1
hostPort+=1
while st and hostPort < 70000:
 print(hostPort)
 try:
  myServer = HTTPServer((hostName, hostPort), MyServer)
  st=0
 except:
  hostPort+=1
myServer.server_close()
os.system('./fileserver.py '+hostName+' '+str(hostPort)+' "'+random.choice(os.listdir('nekopara'))+'" '+ngrok+' > log &')
print('='*9,hostPort)

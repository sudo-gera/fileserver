''':'
python3 $0 $@
exit
':'''
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.request import urlopen as u
from urllib.parse import unquote as uqu
from json import loads as l
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
if len(argv) > 3:
 img='/nekopara/'+argv[3]
else:
 img='/nekopara.jpg'
q=['0.0.0.0']
if len(q) > 1:
 e=int(input())
else:
 e=0
ngrok=1
if len(argv) > 4:
 ngrok=int(argv[4])
q=q[e]
hostName = q
hostPort = port
admin=0

def exex():
 global hostName
 port=os.popen('./fileport.py '+hostName+' '+str(hostPort)+' 2').read().split('='*9)[-1][1:-1]
 return port
class MyServer(BaseHTTPRequestHandler):
 def do_GET(self):
  if os.path.exists('exit'):
   raise KeyboardInterrupt
  global admin
  self.send_response(200)
  path='.'+uqu(self.path)
  if path =='./0/0/' and admin==1:
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes('''
   <html>
   <head>
   <title>'''+path+'''</title>
   </head>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <body>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>

   <div id="main">
   <h1><wi>Enter password</wi></h1>

   <wi><form method="post">
   <textarea name="a"></textarea><br>
   <input type="submit" value="enter"></form></wi>
   <wi>===</wi>

   <form><button formaction="../">
   <h1>..<img src="/favicon.ico" height="25"></h1>
   </button></form>
   <wi>===</wi>

   </div></body></html>''', "utf-8"))
   return None

  if '?' in path:
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes('''
   <html>
   <head>
   <meta http-equiv="refresh" content="0;URL=.">
   </meta>
   </head>
   <body>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>
   </body>
   </html>''', "utf-8"))

  elif path in ['./','.']:
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes('''
   <html>
   <head>
   <meta http-equiv="refresh" content="1;URL=0/">
   </meta>
   </head>
   <body>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>
   </body>
   </html>''', "utf-8"))

  elif os.path.isdir(path):
   if img == '/nekopara.jpg':
    os.system('pwd')
    os.system('cp nekopara/'+random.choice(os.listdir('./nekopara'))+' nekopara.jpg')
   a=open('clip')
   clip=a.read()
   a.close()
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes('''
   <html>
   <head>
   <title>'''+path+'''</title>
   </head>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <body>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>

   <div id="main">
     ''','utf-8'))
   if path == './0/':
    self.wfile.write(bytes('''
    <h1>
     <form enctype="multipart/form-data" method="post" name="sendfile">
      <wi>
       <input type="file" name="u">
       <inp id="inp">
        <input type="submit">
       </inp>
      </wi>
     </form>
    </h1>
    <div id="log"></div>
    <wi>===</wi>

   <script>
    document.forms.sendfile.onchange=function(){
     var file=this.elements.u.files[0]
     if (file) {
      document.getElementById('maincont').innerHTML=''
      document.getElementById('inp').innerHTML=''
      x=new XMLHttpRequest();
      x.upload.onprogress=function(){
       if (event.loaded!=event.total){
        document.getElementById('log') .innerHTML='<wi>'+event.loaded+'<br/>'+event.total+'</wi>'
        }
       else{
        location.reload(true)
       }
      }
      x.open("POST",'.')
      var a=file.name
      var e=''
      var w=0
      for (w=0;w<a.length;w+=1){
       e+=a.charCodeAt(w).toString()+'a'
      }
      x.setRequestHeader("fn",e)
      x.send(file)
     }
    }
   </script>

     ''','utf-8'))
   self.wfile.write(bytes('''
   <maincont id="maincont">

     ''','utf-8'))
   if path == './0/':
    self.wfile.write(bytes('''

   <wi><form method="post">
   <textarea name="c">'''+clip+'''</textarea><br>
   <input type="submit" value="save"></form></wi>
   <wi>===</wi>

   ''','utf-8'))
   self.wfile.write(bytes('''
   <form><button formaction="../">
   <h1>..<img src="/favicon.ico" height="25"></h1>
   </button></form>
   <wi>===</wi>
   ''','utf-8'))
   if admin==2:
    self.wfile.write(bytes('''
   <form method="post"><button formaction="/0/" name="e" value="1">
   <h1>exit</h1>
   </button></form>
   <wi>===</wi>
   ''','utf-8'))

   ld=list(dlistdir(path))
   ld=ld[::-1]
   for w in ld:
    self.wfile.write(bytes('''
    <form><button formaction="'''+w+'''/">
    <h1>'''+w+'''
    <img src="/favicon.ico" height="25">'''*int(os.path.isdir(path+w))+'''
    </h1></button></form>''','utf-8'))

   self.wfile.write(bytes('''</maincont></div></body></html>''', "utf-8"))

  elif os.path.isfile(path):
   if ngrok or path[:4]!='./0/':
    q=open(path,'br')
    di=l(open('0/...').read())
    if path in di.keys():
     tosend=l(open('0/...').read())[path]
     toread=0
     self.send_header("Content-type", "file/file")
     self.send_header("Content-Length", str(tosend))
     self.end_headers()
     while toread<tosend:
      read=q.read()
      self.wfile.write(read)
      toread+=len(read)
    else:
     self.send_header("Content-type", "file/file")
     self.send_header("Content-Length", str(os.path.getsize(path)))
     self.end_headers()
     self.wfile.write(q.read())
    if ngrok == 2:
     raise KeyboardInterrupt
   else:
    self.send_response(200)
    global hostName
    global hostPort
    global exex
    port=exex()
    self.send_header("Content-type", "text/html; charset=utf-8")
    self.end_headers()
    self.wfile.write(bytes('''
   <html><head><title>'''+path+'''</title>
   <meta http-equiv="refresh" content="1;URL=http://'''+hostName+':'+port+path[1:]+'''"></meta>
   </head>
   <body>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>
   <div id="main">
   <h1>
   <form><button formaction="./">..<img src="/favicon.ico" height="25"></button>
   </form>
   </h1>
   </div></body></html>
   ''', "utf-8"))
  elif os.path.isfile(path[:-1]) and path[-1] == '/':
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes('''
   <html><head><title>'''+path+'''</title>
   </head>
   <body>
   <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
   <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>
   <div id="main">
   <h1>
   <form><button formaction="../">..<img src="/favicon.ico" height="25"></button>
   </form>
   <wi><br>'''+path[1:-1]+'<br>size:'+str(os.path.getsize(path[:-1]))+'''</wi><br>
   </h1>
   <a href="'''+path[1:-1]+'''"><img src='/download.png' width=100%></a><br>
   </div></body></html>
   ''', "utf-8"))
  else:
   self.send_header("Content-type", "text/html; charset=utf-8")
   self.end_headers()
   self.wfile.write(bytes("<html><head><title>"+path+"</title></head>", "utf-8"))
   self.wfile.write(bytes('<body><p>not found<br>'+path[1:]+'</p></body></html>', "utf-8"))

 def do_POST(self):
  global admin
  lenn=int(self.headers['Content-Length'])
  ct=self.headers['Content-Type']
  ct=str(ct).split('/')
  o=ct[1:]
  ct=ct[0]

  print(self.headers)
  if ct=='multipart':
   blen=len(o[0].split('=')[1])+8
   if 1:
    data=bytearray()
    while data[-4:]!=bytearray('\r\n\r\n','utf-8'):
     data+=self.rfile.read(1)
     lenn-=1
    toread=lenn-blen
    fn=uqu(data.decode().replace('+',' ')).split('filename',1)[1].split('"')[1]
    file=fn
    fn='.'+self.path+file
    tosave=0
    while os.path.exists(fn):
     tosave+=1
     fn='.'+self.path+str(tosave)+file
    a=l(open('0/...').read())
    a[fn]=toread
    open('0/...','w').write(str(a).replace("'",'"'))
    open(fn,'w').close()
    a=open(fn,'ab')
    rsize=1024
    while toread>0:
     read=min(toread,rsize,102400)
     toread-=read
     ti=time.time()
     a.write(self.rfile.read(read))
     rsize=int(min(rsize/(time.time()-ti)+1,2**22))
    self.rfile.read(blen)
  elif self.headers['fn']:
   name=self.headers['fn']
   name=name[:-1].split('a')
   name=[chr(int(w)) for w in name]
   name=''.join(name)
   if 1:
    toread=lenn
    file=name
    fn='.'+self.path+file
    tosave=0
    while os.path.exists(fn):
     tosave+=1
     fn='.'+self.path+str(tosave)+file
    a=l(open('0/...').read())
    a[fn]=toread
    open('0/...','w').write(str(a).replace("'",'"'))
    open(fn,'w').close()
    a=open(fn,'ab')
    rsize=1024
    while toread>0:
     read=min(toread,rsize,102400)
     toread-=read
     ti=time.time()
     a.write(self.rfile.read(read))
     rsize=max(int(min(rsize/(time.time()-ti),2**22)),1)
  else:
    data=self.rfile.read(lenn)
    data=data.decode().replace('+',' ')
    data=uqu(data)
    dec,data=data.split('=',1)
    if dec=='c':
     open('clip','w').write(data)
    if dec=='a':
     s=' '.join(time.asctime().split(':')).split()
     s0=str((int(s[2])+int(s[4]))%100)+s[3][-1]
     print(s0)
     a1='qwertyuiop'
     a2='asdfghjkl1'
     a3='zxcvbnm098'
     s1=a1[int(s0[0])]
     s2=a2[int(s0[1])]
     s3=a3[int(s0[2])]
     pas=(s1+s2+s3)*((int(s[3][-1])+int(s[4][-1]))//3+1)
     print(pas)
     if data==pas:
      admin=2
    if dec=='e':
     admin=1

  self.send_response(200)
  self.send_header("Content-type", "text/html; charset=utf-8")
  self.end_headers()
  self.wfile.write(bytes('''
     <html>
     <head>
    <meta http-equiv="refresh" content="1;URL=.">
    </meta>
    </head>
    <body>
    <style type=text/css>
    #neko {position: fixed; top:0; botom:0; left:0; right:0}
    #main {position: absolute; top:0; left:0}
    wi {background: #00ff00}
    </style>
    <div id="neko">
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"><br>
    <img src="'''+img+'''" width="100%"></div>
    </body>
    </html>
    ''', "utf-8"))

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

myServer.server_close()
print()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

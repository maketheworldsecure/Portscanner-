# *******PROGRAM TO FIND OPEN PORT*********
#*******(c)Deepakkrishnan**********

#! /usr/bin/python

import socket
from socket import gethostbyname
print("""
======================================================================================
__________              __      _________
\______   \____________/  |_   /   _____/ ____ _____    ____   ____   ___________
 |     ___/  _ \_  __ \   __\  \_____  \_/ ___\ \__  \  /    \ /    \_/ __ \_  __
 |    |  (  <_> |  | \/|  |    /        \  \___ / __ \|   |  |   |  \  ___/|  | \/
 |____|   \____/|__|   |__|   /_______  /\___  (____  |___|  |___|  /\___  |__|
                                      \/     \/     \/     \/     \/     \/
                    Developed By:Deepak Krishnan
                    Version :1.0
======================================================================================
""")
TargetName = raw_input("Enter the Host name EG:WWW.GOOGLE.COM : ")
TargetIp = gethostbyname(TargetName)
TargetPort = int(raw_input("Enter the port to scan <Between 1 to 65535>: "))
print ("===================================================================")
print ("$$$$$$$ port scan started on :"+TargetIp+" $$$$$$$")
print ("===================================================================")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def PortScan(TargetIp,TargetPort):
    try :
        s.connect((TargetIp,TargetPort))
        s.send("port scanner")
        response=s.recv(1024)
        return True
    except :
        return False

if PortScan(TargetIp,TargetPort):
    print ("Yes!!The port is open")
else:
    print ("Oops!!closed port")
    s.close()

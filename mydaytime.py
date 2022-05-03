
import socket
import sys
from datetime import datetime



# define your variables here
PORT = 13
hostname = sys.argv[1]

# check that there are enough parameters
if (len(sys.argv) != 2):
  print("Usage: mydaytime <hostname>")
  sys.exit()

# Write your code here
try:
	IP = socket.gethostbyname_ex(hostname)
	IP = IP[2]
	IP = ''.join(map(str,IP))
	soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	soc.settimeout(3)
	connection = soc.connect_ex((IP,PORT))
	if connection == 0:
		time = soc.recv(1024)
		if(time == None):
			print("Server exists and connects on port 13 but doesn't send time")
		else:
			print("Time received from server is %s" %time.decode("ascii"))
	else:
		print("Server doesn't connect on port 13(not running daytime)")
	
	soc.close()
except:
	print("Bogus hostname: server cannot be contacted")


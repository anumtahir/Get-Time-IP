import socket
import sys

# define your variables here

hostname = sys.argv[1]

# check that there are enough parameters
if (len(sys.argv) != 2):
  print("Usage: mydaytime <hostname>")
  sys.exit()

# Address resolution stage by using gethostbyname_ex()
# Write your code here!

try:
	a = socket.gethostbyname_ex(hostname)
	a = a[2]
	# Print to standard output
	if(len(a)>1):
		for el in a:
			b = ''.join(map(str,el))
			print(b)
	else:
		b = ''.join(map(str,a))
		print(b)
except:
	print("Wrong hostname")

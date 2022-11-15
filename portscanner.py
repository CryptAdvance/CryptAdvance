from socket import *
class PortScanner():
	def POrtScanner(self,input_from_user):
		r=1
		while r==1:
			import socket
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(5)
			a=input("Port Scanner\nEnter the IP Address for which you want to check if the port is open: \n")
			b=int(input("Enter the port number for which you want to check if it is open or not: "))
			def portSCanner(b):
				if s.connect_ex((a,b)):
					print("The port is closed")
				else:
					print("The port is open")
			portSCanner(b)
			

		else:
			r=2

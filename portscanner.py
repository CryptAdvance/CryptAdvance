from socket import *
class PortScanner():
	def POrtScanner(self,input_from_user):
		r=1
		while r==1:
			#a=input("Enter the IP Address for which you want to check if the port is open: \n")
			#b=input("Enter the port number for which you want to check if it is open or not: ")
			def connectionScan(targetHost, targetPort):
				try:
					connect_t=socket(AF_INET,SOCK_STREAM)
					connect_t.connect((targetHost, targetPort))
					print('[+] %d/tcp open'% targetPort)
					connect_t.close()
					with open('portstatus.txt','w') as file:
						file.writelines(str(targetPort)+"/tcp is open \n")
					
				except:
					print('[-] %d/tcp closed'% targetPort)
					connect_t.close()
					with open('portstatus.txt','w') as file:
						file.writelines(str(targetPort)+"/tcp is closed\n")
			r=2
				
			def portScan(targetHost, targetPorts):
				try:
					targetIP=gethostbyname(targetHost)
				except:
					print("[-] Cannot resolve %s"% targetHost)
					return
				try:
					targetName=gethostbyaddr(targetIP)
					print('\n[+] Scan result of: %s '% targetName[0])
				except:
					print("\n[+] Scan result of: %s "% targetIP)
				setdefaulttimeout(1)
				for targetPort in targetPorts:
					print("Scanning Port: %d "% int(targetPort))
					connectionScan(targetHost, int(targetPort))
			portScan("google.com",[80,22])

		else:
			r=2
#https://www.youtube.com/watch?v=bH-3PuQC_n0&list=PLR0bgGon_WTIjs0lyCAUp3v1qAraXCJcH
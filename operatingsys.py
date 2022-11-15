class OperatingSys():
	def OPeratingSys(self,input_from_user):
		import platform
		my_os=platform.system()
		with open('myOS.txt','w') as file:
			file.writelines(str(my_os))
		with open('myOS.txt','r') as file:
			lines=file.read()
			first=lines.split('\n',1)[0]
			print(first)
			if(first=='Windows'):
				import os
				os.system('cls')
			else:
				import os
				os.system('clear')
		r=1
		while r==1:
			a=input("Know Your Operating System\nDo you want to know your Operating System (Y/N)")
			if(a=='Y'):
				import platform
				my_os=platform.system()
				with open('myOS.txt','w') as file:
					file.writelines(str(my_os))
				with open('myOS.txt','r') as file:
					lines=file.read()
					first=lines.split('\n',1)[0]
					print("Your Operating System is "+first)
			r=2

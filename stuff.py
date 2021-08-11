#AUTHOR = wh1t3-h4t
from time import *
from os import *

def bit_stuffing(data): #Stuffing
	c = 0
	data_list = list(data)
	for i in range(len(data_list)+1):
		try:
			if data_list[i]=='1':
				c+=1
				if c==5:
					data_list.insert(i+1, '0')
					c = 0
				continue
			else:
				c = 0
		except IndexError:
			break
	data_list.append('0')
	return ''.join(data_list)
	
def bit_destuffing(data): #De-stuffing
	c = 0
	data_list = list(data)
	del data_list[-1] 
	for i in range(len(data_list)): 
		try:
			if data_list[i]=='1': 
				c+=1 
				if c==5: 
					del data_list[i+1] 
					#print(data_list) #uncomment for debugging
					c = 0 
				continue
			else:
				c = 0
		except IndexError:
			break
	return ''.join(data_list)
	
print(get_terminal_size())
print("Recommended size: 80 x 24 or greater!")
sleep(3)
if uname().sysname == "Linux":
	system('clear')

print("""
███████╗████████╗██╗   ██╗███████╗███████╗   ██████╗ ██╗   ██╗
██╔════╝╚══██╔══╝██║   ██║██╔════╝██╔════╝   ██╔══██╗╚██╗ ██╔╝
███████╗   ██║   ██║   ██║█████╗  █████╗     ██████╔╝ ╚████╔╝ 
╚════██║   ██║   ██║   ██║██╔══╝  ██╔══╝     ██╔═══╝   ╚██╔╝  
███████║   ██║   ╚██████╔╝██║     ██║     ██╗██║        ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝     ╚═╝╚═╝        ╚═╝   

""")	
sleep(1)
data = ""
while len(data)!=16:
	data = input("Enter 16-bit data: ")

stuffed_data = bit_stuffing(data)
print("Stuffed data: {}".format(stuffed_data))
print("De-stuffed data: {}".format(bit_destuffing(stuffed_data)))

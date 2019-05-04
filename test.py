from scapy.all import *

print("This is Xmas Scanner")
ipt = str(input("Please enter the target ip: "))
start = int(input("Please enter the start of ports range: "))
end = int(input("Please enter the end of ports range: "))+1
output = {}
for i in range(start, end):
	s= sr1(IP(dst=ipt)/TCP(dport=i, flags="FPU"),timeout=1)
	if (str(type(s))=="<class 'NoneType'>"):
		output[i] = "opened"
	else:
		output[i] = "closed"


print("Ports are:")
		
for k,v in output.items():
    print(k, v)
		

		
		
		
		
		



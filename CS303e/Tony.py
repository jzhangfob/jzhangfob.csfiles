for r in range (8, -1, -1):    
	for c in range(r):
		print('*', end="")      
	print()
for r in range(8):
	for c in range(r + 1):
		print('*', end = '')
	print ()
	
list = [4,5,6,7,1,2]

for i in range(len(list)):
	print (i)
	
print()
for i in list:
	print (i)
	
	
flag = 'True'

list = [1,2,3,4, -1, 4,5]


#Flags are used to validate input; once a condition is met it will break out of a loop depending on which loop has the 'flag =' condition tied to it

i = 0
while i < len(list):
	print (i)
	while flag == 'True':
		if list[i] < 0:
			flag = 'False' 
	i += 1

def accept_string(num, list):
	list.append(num)
	return list 


def main():
	
	
	list = []
	yolo = accept_string(2, list)
	print (yolo) 
#Return will not print in main unless you print(yolo)
#If print function is in accept_string, then it will print with yolo = accept_string(2, list), another print(yolo) is unnecessary 
			
main()
	


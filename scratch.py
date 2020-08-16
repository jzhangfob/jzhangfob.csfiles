
def main():
	#Split() will split the string into pieces into a list. It splits based off what is the parameter. 
	#If string is entirely the split parameter, will output a list of length (num characters + 1)  
	dude = '1234-2625-473-'
	a = dude.split('-') #    ['', '', '', '', '']
	b = dude.split('dog')#   ['    ']
	
	
	print (a)
	print (b)
	#Messing with round function 
	print (round(-.6)) # -1 
	print (round(-.5)) # 0
	print (round(.5))  # 0
	print (round(.6))  # 1
	print (round(-2.3)) # -2
	print (round(-2.5)) # -2
	print (round(-2.9)) # -3
	print (round (-2.500001)) #-3
	print (round(-2.5234, 4)) #-2.5234
	print (round(-2.5236, 3)) #-2.524 
	print (round(-2.5235, 3)) #-2.523 
	
	#how to left justify 
	print ("\"%-10s\" is a really cool person" %('Johnny')) #"Johnny    " is a really cool person 
	print ("%-8.4f yo" %(-5.52566)) #-5.5257  yo 
	list = [4,5,6,7]
	for x in list:
	  print (x)
	  
	  
	list = [1,2,3,4,2,2]
	yes = [2,2]
	if yes in list:
		print ('True') 
	else:
		print ('yo')
		
	for r in range (8, -1, -1):    
		for c in range(r):
			print('*', end="")      
		print()
	
	for r in range(8):
		for c in range(r + 1):
			print('*', end = '')
		print ()
	
	for c in range(4, -1, -1,):
		print (c)
	
	for i in range(0, 3):
		for j in range(i): 
			print ("*", end = '')
	for i in range(1):
		for j in range(i):
			print ("*", end = '')
	
	print()
	print (str)
	list = ["1", "2", "3", "4"]
	for i in range(len(list)):
		list[i] = int(list[i])
	print (list)
	a = '10'
	a = int(a)
	print (a)
	
	
	
main()
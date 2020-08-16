import random
'''
for i in range(1): 
	print (i) #0
'''
#Determine sum of products of each corresponding element between 2 lists 
def products(list1, list2):
	sum = 0
	for i in range(len(list1)):
		product = list1[i] * list2[i]
		sum += product 
	return sum 
	
#Function that will determine if a list is already in ascending order 
def is_ascending(list):
	copy = list[:]
	true_list = []
	min = list[0]
	while len(copy) != 0:
		min = copy[0]
		for i in range(len(copy)):
			if copy[i] <= min:
				min = copy[i]
		true_list.append(min)
		copy.remove(min)
	if true_list == list:
		return True
	return False 

#Sort a list in ascending order (length 3) without using loops or sort 
def no_loops_ascending(list):
	new_list = []
	copy = list[:]
	minn = min(copy)
	new_list.append(minn)
	copy.remove(minn)
	minn = min(copy)
	new_list.append(minn)
	copy.remove(minn)
	new_list.append(copy[0])
	list = new_list[:]
	return list

#Shuffle contents of a list
def list_randomizer(lst):
	result = []
	while len(lst) > 0:
		index = random.randrange(0,len(lst))
		result.append(lst[index])
		lst.remove(lst[index])
	return result
	
#Find largest product of 2 adjacent numbers 
def largest_adj(list):
	prod_list = []
	for i in range(0, len(list) - 1):
		product = list[i] * list[i + 1]
		prod_list.append(product)
	return max(prod_list)
			
#Figure out if a string is palindromic 			
def pal_string(string):
	string = str(input("Enter a string: "))
	for i in range(len(string)):
		if string[i] != string[-1 - i]:
			return False 
	return True 

#String rotation 
def string_rotate(string, n):
	string = str(input("Enter a string: "))
	rotations = n % len(string)
	
	sliced = string[-rotations: ]
	new_string = sliced + string 
	new_string = new_string[:len(string)]
	return new_string 

def in_file(file_name, substring):
	counter = 0
	for line in file_name:
		counter += line.count(substring)
	return counter 
	
def forbidden_list(file_name, forb_list):
	for line in file_name: 
		for ch in forb_list:
			if ch in line:
				return False 
	return True 

def five_list(list):
	list2 = list[:]
	while len(list2) > 0:
		j = 0
		while j < 5:
			if len(list2) == 0:
				break
			print (list2[0], end = ' ')
			list2.remove(list2[0])
			j += 1
		print()

def show_line(file):
	counter = 1
	for line in file:
		if 'yolo' in line:
			print(counter, line.rstrip())
		counter += 1

def swap_file(file):
	outfile = open('outfile.txt', 'w')
	for line in file:
		if 'yolo' in line:
			outfile.write(line.replace('yolo', 'haha'))
		else:
			outfile.write(line)
	outfile.close()

def ch_pairs(string):
	counter = 0
	for i in range(0, len(string), 2):
		if (i == len(string) - 1 or i == len(string) - 2):
			break 	
		if ord(string[i]) == ord(string[i+1]):
			counter += 1
	return counter 
		
	
	
		
	
		
	
	
		
			

	

def main():
	'''
	list = [2,3,1]
	a = no_loops_ascending(list)
	print (a)
	
	list2 = [1,2,3,4,5]
	b = list_randomizer(list2)
	print (b)
	
	#Largest_adj
	list3 = [4,5,1,2,3]
	c = largest_adj(list3)
	print (c)
	
	#Palindromic string 
	d = ''
	print (pal_string(d))
	
	#String rotate function
	e = ''
	print (string_rotate(e, 10))
	
	infile = open("test.txt", "r")
	print (in_file(infile, 'yolo'))
	
	infile = open("test.txt", "r")
	forb_list = ['frag']
	print (forbidden_list(infile, forb_list))
	
	infile = open("test.txt", "r")
	
	
	swap_file(infile)
	
	#five to a line 
	f = [1,2,3,4,5]
	print (five_list(f))
	'''
	print (ch_pairs('ppreeetti'))
	
	print (no_loops_ascending([7,6,5]))
	
	
	
	
	
	
	

main()
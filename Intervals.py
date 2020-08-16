#  File: Intervals.py

#  Description: Create a program that will output merged intervals so that there are no longer any overlapping intervals 

#  Student Name: Jonathan Zhang

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/19/2016
 
#  Date Last Modified: 4/19/2016 
	
	
	

def main():
	#Open the file for reading 
	infile = open("intervals.txt", "r")
	#Initialize the list that will hold each pair of numbers in a tuple
	list = []

	#First, add each line to the file unformatted 
	for line in infile: 
		list.append(line)
	#Next, take out the white space characters and split each pair of numbers into a list 
	for i in range(len(list)):
		list[i] = list[i].rstrip()
		list[i] = list[i].split(' ')
		#Convert strings into integers 
		for j in range(len(list[i])):
			list[i][j] = int(list[i][j])
		#Turn each separate list into a tuple 
		list[i] = tuple(list[i])
	
	#new_list sorts the tuples in ascending order based on the first number in each pair 
	new_list = []
	for i in range(len(list)):
		new_list.append(min(list))
		list.remove(min(list))
	
	#Print the header
	print()
	print('Non-intersecting Intervals:')
	
	i = 0
	#Go through the length of the list 
	while (i < len(new_list) - 1):
		#Establish coordinate values for first tuple and second tuple 
		x1 = new_list[i][0]
		y1 = new_list[i][1]
		x2 = new_list[i+1][0]
		y2 = new_list[i+1][1]
		
		#If the intervals overlap, remove the first two tuples 
		if (y1 >= x2):
			new_list.pop(i)
			new_list.pop(i)
			#Insert a new tuple into the list with the biggest interval possible 
			if (y2 >= y1):
				new_list.insert(i, (x1, y2))
			else:
				new_list.insert(i, (x1, y1))
		#If the intervals do not overlap, move the index over one 
		if (x2 > y1):
			i += 1
			
	#Print the contents of the list 
	for i in range (0, len(new_list)):
		print(new_list[i])	
				
				
				
main()
	
	
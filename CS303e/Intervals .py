#  File: Intervals.py

#  Description: Create a program that will output merged intervals so that there are no longer any overlapping intervals 

#  Student Name: Jonathan Zhang

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/19/2016
 
#  Date Last Modified: 4/19/2016 

def main():
	infile = open("intervals.txt", "r")
	
	list = []
	
	for line in infile:
		line.strip()
		line.split()
		list.append(line) 
	
	print (list)

main()
	
	
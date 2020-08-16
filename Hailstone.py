#  File: Hailstone.py

#  Description: Create a program that given a range of numbers, will calculate which number has the longest hailstone sequence 

#  Student Name: Johnny Zhang 

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/9/2016

#  Date Last Modified: 2/9/2016

def main():

	#Ask the user to enter the starting number and ending number in the range 
	start = eval(input("Enter starting number of the range: "))
	end = eval(input("\nEnter ending number of the range: "))
		
	#Check to see if start and end are both positive and if start < end 
	while (((start < 0) or (end < 0)) or (start >= end)):
		start = eval(input("\nEnter starting number of the range: "))
		end = eval(input("\nEnter ending number of the range: "))
		
	#Initialize variables to hold num and max counter 
	max_num = 0
	max_counter = 0
	
	#Set num to start value 
	num = start 
	#Initialize counter 
	counter = 0
	#Loop for numbers within the range 
	while (start <= end):
		#Reset the num and counter variables 
		num = start
		counter = 0
		#Iterate calculation of Hailstone sequence for each number in the range 
		while (num != 1):
			#If even number 
			if (num % 2 == 0):
				#Reset num for the next iteration 
				num = num // 2
			#If odd number 
			else:
				#Reset num for the next iteration 
				num = num * 3 + 1
			#Increment counter 
			counter += 1
			#Conditions for max_num and max_counter 
			if (counter >= max_counter):
				max_counter = counter 
				max_num = start  
		#Start the next number in the range 
		start += 1
	
	print ("\nThe number", str(max_num), "has the longest cycle length of", str(max_counter) + ".")
			
main()
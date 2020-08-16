#  File: PalindromicSum.py

#  Description: Given a range of numbers, figure out which one has the longest cycle until it becomes a palindromic number 

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/19/2016 

#  Date Last Modified: 2/19/2016 

#Create the reverse number function
def rev_num(n):
	rev_n = 0
	while (n > 0):
		rev_n = rev_n * 10 + (n % 10)
		n = n // 10
	return rev_n 
	
#Create the is_palindromic function 	
def is_palindromic(n):
	return (n == rev_num(n))

def main():
    #Ask the user to enter a starting and ending number 
	start = eval(input("Enter starting number of the range: "))
	end = eval(input("\nEnter ending number of the range: "))
	
	#Check for positivity and that start < end 
	while ((start > end) or (start < 0 or end < 0)):
		start = eval(input("\nEnter starting number of the range: "))
		end = eval(input("\nEnter ending number of the range: "))
	
	#Initialize max_counter and max_number 
	max_counter = 0
	max_number = 0 
	
	#While loop to iterate over the range of start and end 
	while (start <= end):
		#Set n to start and reset counter to 0 
		n = start 
		counter = 0
			
		#Iterate until the number IS palindromic 
		while (not(is_palindromic(n))):
			n = n + rev_num(n) 
			counter += 1 
			
		#Update max_counter and max_number 
		if (counter >= max_counter):
			max_counter = counter 
			max_number = start 
			
		#Go to the next value 
		start += 1 
		
	#Print output 	
	print ("\nThe number", str(max_number), "has the longest cycle length of", str(max_counter) + ".")
			
		
main() 

	
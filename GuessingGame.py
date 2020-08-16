#  File: GuessingGame.py

#  Description: Create a program that will "guess" a number that the user chooses between 1 and 100 (using binary search)

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246	

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/11/2016

#  Date Last Modified: 4/11/2016 

def main():
	#Initialize the boundaries of the guess 
	lo = 1
	hi = 100 
	
	#Print the introduction and header 
	print ("Guessing Game")
	print()
	print ("Think of a number between 1 and 100 inclusive.\nAnd I will guess what it is in 7 tries or less.")
	print()
	
	#Prompt the user to enter if he/she is ready or not 
	choice = input("Are you ready? (y/n): ")
	
	#Keep prompting if user is not entering y or n 
	while choice != 'y' and choice != 'n':
		choice = input("Are you ready? (y/n): ")
	if choice == 'n':
		print ("Bye")
		return 
	
	#Initialize the counter variable; this variable will not exceed 6 (for a total of 7 tries)
	counter = 0 
	#Initialize the first "guess" by the program; should be middle of lo and hi 
	mid = (lo + hi) // 2 
	while counter < 7:
		#Print the guess, ask for user input if right or wrong 
		print ("\nGuess %d: The number you thought was %d" %(counter + 1, mid))
		response = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
		print()
		
		#Keep prompting user if he/she is not entering 0, 1, or -1 
		while response != '0' and response != '1' and response != '-1':
			print ("\nGuess %d: The number you thought was %d" %(counter + 1, mid))
			response = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
			print()
			
		#If 0, break out of the program, else, reset mid accordingly 
		if response == '0':
			print("\nThank you for playing the Guessing Game.")
			return 
		elif response == '1':
			hi = mid 
			mid = (lo + mid) // 2
		elif response == '-1':
			lo = mid
			mid = (hi + mid + 1) // 2
			
		#Increment counter 
		counter += 1
	
	#If out of loop, that means the user guessed a number out of range or incorrect entry 
	print ("Either you guessed a number out of range or you had an incorrect entry.")
	
	
main()
# File: Deal.py

# Description: Create a program that simulates the game show Let's Make A Deal with host Monty Hall 

# Student Name: Johnny Zhang 

# Student UT EID: jz5246	 

# Course Name: CS 303E

# Unique Number: 50860

# Date Created: 3/4/2016

# Date Last Modified: 3/4/2016 

#Import random library 
import random 

#Define main
def main():
	#Get user input and initialize wins and counter 
	num_tries = eval(input("\nEnter number of times you want to play: "))
	wins = 0
	counter = 1
	
	#Print new line and header 
	print ()
	print ("  Prize      Guess       View    New Guess")
	
	#Loop for the number of times the user wants to play 
	while (counter <= num_tries):
		
		#Reset the variables 
		prize = random.randint(1, 3)
		user_guess = random.randint(1,3)
		view = 0
		newGuess = 0
	
		#Compute a number that determines which door Monty reveals. Cannot be the prize door or the user guess 
		for i in range (1,4):
			if (i != prize and i != user_guess):
				view = i 
	
		#Compute a number that determines the user's new guess. Cannot be view or original guess 
		for i in range (1,4):
			if (i != user_guess and i != view):
				newGuess = i 
		
		#Increment wins by 1 if the user "guessed" right 
		if (newGuess == prize):
			wins += 1 
		
		#Calculate the probablities that the user wins by switching and by not switching 
		switch_prob = wins / num_tries
		no_switch = 1 - switch_prob 
		
		#Print output 
		print ("    " + str(prize), end = "          ")
		print (str(user_guess), end = "          ")
		print (str(view), end = "          ")
		print (str(newGuess))
		
		#Increment counter 
		counter += 1
	
	#Print the probabilities 
	print ("\nProbability of winning if you switch = %.2f" %(switch_prob))
	print ("Probability of winning if you do not switch = %.2f" %(no_switch))
	
#Call main 
main()
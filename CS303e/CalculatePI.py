#  File: CalculatePI.py

#  Description: Create a program that will determine the value of pi given the probability of hitting a circle within a 2x2 square. The circle has radius 1 

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/29/2016 

#  Date Last Modified: 2/29/2016 

#Import libraries math and random 
import math
import random

#Define the computePI function 
def computePI(numThrows):
	#Initialize sum_darts to keep track of which darts hit the target 
	sum_darts = 0
	#Initialize counter 
	counter = 1
	#Iterate through numThrows, inclusive 
	while (counter <= numThrows):
		#Give a random x position and y position, assuming center of circle is origin and corner of board is 1,1 
		xPos = random.uniform(-1.0, 1.0)
		yPos = random.uniform(-1.0, 1.0)
		
		#Determine if dart landed within the 1 radius circle 
		if ((abs(xPos)**2 + abs(yPos)**2)**.5) < 1:
			sum_darts += 1
		#Go on to the next throw 	
		counter += 1 
	return (4 * (sum_darts / numThrows) )

#Define main 
def main():
	#Initialize num
	num = 100 
	#Calculate pi for numbers 100-10000000 by powers of 10
	#Header 
	print ("\nComputation of PI using Random Numbers\n")
	
	while (num <= 10000000):
		#Call the computePI function 
		compute_pi = computePI(num)
		#Calculate difference between computed and real Pi values 
		difference = compute_pi - math.pi 
		#Print output with formatting 
		print ("num = %-8d" %(num), end = '   ')
		print ("Calculated PI = %.6f" %(compute_pi), end = '   ')
		print ("Difference = %+-.6f" %(difference))
		#Increment num by powers of 10 
		num *= 10 
	#Closer 
	print ("\nDifference = Calculated PI - math.pi")
		
	
	

#Call main 
main()


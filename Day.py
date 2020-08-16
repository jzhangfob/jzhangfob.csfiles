#  File: Day.py

#  Description: Create a program that will tell the user the day of the week given a year, month, and day 

#  Student Name: Johnny Zhang 	

#  Student UT EID: jz5246		

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/6/2016

#  Date Last Modified: 2/6/2016 

def main():

	#Ask the user to enter a year 
	year = eval(input("Enter a year: "))
	
	#Input validation; check to see if year is in correct range 
	while ((year<1900) or (year>2100)):
		year = eval(input("Enter a year: "))
		
	#Ask the user to enter a month
	month = eval(input("Enter a month: "))
	
	#Check to see if month is in correct range
	while ((month<1) or (month>12)):
		month = eval(input("Enter a month: "))
		
	#Initialize the variable num_days
	num_days = 0
	
	#Figure out if the year is a leap year by assigning it to a boolean value 
	is_leap = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)) 
		
	#Set conditions for days in a month according to each month 
	if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) \
	or (month == 10) or (month == 12)):
		num_days = 31
	elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
		num_days = 30
	elif ((month == 2)):
		num_days = 28 
		#Condition for February and if year is leap year 
		if (is_leap):
			num_days = 29
		
	#Ask the user to enter in a day 
	day = eval(input("Enter a day: "))
	
	#Check to see if user input is valid 
	while ((day < 1) or (day > num_days)):
		day = eval(input("Enter a day: "))
			
	#Initialize variables a, b, c, d 
	
	#The month of the year, according to the algorithm 
	a = month 
	#The day of the month 
	b = day
	#The year of the century 
	c = year % 100 
	#The century 
	d = year // 100 
	
	#Change the numeric value of the month according to the algorithm 
	
	#For months between March and December; inclusive 
	if (month >= 3 and month <= 10):
		a -= 2
	#For January and February 
	else:
		a += 10  
		c = (year % 100) - 1
	
	#Algorithm 
	w = (13 * a - 1 ) // 5 

	x = c // 4 

	y = d // 4 

	z = w + x + y + b + c - 2 * d 

	r = z % 7 

	r = (r + 7) % 7 
	
	#Print out the day of the week
	if (r == 0):
		print ("\nThe day is Sunday.")
	elif (r == 1):
		print ("\nThe day is Monday.")
	elif (r == 2):
		print ("\nThe day is Tuesday.")
	elif (r == 3):
		print ("\nThe day is Wednesday.")
	elif (r == 4):
		print ("\nThe day is Thursday.")
	elif (r == 5):
		print ("\nThe day is Friday.")
	elif (r == 6):
		print ("\nThe day is Saturday.")
		
#Call main 
main()
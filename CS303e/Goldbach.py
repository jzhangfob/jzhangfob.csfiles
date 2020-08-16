#  File: Goldbach.py

#  Description: Given a range of even numbers greater than or equal to 4, print out all the unique sum combinations of prime numbers 

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/25/2016 

#  Date Last Modified: 2/25/2016 


#Define the is_prime function
def is_prime (n):
  if (n == 1):
    return False

  limit = int(n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor += 1
  return True
 

#Define main function 
def main():
	#Initialize start and end for the range 
	start = eval(input("Enter the lower limit: "))
	end = eval(input("Enter the upper limit: "))
	#While loop to check number conditions 
	while (start >= end or (start % 2 != 0 or end % 2 != 0) or start < 4):
		start = eval(input("Enter the lower limit: "))
		end = eval(input("Enter the upper limit: "))
	
	#Initialize the counter 
	counter = start 
	#Outer while loop to that iterates over the given range  
	while (counter <= end):
		
		#Initialize n and answer 
		n = 2 
		answer = ''
		#Note to self: always put variables that you need to update towards the top of the while loop so that it will reset after each iteration 
		#Inner while loop to determine all possible prime sum combinations excluding repititions 
		while (n <= counter // 2):
			if (is_prime(counter - n) and is_prime(n)):
				#Format the answer 
				answer += " = " + str(n) + " + "+ str(counter - n) 
			n += 1
		#Final format answer and print it out 
		answer = str(counter) + answer
		print(answer)
		#Go to the next number in the range 
		counter += 2
					
#Call main 	
main()
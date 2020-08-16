#  File: CreditCard.py

#  Description: Create a program that will determine if a credit card is valid, as well as what type it is

#  Student Name: Jonathan Zhang	

#  Student UT EID: jz5246

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/9/2016

#  Date Last Modified: 4/9/2016 



#This function is for the Luhn's Algorithm
#def luhn(int):
	
		
		
	


# This function checks if a credit card number is valid
def is_valid (cc_num):
	#cc_num = int(input("Enter 15 or 16-digit credit card number: "))
	cc_num = str(cc_num)
	print (len(cc_num))
	if len(cc_num) != 15 and len(cc_num) != 16:
		print ("Not a 15 or 16-digit number")
		return 
	else:
		#Length of string is 15 or 16-digit
		#Start from second digit, add 2 
		#Create a list to hold all integers 
		all_list = []
		#Create a list to hold products of odd integers * 2 
		odd_list = []
		#Create a list to hold all even index numbers 
		even_list = []
		#Initialize sum variable to store sum
		sum = 0
		for ch in cc_num:
			all_list.append(ch)
		#Convert strings to integers in the all_list 
		for i in range(len(all_list)):
			all_list[i] = int(all_list[i])
		print (all_list)
		#Create the list that will hold all the even indexed integers 
		for i in range(len(all_list) -1, -1, -2):
			even_list.append(all_list[i])
			if i == 0 or i == 1:
				break 
		print (even_list)
			
			
		#Create the list that will hold all odd indexed numbers * 2
		for i in range(len(all_list) - 2, -1, -2):
			product = all_list[i] * 2 
			odd_list.append(product)
			if i == 0 or i == 1:
				break 
			product = 0
		print (odd_list)
		
		




# This function returns the type of credit card
#def cc_type (cc_num): 




def main():
	cc_num = int(input("Enter 15 or 16-digit credit card number: "))
	is_valid(cc_num)



main()

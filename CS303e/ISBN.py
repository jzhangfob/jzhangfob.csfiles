#  File: ISBN.py

#  Description: Create a program that will validate a given ISBN number 

#  Student Name: Johnny Zhang

#  Student UT EID: jz5246

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 3/22/2016

#  Date Last Modified: 3/23/2016

#Function to calculate the partial sum of input and append to output 
def partial_sum(input_list, output_list):
	lower_in = 0
	upper_in = 0
	counter = 0
	sum = 0
	while (upper_in < len(input_list)):
		lower_in = 0
		sum = 0
		while (lower_in <= upper_in):
			sum += int(input_list[lower_in])
			lower_in += 1
		output_list.append(sum)
		upper_in += 1
	return output_list

#Function to clean up the ISBN number by getting rid of hyphens and white spaces; put result in a list 
def clean_isbn(isbn_num, list):
	isbn_num = isbn_num.replace("-", "")
	isbn_num = isbn_num.replace("\n", "")
	for ch in isbn_num:
		list.append((ch))
	return list

def main():
	#Open text infile for reading and text outfile for writing  
	infile = open("isbn.txt", "r")
	outFile = open("isbnOut.txt", "w")
	#Initialize the list that will hold the ISBN digits separately 
	holder = []
	#Initialize the list that will hold partial sums of holder list
	s1 = []
	#Initialize the list that will hold partial sums of s1 list
	s2 = []

	#List of acceptable ASCII codes
	accepted = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 88, 120]
	accepted_nums = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
	accepted_letters = [88, 120]

	#Initialize flag to keep reading lines until end is reached 
	end_of_file = 'False'
	while end_of_file == 'False': 

		#Read lines of file and strip away blank space char
		a = infile.readline()
		a = a.rstrip()
		#If reached the end of the file, break out of the loop 
		if a == '':
			break
		#Initialize the list that will hold the ISBN digits separately 
		holder = []
		#Initialize the list that will hold partial sums of holder list
		s1 = []
		#Initialize the list that will hold partial sums of s1 list
		s2 = []

		#Create the list with the ISBN numbers and call it mod_isbn
		mod_isbn = clean_isbn(a, holder)	
		#print (mod_isbn)

		#While loop to check if the ISBN passes basic requirements and to break out of the loop if otherwise, printing 'invalid'
		flag = 'Valid'
		while (flag == 'Valid'):
			if len(mod_isbn) != 10:
				print ('%s  invalid' %(a))
				#print ('ha')
				outFile.write('%s  invalid\n' %(a))
				flag = 'Invalid'
			elif len(mod_isbn) == 10:
				i = 0
				while i <= 8:
					if (ord(mod_isbn[i]) not in accepted_nums):
						print ('%s  invalid' %(a))
						outFile.write('%s  invalid\n' %(a))
						flag = 'Invalid'
					i += 1
				if (ord(mod_isbn[-1]) not in accepted):
					print ('%s  invalid\n' %(a))
					outFile.write('%s  invalid\n' %(a))
					flag = 'Invalid'
				else: 
					break

		#If tests are passed, now check for a valid ISBN number 
		if flag == 'Valid':
			#Change 'X' or 'x' to 10 
			if (ord(mod_isbn[-1]) in accepted_letters):
				mod_isbn[-1] = '10'
		

			#Tally up the partial sum of the ISBN digits into s1
			partial_isbn = partial_sum(mod_isbn, s1)
			#print (partial_isbn)

			#Tally up the partial sum of s1 into s2 
			final_sum = partial_sum(partial_isbn, s2)
			#print (final_sum)

			#Determine if ISBN is valid 
			if (int(final_sum[-1]) % 11 == 0):
				print ("%s  valid" %(a))
				outFile.write('%s  valid\n' %(a))
			else:
				print ("%s  invalid" %(a))
				outFile.write('%s  invalid\n' %(a))
	infile.close()
	outFile.close()
	



		
main()
	

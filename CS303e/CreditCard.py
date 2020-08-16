#  File: CreditCard.py

#  Description: Create a program that will determine if a credit is valid, and what type of credit card it is 

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/9/2016

#  Date Last Modified: 4/9/2016 

#Define a function to check the number of digits (return true if 15 or 16 length)
def check_digits(cc_num):

  if((len(str(cc_num)) == 15) or (len(str(cc_num)) == 16)):
    return True
  else:
    return False

#Apply Luhn's test to the number and check its validity 
def is_valid(cc_num):

  cc_digits = []
  len_num = len(str(cc_num))
  for i in range (len_num):
    cc_digits.append(cc_num % 10)
    cc_num = cc_num // 10

  #Double odd digits and take the sum of the digits of the odd numbers 
  for i in range (1, len_num, 2):
    cc_digits[i] = (cc_digits[i] * 2) % 10 + (cc_digits[i] * 2) // 10
  
  sum_all_digits = 0
  
  for i in range(len_num):
    sum_all_digits += cc_digits[i]

  if (sum_all_digits % 10 == 0):
    return True
  else:
    return False
    
    
    

#Define a function to determine the credit card type 
def cc_type(cc_num):
  
  cc_digits = []
  len_num = len(str(cc_num))
  
  for i in range (len_num):
    cc_digits.append(cc_num % 10)
    cc_num = cc_num // 10
  
  #Make the digits read left to right as entered by user
  for i in range (len_num // 2):
    cc_digits[i], cc_digits[len_num - 1 - i] = cc_digits[len_num - 1 - i], cc_digits[i]
    
  #Return output based on credit card type 
  if (cc_digits[0] == 3 and ((cc_digits[1] == 4) or (cc_digits[1] == 7))):
    return 'American Express '
  
  elif (cc_digits[0] == 6):
    if((cc_digits[1] == 0) and (cc_digits[2] == 1) and (cc_digits[3] == 1)):
      return 'Discover '
    elif((cc_digits[1] == cc_digits[2]) and (cc_digits[1] == 4)):
      return 'Discover '
    elif((cc_digits[1] == 5)):
      return 'Discover '

  elif(cc_digits[0] == 5 and cc_digits[1] <= 5):
    return 'MasterCard '
  
  elif(cc_digits[0] == 4):
    return 'Visa '
  
  else:
    return ''
   

def main():
  #Prompt user to enter a credit card number, check for validity and card type 
  cc_num = int(input('Enter a 15 or 16 digit number: '))
  
  #Check number of digits 
  if(not check_digits(cc_num)):
    print('Not a 15 or 16-digit number')
    return ''
  #If valid, print out the type and credit card number, returning a blank space for unidentifiable types 
  if(is_valid(cc_num)):
    print('Valid ' + cc_type(cc_num) + 'credit card number')
  else:
    print('Invalid credit card number')


main()
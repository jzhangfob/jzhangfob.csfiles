#  File: EasterSunday.py

#  Description: Write a program that will give you the date of Easter Sunday on any given year 

#  Student Name: Johnny Zhang 

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860 

#  Date Created: 1/30/2016

#  Date Last Modified: 1/30/2016 

#Define the main function
def main():
  #Ask the user to input a year 
  y = eval(input("Enter year: "))
  print ()
  #Create the formulas for the algorithm 
  a = y % 19
  b = y // 100 
  c = y % 100 
  d = b // 4
  e = b % 4 
  g = (8 * b + 13) // 25
  h = (19 * a + b - d - g + 15) % 30
  j = c //4 
  k = c % 4 
  m = (a + 11 * h) // 319 
  r = (2 * e + 2 * j - k - h + m + 32) % 7 
  n = (h - m + r + 90) // 25 
  p = (h - m + r + n + 19) % 32 
  
  #Conditional statements for the specific months 
  if n == 4:
    n = "April"
  else:
    n = "March"
  #Print out the output   
  print ("In", y, "Easter Sunday is on", p, n + '.')
#Call main
main()

#  File: Grid.py

#  Description: Create a program that will find the largest product of 4 numbers in any direction (horizontal, vertical, diagonal right, diagonal left) 

#  Student Name: Jonathan Zhang 

#  Student UT EID: jz5246 

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 4/15/2016 

#  Date Last Modified: 4/16/2016 

#Open up the text file for reading 
grid = open('grid.txt','r')

#Format the first item in the textfile to read as an int
n = grid.readlines(1)
n[-1] = int(n[-1].strip())
n = n[0]

#Create an empty list to hold unformatted horizontal lines
h_line = []
for line in grid:
    h_line.append(line.strip())

#Create a list to hold properly formatted horizontal lines 
horizontal=[]

#Create List to properly hold formatted vertical lines 
vertical =[]

#Create a function to format properly
def format(l):
    l = l.replace(" ","")
    Test = []
    i=0
    while i < (len(l)-1):
        q = int(l[i])
        w = int(l[i+1])
        num = ((q*10)+w)
        Test.append(num)
        i +=2
    horizontal.append(Test)

for line in h_line:
    num = format(line)

#Create a list that will hold the vertical numbers in lines 
for j in range (len(horizontal)-1):
    new=[]
    for i in range (len(horizontal[0])):
        new.append(horizontal[i][j])
    vertical.append(new)

#Create a function to find the max number of a given list 
def find_max(l):
    Max = 0
    for i in range(len(l)-3):
        num = l[i]*l[i+1]*l[i+2]*l[i+3]
        if num >= Max:
            Max = num
    return Max

#Initialize the max variable and compare it with num 
Max = 0
for line in horizontal:
    num = find_max(line)
    if num > Max:
        Max = num
for line in vertical:
    num = find_max(line)
    if num > Max:
        Max = num
		
#Create a loop that will go diagonally left to right 
k=0
while k < n-3:
    i = 0
    while i < n-3:
        num = (horizontal[k][i]*horizontal[k+1][i+1]*horizontal[k+2][i+2]*horizontal[k+3][i+3])
        i += 1
        if num > Max:
            Max = num
    k += 1

#Create a loop that will go diagonally right to left 
k=0
while k < n-3:
    i = (n-1)
    while i > 3:
        num = (horizontal[k][i]*horizontal[k+1][i-1]*horizontal[k+2][i-2]*horizontal[k+3][i-3])
        i -= 1
        if num > Max:
            Max = num
    k += 1

#Print output 
print ("The greatest product is ",Max, ".", sep="")


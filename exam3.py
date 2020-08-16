#EXAM 3 REVIEW 

# 2d lists scratchwork
b = []

a = [1, 2, 3]

b.append(a)

a = [4,5,6]

b.append(a)

a = [7,8,9]

b.append(a)

a = [1,2,3]

b.append(a)

'''
print (b) #b = [[1,2,3], [4,5,6], [7,8,9], [1,2,3]] len = 4 

for row in b:
	for col in row:
		print (col, end = '')
	print()
	
print ()

#Rows are represented by the length of the entire list 
for i in range(len(b)):
	#Columns are represented by the length of the sublists 
	for j in range(len(b[i])):
		print (b[i][j], end = '')
	print ()
	
print ()


for i in range(len(b[0])):
	for j in range(len(b)):
		print (b[j][i], end = '')
	print () 
	
#Make a copy of a matrix 
new_matrix = []
for row in b:
	new_row = row[:]
	new_matrix.append(new_row)
print (new_matrix)

#Transpose a matrix 
new_matrix = []
new_row = []
for i in range(len(b[0])):
	new_row = []
	for j in range(len(b)):
		new_row.append(b[j][i])
	new_matrix.append(new_row)
print (new_matrix)

'''
'''
#Dictionaries
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a']
dict = {}
for letter in letters:
	if letter in dict:
		dict[letter] += 1
	else:
		dict[letter] = 1 
print (dict)

string = 'abc !' 
new_string = string.strip()
for ch in new_string:
	if ch in dict:
		print (ch, dict[ch])

for key in dict:
	print (dict[key], key)

dict2 = {}
dict2['Texas'] = 'Austin'
dict2['China'] = 'Beijing'
dict2['Italy'] = 'Rome'
print (dict2)
dict3 = {}

for key in dict2:
	if key not in dict3:
		dict3[dict2[key]] = key 
print (dict3)

'''
'''

#Sets
list1= ['yo', 'hello', 'hi', 'be']
list2= ['yo', 'hi', 'be']

set1 = set(list1)
set2 = set(list2)
#Intersection of the two sets (what's common) 
set3 = set1 & set2 
print (set3) # set3 = set(['yo', 'hi', 'be'])

#Union of two sets (set1 + set2 minus the repeated) 
set3 = set1 | set2 
print (set3)

a = set(['a', 'b', 'c', 'd']) 
b = set(['a','b', 'e'])
#Difference between two sets (elements in a that aren't in b) 
g = a - b
print (g) # g = set(['c', 'd']) 

#Symmetric difference - elements in a or b but not in both 

g = a^b 
print (g) # g = set(['c', 'd', 'e'])
'''

'''
#Lists and associated functions

#Create a list with 3 rows and 5 columns populated with random numbers from 1- 100 
import random
list = []
for i in range(3):
	mini_list = []
	for j in range(5):
		x = random.randrange(1, 101)
		mini_list.append(x)
	list.append(mini_list)
print (list) #worked 

#Return True if 2-d lists are the same, False otherwise
list1 = [[1,2,3], [4,5,6]]
list2 = [[1,2,3], [4,5,6]]

for i in range(len(list1[0])):
	for j in range(len(list1)):
		if list1[j][i] != list2[j][i]:
			print ("False") 
print ("True")

#Create a new list from the sum of corresponding elements of two 2-d lists 
list = []
for i in range(len(list1[0])):
	mini_list = []
	for j in range(len(list1)):
		x = list1[j][i] + list2[j][i]
		mini_list.append(x)
	list.append(mini_list)
print (list)
	
#Create a 2d list from a 2d list with each row in reverse order 
list = [[1,2,3], [4,5,6]]
want = [] #we want [[3,2,1], [6,5,4]]


for i in range(len(list)):
	mini_list = []
	for j in range(1, len(list[0]) + 1):
		x = list[i][-j]
		mini_list.append(x)
	want.append(mini_list)
print (want) #correct 

#Create a 2d list from a 2d list with each column in reverse order 

list = [[1,2,3], [4,5,6], [7,8,9]]
new_list = []

for i in range(1, len(list) + 1):
	mini_list = []
	for j in range(len(list[0])):
		x = list[-i][j]
		mini_list.append(x)
	new_list.append(mini_list)
print (new_list)

#Given two 1-d lists of the same size, return the sum of the corresponding products of the elements 
list1 = [1,2,3]
list2 = [4,5,6]

sum = 0
for i in range(len(list1)):
	product = list1[i] * list2[i]
	sum += product
print (sum) #Correct 

#Create functiont that returns True if 1-d list is sorted in ascending order, false otherwise
list = [1,2,4,7]

for i in range(len(list)):
	if i == len(list) - 1:
		break 
	if (list[i + 1] >= list[i]) == False:
		print ('False')
print ('True') #worked 

assorted = []
min = list[0]
copy = list[:]
while len(copy) != 0:
	min = copy[0]
	for i in range(len(copy)):
		if copy[i] <= min:
			min = copy[i]
	assorted.append(min)
	copy.remove(min)
if assorted == list:
	print ('True haha') #worked 
	
#Create a function that returns the sum of rows, columns and diagonals 
list = [[1,2,3], [4,5,6], [7,8,9]]

sum = 0
for i in range(len(list)):
	row_sum = 0
	for j in range(len(list[0])):
		row_sum += list[i][j]
	sum += row_sum 
	
for i in range(len(list[0])):
	col_sum = 0
	for j in range(len(list)):
		col_sum += list[j][i]
	sum += col_sum
	
for i in range(len(list)):
	r_diag = 0
	r_diag += list[i][i]
	sum += r_diag 

for i in range(len(list)):
	l_diag = 0
	l_diag += list[i][len(list) - 1 -i]
	sum += l_diag 

print (sum)

#Shuffle contents of the list 

list = [1,2,3,4,5]

new_list = []

copy = list[:]

while len(copy) != 0:
	for i in range(len(copy)):
		index = random.randrange(0, len(copy))
		new_list.append(copy[index])
		copy.remove(copy[index])
print (new_list)
'''
'''
#Strings and their functions 
string1 = 'iceman!@34'
string2 = 'cinema  '

list1= []
list2 = []

for ch in string1:
	if ch.isalpha():
		a = ch.upper()
		list1.append(a)

for ch in string2:
	if ch.isalpha():
		a = ch.upper()
		list2.append(a)

set1 = set(list1)
set2 = set(list2)
set3 = set1 & set2 

if set3 == set1 and set3 == set2:
	print ("True")
else:
	print ("False") #Worked 
'''
#File manipulation for reading, writing, appending 

infile = open("userpassword.txt", "r")
username = 'jzhangfob'
password = 'hello'
string = username + password 

for line in infile:
	line = line.strip()
	line = line.replace(":", "")
	if line == string:
		print ("True")

infile.close()

a = [2, 5, 8, 9, 11, 14, 16, 19, 22, 25, 35, 41, 45, 55, 62]
x = 23

def binarySearch (a, x):
	lo = 0
	hi = len(a) - 1
	count = 0
	while (lo <= hi):
		count = count + 1
		mid = (lo + hi) // 2
		print (count, mid)
		if (x < a[mid]):
			hi = mid - 1
		elif (x > a[mid]):
			lo = mid + 1
		else:
			return mid
	return -1

binarySearch(a, x)

	








		




			







	



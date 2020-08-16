#  File: htmlChecker.py
#  Description: Create a program that will check if an html file has matching tags throughout 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 9/30/2016
#  Date Last Modified: 9/30/2016 


#Implement the stack class
class Stack (object):
	def __init__(self):
		self.items = [ ]

	def isEmpty (self):
		return self.items == [ ]

	def push (self, item):
		self.items.append (item)

	def pop (self):
		return self.items.pop ()

	def peek (self):
		return self.items [len(self.items)-1]

	def size (self):
		return len(self.items)

def getTag(index, line):
	returnTag = ''
	while line[index] != ">":
		if line[index] == ' ':
			break
		returnTag += line[index]
		index += 1 
	return returnTag 
		
def main():

	infile = open("htmlfile.txt", "r")
	#Hold every single tag 
	tagsList = []
	#Get rid of duplicates from tagsList
	VALIDTAGS = []
	counter = 0
	#Create an instance of stack
	tagStack = Stack()
	#Create an exception tags list 
	EXCEPTIONS = ['meta', 'br', 'hr']
	
	#Read each line, then go through each line to extract all tags 
	for line in infile:
		line = line.strip()
		if line == "":
			continue
		#Iterate through the line and extract tags, appending them to tagsList 
		for i in range(len(line)):
			if line[i] == "<":
				tagsList.append(getTag(i+1, line))
	
	#Iterate through tagsList to create validTags
	for tag in tagsList:
		#Check for exceptions
		if tag in EXCEPTIONS:
			print ("Tag " + str(tag) + " does not need a match: stack is still ", end = '')
			print (tagStack.items)
			#Add tag to VALIDTAGS
			if tag not in VALIDTAGS:
				VALIDTAGS.append(tag)
				print ("This is a new tag. Adding to VALIDTAGS")
			continue 
		#Push start tags onto the stack and print output 
		if tag[0] != "/":
			tagStack.push(tag)
			print ("Tag " + str(tag) + " pushed: stack is now ", end = '')
			print (tagStack.items)
		#Check to make sure end tags match with top of stack
		elif tag[0] == "/":
			#If it's a match 
			if tag[1:] == tagStack.peek():
				tagStack.pop()
				print ("Tag " + str(tag) + " matches top of stack: stack is now ", end = '')
				print (tagStack.items)
			#If not a match 
			else:
				print ("Error. Tag is " + str(tag) + " but top of stack is " + str(tagStack.peek()))
				#break
		#Add tag to VALIDTAGS
		if tag not in VALIDTAGS:
			VALIDTAGS.append(tag)
			print ("This is a new tag. Adding to VALIDTAGS")
			
	#Ending output 
	if tagStack.isEmpty():
		print ("Processing complete. No mismatches found")
	if tagStack.isEmpty() == False:
		print ("Processing complete. Unmatched tags remain on stack: ", end = '')
		print (tagStack.items)
	
	print ("\nHere's the list of valid tags: ", end = '')
	VALIDTAGS.sort()
	print (VALIDTAGS)
	EXCEPTIONS.sort()
	print ("\nHere's the list of exceptions: ", end = '')
	print (EXCEPTIONS)
	
main()



	


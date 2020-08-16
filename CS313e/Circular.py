#  File: Circular.py
#  Description: Create a program that simulates Hot Potato using Circular Lists 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/28/2016
#  Date Last Modified: 10/30/2016 

class Node (object):
	def __init__(self,initdata):
		self.data = initdata	# always do this â€“ saves a lot
		self.next = None        # of headaches later!
		
	def getData (self):
		return self.data            # returns a POINTER

	def getNext (self):
		return self.next            # returns a POINTER

	def setData (self, newData):
		self.data = newData         # changes a POINTER

	def setNext (self,newNext):
		self.next = newNext         # changes a POINTER

#Circular list class 
class CircularList(object):

	def __init__ (self): 
	# the circular list constructor method.
		sentinel = Node('Sentinel')
		self.head = sentinel 
		sentinel.setNext(self.head)

	def add (self,item):
		#Add elements to the back of the list 
		current = self.head.getNext()
		previous = self.head 
		
		while current.getNext() != self.head:
			previous = current 
			current = current.getNext()
		temp = Node(item)
		current.setNext(temp)
		temp.setNext(self.head)
		
	#Return if the circular list is empty or not 
	def isEmpty (self):
		return (self.head.getNext() == self.head)
	 
	#Return true if there's only one person left in the list; the survivor 
	def onlyOneNode (self):
		#Set current to the first person after sentinel 
		onlyOne = False 
		current = self.head.getNext()
		if current.getNext() == self.head:
			onlyOne = True 
		return (onlyOne)
		
	def remove (self,current,previous):
      # Delete the node pointed to by "current" from the circular list.
      # Pass the "previous" pointer along for convenience.  This method
      # would only be called if there are at least 2 nodes in the list.
      # Return a pointer to the node immediately following the deleted
      # one.  Hint:  be sure to correctly handle the case where you delete
      # the first node in the circular list.
	  #^^^self.head.setNext(previous.getNext()) -- for deleting the first node in the ciruclar list 
		if self.head.getNext() == current:
			self.head.setNext(current.getNext())
			return 
		previous.setNext(current.getNext())
	  
	def __str__ (self):
		returnString = ''
		current = self.head
		counter = 1 
		while current.getNext() != self.head:
			if counter % 10 == 0:
				returnString += '\n'
			returnString += str(current.getNext().getData()) + ' '
			current = current.getNext()
			counter += 1 
		return (returnString)
			
def main():
	'''
	test = CircularList()
	test.add('Johnny')
	test.add('Wilson')
	test.add('Roger')
	test.add('Mike')
	
	hit = 3
	counter = 0 
	current = test.head 
	previous = None 
	while test.onlyOneNode() == False:
		while counter < hit:
			if current.getNext() == test.head:
				previous = current 
				current = test.head.getNext()
				counter += 1 
				continue 
			previous = current 
			current = current.getNext()
			counter += 1 
		test.remove(current,previous) 
		print(test)
		counter = 0 
	'''
	infile = open("HotPotatoData.txt","r")
	for line in infile:
		#line = line.strip()
		line = line.split() 
		playerList = CircularList()
		while line != '':
			round = 1 
			numNames = int(line[0])
			hitCount = int(line[1])
			
			for i in range(0, numNames):
				line = infile.readline().rstrip()
				playerList.add(line)
			#print(playerList)
			#hitCount = int(line[1])
			counter = 0 
			current = playerList.head 
			previous = None 
			while playerList.onlyOneNode() == False:
				counter = 0 
				while counter < hitCount:
					if current.getNext() == playerList.head:
						previous = current 
						current = playerList.head.getNext()
						counter += 1 
						continue 
					previous = current 
					current = current.getNext()
					counter += 1 
				print ("Iteration number: " + str(round))
				print ("Player to be removed: " + str(current.getData()))
				playerList.remove(current,previous)
				if playerList.onlyOneNode() == True:
					print ("The sole survivor: ", end = '')
					print (playerList) 
					print ("\nNEW GAME\n")
				else:
					print ("Updated List of players: ", end = '')
					print (playerList)
				round += 1 
			break
			
main()
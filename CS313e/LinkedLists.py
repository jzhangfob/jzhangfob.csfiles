#  File: LinkedLists.py
#  Description: Create a program that has methods for Linked Lists
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/20/2016
#  Date Last Modified: 10/21/2016 


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
	  
class LinkedList():
	
	def __init__(self):
		self.head = None 
		
	def __str__(self):
		
		returnString = ''
		current = self.head 
		while current != None:
			returnString += str(current.getData()) + '  '
			current = current.getNext()
		
		return returnString
			
	#Add an item to the beginning of the list
	def addFirst(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp 
	
	#Add an item to the end of the list 
	def addLast(self, item):
		temp = Node(item)
		found = False 
		current = self.head
		if current == None:
			self.head = temp 
		else:
			while not found:
				if current.getNext() == None:
					found = True 
				else:
					current = current.getNext()
			current.setNext(temp)
			
	#Insert an item in the proper place of an ordered list, assuming the original list is already in order 
	def addInOrder(self, item):
		temp = Node(item)
		found = False 
		previous = None 
		current = self.head 
		
		while not found and current != None: 
			if current.getData() > temp.getData():
				found = True 
			else:
				previous = current 
				current = current.getNext()
		
		if previous == None:
			temp.setNext(self.head)
			self.head = temp 
		else:
			temp.setNext(current)
			previous.setNext(temp)
	
	#Return the number of items in the list 
	def getLength(self):
		length = 0
		current = self.head 
		while current != None:
			length += 1 
			current = current.getNext() 
		return length
	
	#Search an unordered list for an item returning True or False 
	def findUnordered(self, item):
		found = False 
		current = self.head 
		
		while not found and current !=None:
			if current.getData() == item: 
				found = True 
			else:
				current = current.getNext()
		
		return found
	
	#Search an ordered list for an item returning True or False, should be more efficient than unOrdered search 
	def findOrdered(self, item):
		found = False 
		stop = False 
		current = self.head 
		while not found and not stop and current != None:
			if current.getData() == item:
				found = True 
			elif current.getData() > item:
				stop = True 
			else:
				current = current.getNext() 
				
		return found 
			
	#Delete an item from an unordered list, returning True if found, False otherwise 
	def delete(self, item):
		found = False 
		current = self.head
		previous = None 
		while not found and current != None:
			if current.getData() == item:
				found = True 
			else:
				previous = current 
				current = current.getNext()
		#If the item you need to delete is the first and only element in list 
		if previous == None:
			self.head = current.getNext()
		else:
			#If not found 
			if current == None:
				return found 
			previous.setNext(current.getNext())
		return found
		
	#Return a new linked list that is a copy of the OG made up of its individual elements 
	
	def copyList(self):
		returnList = LinkedList()
		current = self.head 
		while current != None:
			temp = current.getData()
			returnList.addLast(temp)
			current = current.getNext()
		
		return (returnList)
			
	
	#Return a new linked list that contains the elements of the original list in reverse order 
	def reverseList(self):
		returnList = LinkedList()
		current = self.head
		while current != None:
			returnList.addFirst(current.getData())
			current = current.getNext()
		return (returnList) 
	
	#------THIS IS MY OWN REMOVE METHOD THAT i USE IN ORDERLIST------
	def remove(self,item):
		found = False 
		current = self.head
		previous = None 
		while not found and current != None:
			if current.getData() == item:
				found = True 
			else:
				previous = current 
				current = current.getNext()
		#If the item you need to delete is the first and only element in list 
		if previous == None:
			self.head = current.getNext()
		else:
			#If not found 
			if current == None:
				return found 
			previous.setNext(current.getNext())

	#Return a new linked list that contains the elements of the original list in acsending (alphabetical) order 
	def orderList(self):
		returnList = LinkedList()
		copy = self.copyList()
		current = copy.head 
		while copy.head != None:
			current = copy.head 
			min = current.getData()
			while current != None:
				if current.getData() <= min:
					min = current.getData()
				current = current.getNext()
			returnList.addLast(min)
			copy.remove(min)
		return (returnList)
		
	#Return True if list in ascending order, false otherwise 
	def isOrdered(self):
		current = self.head 
		previous = None 
		if current == None:
			return True 
		while current != None:
			if current.getNext() == None:
				break 
			if current.getData() > current.getNext().getData():
				return False 
			current = current.getNext()
		return True 
	
	
	def isEmpty(self):
		return (self.head == None)
	
	
	def mergeList(self, b):
		sum = ''
		current = self.head 
		current2 = b.head
		returnList = LinkedList()
		while current != None:
			sum = ''
			sum += current.getData()
			sum += current2.getData()
			returnList.addLast(sum)
			current = current.getNext()
			current2 = current2.getNext()
		return (returnList)
	#Test if two lists are equal, item by item 
	def isEqual(self, b):
		isEqual = True 
		current = self.head
		current2 = b.head 
		while isEqual and current != None:
			if current == None or current2 == None:
				break
			if current.getData() != current2.getData():
				isEqual = False 
			current = current.getNext()
			current2 = current2.getNext()
		if current != current2:
			return (False)
		return (isEqual)
	
	#Remove all duplicates from a list, returning a new list. Do not change the order of the remaining elements 
	def removeDuplicates(self):
		returnList = self.copyList()
		current = returnList.head 
		while current != None: 
			current2 = current 
			while current2 != None:
				prev = current2 
				current2 = current2.getNext()
				if current2 == None:
					break 
				if current2.getData() == current.getData():
					next = current2.getNext() 
					prev.setNext(next)
			current = current.getNext()
		return (returnList)
			



# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
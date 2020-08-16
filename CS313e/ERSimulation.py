#  File: ERSimulation.py
#  Description: Create a program that will simulate hospital queues for treating patients 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/12/2016
#  Date Last Modified: 10/13/2016 

class Queue:

	def __init__(self):
		self.items = []

	def enqueue(self,item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

#Function to print all three queues 
def printQueues(critical, serious, fair):
	print ("Queues are:")
	print ("Critical: ", end = '')
	print (critical.items)
	print ("Serious: ", end = '')
	print (serious.items)
	print ("Fair: ", end = '')
	print (fair.items)
	print ()

def main():
	#Create the queues
	Critical = Queue()
	Serious = Queue()
	Fair = Queue()
	
	#Open and read lines from the file 
	infile = open("ERsim.txt", "r")
	
	#Read lines
	for line in infile:
		line = line.strip()
		keywords = line.split()
		
		#Keyword add
		if keywords[0] == "add":
			#If critical
			if keywords[-1] == "Critical":
				print ("Add patient " + str(keywords[1] + "to Critical queue"))
				Critical.enqueue(keywords[1])
				printQueues(Critical, Serious, Fair)
			#If serious 
			elif keywords[-1] == "Serious":
				print ("Add patient " + str(keywords[1] + "to Serious queue"))
				Serious.enqueue(keywords[1])
				printQueues(Critical, Serious, Fair)
			#If fair
			else:
				print ("Add patient " + str(keywords[1] + "to Fair queue"))
				Fair.enqueue(keywords[1])
				printQueues(Critical, Serious, Fair)
				
		#Keyword treat 
		elif keywords[0] == "treat":
			#If treat next 
			if keywords[1] == "next":
				#Check for all empty 
				#if (Critical.isEmpty() == True and Serious.isEmpty() == True and Fair.isEmpty() == True):
				#	print ("No patient in Queues")
				#If Critical not empty 
				if Critical.isEmpty() == False:
					print ("Treat next patient in Critical queue")
					print ("\nTreating " + str(Critical.peek()) + " from Critical queue")
					Critical.dequeue()
					printQueues(Critical, Serious, Fair)
				#If Critical empty 
				elif Critical.isEmpty() == True:
					#If Serious not empty 
					if Serious.isEmpty() == False:
						print ("Treat next patient in Serious queue")
						print ("\nTreating " + str(Serious.peek()) + " from Serious queue")
						Serious.dequeue()
						printQueues(Critical, Serious, Fair)
					#If Serious empty 
					elif Serious.isEmpty() == True:
						#If Fair not empty 
						if Fair.isEmpty() == False:
							print ("Treat next patient in Fair queue")
							print ("\nTreating " + str(Fair.peek()) + " from Fair queue")
							Fair.dequeue()
							printQueues(Critical, Serious, Fair)
						#If it makes it down to here, all queues are empty, print output 
						elif Fair.isEmpty() == True:
							print ("No patient in Queues")
			#If treat all
			elif keywords[1] == "all":
				print ("\nTreat all\n")
				while Critical.isEmpty() == False:
					print ("Treat next patient in Critical queue")
					print ("\nTreating " + str(Critical.peek()) + " from Critical queue")
					Critical.dequeue()
					printQueues(Critical, Serious, Fair)
				while Serious.isEmpty() == False:
					print ("Treat next patient in Serious queue")
					print ("\nTreating " + str(Serious.peek()) + " from Serious queue")
					Serious.dequeue()
					printQueues(Critical, Serious, Fair)
				while Fair.isEmpty() == False:
					print ("Treat next patient in Fair queue")
					print ("\nTreating " + str(Fair.peek()) + " from Fair queue")
					Fair.dequeue()
					printQueues(Critical, Serious, Fair)
				print ("\nAll patients treated\n")
			#If treat a specific queue
			if keywords[1] == "Serious":
				if Serious.isEmpty() == False:
					print ("Treat next patient in Serious queue")
					print ("\nTreating " + str(Serious.peek()) + " from Serious queue")
					Serious.dequeue()
					printQueues(Critical, Serious, Fair)
				elif Serious.isEmpty() == True:
					print ("No patients left in Serious")
			elif keywords[1] == "Critical":
				if Critical.isEmpty() == False:
					print ("Treat next patient in Critical queue")
					print ("\nTreating " + str(Critical.peek()) + " from Critical queue")
					Critical.dequeue()
					printQueues(Critical, Serious, Fair)
				elif Critical.isEmpty() == True:
					print ("No patients left in Critical")
			elif keywords[1] == "Fair":
				if Fair.isEmpty() == False:
					print ("Treat next patient in Fair queue")
					print ("\nTreating " + str(Fair.peek()) + " from Fair queue")
					Fair.dequeue()
					printQueues(Critical, Serious, Fair)
				elif Fair.isEmpty() == True:
					print ("No patients left in Fair")
			
		#If exit
		if keywords[0] == "exit":
			print ("Exit")
			

			


main()

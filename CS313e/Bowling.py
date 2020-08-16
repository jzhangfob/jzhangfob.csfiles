#  File: Bowling.py
#  Description: Create a program that will output the correct score of a 10-frame bowling game
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/6/2016
#  Date Last Modified: 9/6/2016


#Create a function to calculate the running score
def calcScore(masterlist):

	#Pass a list through this function and spit out a score 
	#Print out all the output 
	
	runningScore = 0
	runningList = []
	counter = 0
	
	#Change the special characters within a score line into numbers
	for i in range(len(masterlist)):
		
		for j in range(len(masterlist[i])):
		
			if masterlist[i][j] == "X":
				masterlist[i][j] = "10"
			if masterlist[i][j] == "/":
				masterlist[i][j] = str(10 - int(masterlist[i][j-1]))
			if masterlist[i][j] == "-" or masterlist[i][j] == " ":
				masterlist[i][j] = "0"
	
		
	#Create the running list 	
	for i in range(len(masterlist)):
	
		for j in range(len(masterlist[i])):
			
			if counter == 9:
				runningScore += int(masterlist[i][j])
				runningScore += int(masterlist[i][j+1])
				
				if ((int(masterlist[i][j]) + int(masterlist[i][j+1])) >= 10):
					runningScore += int(masterlist[i][j+2])
				
				break
			
			#If strike on the 9th roll
			if masterlist[i][j] == "10" and counter == 8:
				runningScore += 10
				runningScore += int(masterlist[i+1][0])
				runningScore += int(masterlist[i+1][1])
			
			#If your roll a normal strike 
			elif masterlist[i][j] == "10":
				
				runningScore += 10
				
				#If you roll a strike again 
				if masterlist[i+1][j] == "10":
					
					#If you're on the 10th frame, sum up what's left and break the loop 
					if counter == 9: 
						runningScore += int(masterlist[i][j:])
						runningList.append(runningScore)
						break
					
					#If you're not on the 10th frame, sum up the strike and the next score 
					runningScore += 10 
					runningScore += int(masterlist[i+2][0])
				
				#If you don't roll another strike, simply add the next two scores 
				else:
				
					runningScore += int(masterlist[i+1][j])
					runningScore += int(masterlist[i+1][j+1])
			
			#If a spare 
			elif  (j != 1) and (int(masterlist[i][j]) + int(masterlist[i][j+1]) == 10):
				
				runningScore += 10 
				runningScore += int(masterlist[i+1][0])
				break 
		
			#If a normal shot 
			else:
			
				runningScore += int(masterlist[i][j])
			
		runningList.append(runningScore)
		counter += 1
	
	#Return frame score 
	return runningList 
	
	
def main():
	
	
	#Open the file the reading and name it scores
	scores = open("scores.txt", "r")
	
	#Constantly updating list of scores (per line)
	scoreList = []
	
	#Iterate through the file 
	for line in scores:
		
		#Split the lines into this list 
		scoreList = line.split()
		
		#Constantly updating frame list 
		frameList = []
		
		#Constantly updating list of all the frame lists 
		masterList = []
		
		i = 0
		#Keeps track of what frame we're on 
		counter = 0
		
		#Loop through the scores and put the scores into their respective frames, 1-10 
		while i < len(scoreList):
			
			#List to hold the scores 
			frameList = []
			
			if counter == 9:
			
				for j in range(i, len(scoreList)):
					
					frameList.append(scoreList[j])
				masterList.append(frameList)
				break
			
			if scoreList[i].isdigit() or scoreList[i] == "-":
			
				if i == len(scoreList) - 1:
					
					break 
				
				frameList.append(scoreList[i])
				frameList.append(scoreList[i+1])
				masterList.append(frameList)
				counter += 1 
				
				i += 1
						
			elif scoreList[i] == "X":
			
				frameList.append(scoreList[i])
				
				if i == len(scoreList) - 3 and counter == 9:
					
					frameList.append(scoreList[i + 1])
					frameList.append(scoreList[i + 2])
					masterList.append(frameList)
					counter += 1
					break 
	
				masterList.append(frameList)
				counter += 1
			
			i += 1
		
		#Print the header 
		print("  1   2   3   4   5   6   7   8   9    10")
		print("+---+---+---+---+---+---+---+---+---+-----+")
		
		#Print the frames and their respective scores 
		for i in range(len(masterList)):
		
			if(masterList[i][0] == "X"):
				masterList[i].append(" ")

		if(len(masterList[9]) == 2):
			masterList[9].append(" ")

		print("|", end = "")
		
		for j in range(len(masterList)):
		
			if j == 9:
				print(masterList[j][0], masterList[j][1], str(masterList[j][2]) + "|")
				
			else:
				print(masterList[j][0], masterList[j][1], end = "|")
		
		#Call the function to calculate the score 
		a = calcScore(masterList)
		
		print("|", end = "")
		
		for num in range(len(a)):
		
			n = str(a[num])
			if num == 9:
				print(n.rjust(5, " "), end = "")
				print("|")
				
			else:
				print(n.rjust(3, " "), end = "|")
				
		print("+---+---+---+---+---+---+---+---+---+-----+")

		print()


main()
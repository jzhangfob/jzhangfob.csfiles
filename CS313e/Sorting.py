#  File: Sorting.py
#  Description: Create a program that will run different sorting methods on multiple sets data and create time tables 
#  Student's Name: Jonathan Zhang
#  Student's UT EID: jz5246
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/16/2016
#  Date Last Modified: 11/16/2016 

import random
import time
import sys
sys.setrecursionlimit(10000)

#Sort functions 
def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1,fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp


def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue

def shellSort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapInsertionSort(alist,startposition,sublistcount)
		sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):
		currentvalue = alist[i]
		position = i

		while position>=gap and alist[position-gap]>currentvalue:
			alist[position] = alist[position-gap]
			position = position - gap

		alist[position] = currentvalue

def mergeSort(alist):
	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j += 1
			k += 1

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
	if first < last:
		splitpoint = partition(alist,first,last)
		quickSortHelper(alist,first,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
	pivotvalue = alist[first]
	leftmark = first + 1
	rightmark = last
	done = False

	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark += 1

		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark -= 1

		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark
	
#Calculate run time averages given list size 
	#n is the size of the list, 0 up to n but not including n 
	#sortType tell you what sort method you're using
	#listType tells you what kind of data to use (random, almostSorted, Reverse, sorted)
def calAverage(n, sortType, listType):
	avgTime = 0 
	for i in range(5):
		list = [i for i in range(n)]
		#Configure the list according to its type  
		if listType == "Random":
			random.shuffle(list)
		elif listType == "Reverse":
			list.reverse()
		elif listType == "Almost sorted":
			tenPercent = n//10 
			for i in range(tenPercent):
				#Must go n-1 because the range is INCLUSIVE 
				swapOne = random.randint(0, n-1)
				swapTwo = random.randint(0, n-1)
				temp = list[swapTwo]
				list[swapTwo] = list[swapOne]
				list[swapOne] = temp
		#Start the counter 
		startTime = time.perf_counter()
		#Sort the list 
		sortType(list)
		#End the counter 
		endTime = time.perf_counter()
		#Calculate elapsed time 
		elapsedTime = endTime - startTime 
		avgTime += elapsedTime 
	#Calc average time 
	avgTime = avgTime / 5 
	avgTime = round(avgTime, 6)
	return (avgTime)

#Create a function that will generate the desired formatted output given a start list type 
def solve(listType):
	
	print ("Input type = " + str(listType))
	print ("                    avg time   avg time   avg time")
	print ("   Sort function     (n=10)     (n=100)   (n=1000)")
	print ("-----------------------------------------------------")
	print ("      bubbleSort" + str(calAverage(10, bubbleSort, str(listType))).rjust(12) + str(calAverage(100, bubbleSort, str(listType))).rjust(11) + str(calAverage(1000, bubbleSort, str(listType))).rjust(11))
	print ("   selectionSort" + str(calAverage(10, selectionSort, str(listType))).rjust(12) + str(calAverage(100, selectionSort, str(listType))).rjust(11) + str(calAverage(1000, selectionSort, str(listType))).rjust(11))
	print ("   insertionSort" + str(calAverage(10, insertionSort, str(listType))).rjust(12) + str(calAverage(100, insertionSort, str(listType))).rjust(11) + str(calAverage(1000, insertionSort, str(listType))).rjust(11))
	print ("       shellSort" + str(calAverage(10, shellSort, str(listType))).rjust(12) + str(calAverage(100, shellSort, str(listType))).rjust(11) + str(calAverage(1000, shellSort, str(listType))).rjust(11))
	print ("       mergeSort" + str(calAverage(10, mergeSort, str(listType))).rjust(12) + str(calAverage(100, mergeSort, str(listType))).rjust(11) + str(calAverage(1000, mergeSort, str(listType))).rjust(11))
	print ("       quickSort" + str(calAverage(10, quickSort, str(listType))).rjust(12) + str(calAverage(100, quickSort, str(listType))).rjust(11) + str(calAverage(1000, quickSort, str(listType))).rjust(11))
	print ()
	print ()

def main():
	
	#Solve for randomized list, sorted list, reversed list, and an almost sorted list 
	solve("Random")
	solve("Sorted")
	solve("Reverse")
	solve("Almost sorted")
	
main()
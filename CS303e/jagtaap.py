# Create a global variable for the word dictionary
dict = {}

#Populate the global dictionary from the scrabble text file 
def create_word_dict(filename):
	scrabble = open(filename, "r")
	for line in scrabble:
		line = line.strip()
		if line in dict:
			dict[line] = dict[line] + 1
		else:
			dict[line] = 1
	
	scrabble.close()

#Modify the string so that it handles punctuation and apostrophes 
def parseString(st):
	blank_string = ' '
	
	for i in range(len(st)):
		if st[i].isalpha():
			blank_string += st[i]	
		if i == len(st) - 2:
			if i == "'":
				if st[i+1] != "s":
					blank_string += "'"
					blank_string += st[i+1]
					break 
	blank_string = blank_string.strip()
	return blank_string

#Function that will return a dictionary of words from the novel 
def getWordFreq(file):
	#Open the book for reading
	book = open(file, "r")
	#Temporary storage unit for words in a line 
	word_list = []
	#Temporary dictionary that holds spaces 
	word_dict = {}
	
	#Loop through lines in book and modify 
	for line in book:
		#Get rid of \n at the end 
		line = line.strip()
		if len(line) == 0:
			continue
		#Replace hyphens with spaces 
		if '-' in line:
			line = line.replace('-', ' ')
		#Create a list with the words in the line 
		word_list = line.split()
		#print (word_list)
		#Populate the dictionary with the words
		for word in word_list: 
			if word.isnumeric() == False:
				word = parseString(word)
				#print (word, type(word))
				if word in word_dict:
					word_dict[word] += 1
				else:
					word_dict[word] = 1 
	book.close()
	
	#Transfer the words from the dictionary into a list 
	dict_list = []
	for key in word_dict:
		if key:
			dict_list.append(key)
			
	#Fish out the capitalized words, as they are repeats 
	#Create a list to hold capitalized words 
	cap_list = []
	for word in dict_list:
		if word[0].isupper():
			cap_list.append(word)
	#print (cap_list)
	
	#Dealing with capitalized words 
	for word in cap_list:
		if word.lower() in word_dict:
			word_dict[word.lower()] += word_dict[word]
			#print (word_dict[word.lower()], word.lower())
		elif word.lower() in dict:
			#print ("AY")
			word_dict[word.lower()] = word_dict[word]
		if word in word_dict:
			del word_dict[word]
	
	return word_dict 
	
#Function that will compare statistics from the two novels 	
def wordComparison(author1, wordfreq1, author2, wordfreq2):
	#Get the unique words from the first dictionary, put them in a list 
	unique_list1 = [] 
	check_total_1 = 0
	for key in wordfreq1:
		check_total_1 += wordfreq1[key]
		#print (key, type(key), word_dict[key])
		if key:
			unique_list1.append(key) 
	print (author1)
	print ('Total distinct words =', len(unique_list1)) #-- unique words 	
	print ('Total words (including duplicates) =', check_total_1)
	print ('Ratio (% of total distinct words to total words) =', round(len(unique_list1) * 100 / check_total_1, 10))
	print ()
			
	#Create a set that holds that list of the unique words from book 1 
	set1 = set(unique_list1)
	
	#Get the unique words from the second dictionary, put them in a list 
	unique_list2 = []
	check_total_2 = 0
	for key in wordfreq2:
		check_total_2 += wordfreq2[key]
		if key:
			unique_list2.append(key)
	print (author2)
	print ('Total distinct words =', len(unique_list2)) #-- unique words 	
	print ('Total words (including duplicates) =', check_total_2)
	print ('Ratio (% of total distinct words to total words) =', round(len(unique_list2) * 100 / check_total_2, 10))
	print ()		
	
	#Create a set that holds that list of the unique words from book 2 
	set2 = set(unique_list2) 
	
	#Words in set1 that are not in set2 and vice versa 
	difference1 = set1 - set2
	difference2 = set2 - set1 
	
	#Frequency of the words in difference1 and difference2
	frequency1 = 0
	for word in wordfreq1:
		if word in difference1:
			frequency1 += wordfreq1[word]
	frequency2 = 0
	for word in wordfreq2:
		if word in difference2:
			frequency2 += wordfreq2[word] 
	
	#Print output 
	print (author1 + " used", len(difference1), "words that " + author2 + " did not use.")
	print ("Relative frequency of words used by " + author1 + " not in common with " + author2 + " = %.10f" %(frequency1 * 100/ check_total_1))   
	print ()
	print (author2 + " used", len(difference2), "words that " + author1 + " did not use.")
	print ("Relative frequency of words used by " + author2 + " not in common with " + author1 + " = %.10f" %(frequency2 * 100/ check_total_2))  

	
def main():
	#Create the master dictionary / scrabble dictionary 
	create_word_dict("words.txt")
	print()
	
	#Enter the names of the two books 
	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")
	print ()
	
	#Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print() 
	
	#Obtain the word dictionaries from the two books 
	wordfreq1 = getWordFreq(book1)
	wordfreq2 = getWordFreq(book2)
	
	#Compare stats from the two books 
	wordComparison(author1, wordfreq1, author2, wordfreq2)
	
main()
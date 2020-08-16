#  File: DNA.py

#  Description: Create a program that will output the largest matching nucleotide sequence between pairs of DNA strands 

#  Student Name: Johnny Zhang

#  Student UT EID: jz5246

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 3/21/2016

#  Date Last Modified: 3/22/2016

#Create substring function that will put all possible nucleotide sequences into a list 
def substring(str, list):
	list = []
	wnd = len(str)
	while (wnd > 0):
		start_index = 0
		while (start_index + wnd <= len(str)):
			piece = str[start_index: start_index + wnd]
			list.append(piece)
			start_index += 1
		wnd -= 1 
	return (list)

def main():
	#Initialize lists that will hold separate lines in the file to represent DNA pairings 
	dna1 = []
	dna2 = []
	#Initialize counter 
	counter = 0
	#Open text file for reading 
	infile = open("dna.txt", "r")
	#Get the number of pairs of DNA strands from first line in file 
	num_pairs = int(infile.readline())
	#Print header 
	print ("\nLongest Common Sequences\n")
	#Create loop that will run num_pairs times, reading two lines per iteration 
	while (counter < num_pairs):
		#Reset lists containing the next pair of DNA strands, max_strand and max_length 
		dna1 = []
		dna2 = []
		max_strand = []
		max_length = 0
		
		#Add the next line from the file to two lists representing DNA1 and DNA2 
		dna1.append(infile.readline())
		dna2.append(infile.readline())
		#Strip white spaces characters from the lists' strings
		dna1[0] = dna1[0].rstrip()
		dna2[0] = dna2[0].rstrip()
		dna1[0] = dna1[0].upper()
		dna2[0] = dna2[0].upper()
		
		#Pass the DNA string into the substring function 
		first_strand = substring(dna1[0], dna1)
		second_strand = substring(dna2[0], dna2)
		
		#Figure out the largest common nucleotide sequence 
		for i in first_strand:
			if (i in second_strand) and (len(i) >= max_length):
				max_length = len(i)
				max_strand.append(i)

		#Get rid of duplicate DNA sequences 
		i = 0
		j = 1
		while(i<len(max_strand)):
			while (j < len(max_strand)):
				if max_strand[i] == max_strand[j]:
					max_strand.remove(max_strand[j])
				else:
					j += 1
			i += 1

		#Print output
		if len(max_strand) == 0:
			print ("Pair %d: No Common Sequence Found\n" %(counter + 1))
		else:
			print ("Pair %d: %s" %(counter + 1, max_strand[0]))
			for i in range(len(max_strand)-1):
				print ("\t%s" %(max_strand[i+1]))
			print()
			
			
			
		#Increment counter 
		counter += 1
	#Close file 
	infile.close()
#Call main
main()
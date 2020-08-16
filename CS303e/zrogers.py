def main():

  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary, these are the keys 
  pop_freq ['1'] = 0
  pop_freq ['2'] = 0
  pop_freq ['3'] = 0 
  pop_freq ['4'] = 0
  pop_freq ['5'] = 0
  pop_freq ['6'] = 0 
  pop_freq ['7'] = 0 
  pop_freq ['8'] = 0 
  pop_freq ['9'] = 0

  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # read the header and ignore
  header = in_file.readline()

  # read subsequent lines
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
	# get the first digit from the population
    first_digit = pop_num[0] 

    # make entries in the dictionary, these are the values 
    pop_freq [first_digit] += 1
   
  # close the file
  in_file.close()
  
  # calculate the total number of frequencies
  total_freq = 0 
  for freq in pop_freq:
    total_freq += int(pop_freq[freq])
  
  # make a list out of all the keys in the dictionary, aka frequencies 
  all_freq = list(pop_freq.keys())
  all_freq.sort()
    
  # write out the result
  print ("Digit\tCount\t%")
  for freq in all_freq:
    print (freq + "\t", end = '') 
    print (str(pop_freq[freq]) + "\t", end = '')
    print (round((pop_freq[freq] / total_freq) * 100, 1))
	
    
	
	
  
main()
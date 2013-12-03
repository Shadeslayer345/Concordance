fileName = raw_input("Enter a file name here ===> ")
readIn = open(fileName+".txt", "r")
writeout = open("Concordance.txt", "w")
textIN = readIn.read()
''' Function To Remove Punctuation From Values To Be Entered In The Concordance '''
def removePunctFrom(iS): # iS = Input String
	if iS.endswith(",") or iS.endswith(";") or iS.endswith(":") or iS.endswith('"') or iS.endswith("'") or iS.startswith("'") or iS.startswith('"') or iS.endswith("!"): # All test cases concerning punctuation that should be removed before adding the value to the concordance
		newS = iS[0:len(iS)-1] # Leaving the word with the punctuation intact, we tell the program to ignore the last value (i.e. the end punctuation)
	else:
		newS = iS # If no puncuation exists, leave the value alone
	return newS # Sends back the value without punctuation 
''' Function To Remove Duplicate Values From The List '''
def removeDupes(iL): # iL = Input List
	return sorted(list(set(iL))) # Set is a data structure that by default cannot contain duplicate values so we sort the list and turn it into a set
''' Function To Display List '''
def displayList(iL): # iL = Input List
	for x in xrange(len(iL)):
		print iL[x] + "\n" # Prints every index from 0 to the last index using x as the index
''' Function To Create A Paragraph Matrix '''
def createPMat(iT): # iL = Input Text
	iT = iT.lower() # Sets all words to lower case values
	sentenceList = iT.split(".") # This parses the iT into sentences which are assumed to be separated by periods.
	wordList = [] # This List's indicies will hold the words from each sentence.
	PMat1 = [] # This List will act as a Matrix by holding the wordList for each sentence as the row index and the indicies of each wordList as the column index
	''' Function To Place Each Separate Word Into An Index In WordList Then Add WordList As An Index Into The Paragraph Matrix '''
	for i in xrange(len(sentenceList)):
		wordList = sentenceList[i].split(" ") # Breaks each sentence into words that are then each added as indicies in the wordList
		PMat1.append(wordList) # Adds each sentences words as a list to the paragraph matrix
	return deleteStartSpace(PMat1) # Returns the matrix with filled indecies and all words now lowercase
	 
''' Function To Delete The Space At The Start Of A Sentece '''
def deleteStartSpace(iL): # iL = Input List
	for x in xrange(len(iL)):
		if iL[x][0] == '': # Test the first value of each index in the matrix(i.e. the first part of the sentence) to see if a space exist
			del iL[x][0] # If a space is found we remove that value
	return iL # Returns the matrix without spaces at the beginning of each sentence
''' Recursive Function To Create A List With Concordances Of Each Word '''
def index(iL, oL, r=0, c=0): # iL = Input List, oL = Output List, r = Row, c = Column
	PMat2 = iL # Naming the iL argument
	occurrence = 0 # Occurence is an integer value representing the total occurence of each word in the File
	citation = "" # Citation is a string value representing where each word occures, based on sentence
	row = r # Row is the parameter that will iterate each index of the matrix when we are assigning a value to test in the paragraph matrix
	column = c # Column is the parameter that will iterate through the each index of the row index value in the paragraph matrix
	test = PMat2[row][column] # Test is the value which will be compared to each word in the text file by means of the paragraph matrix
	glossary = oL # Glossary is the name of th list that we will output
 	done = False
 	if not done: # Part of our exit condition when the value of the row variable has reached the length of the paragraph matrix - 2 we are at the end of the list and should be finished, this will reflect done being True and exiting the loop
		# We use the length of the paragraph matrix - 2 because, with zero based counting we have one less index than the length but also when 
		# dealing with our method ofparsing the file we split at the period. So the last sentence is not truly the last index, the last index is blank
		for sentences in xrange(len(PMat2)-1): # Labeled as such for ease of reading. We will iterate throught each "sentence" in the paragraph as the sentences are each one index in the paragraph matrix (see line 47-48 for why we subtract 2)
			for words in xrange(len(PMat2[sentences])): # Labeled as such for eas of reading. We will iterate through each "word" in the "sentence" of the "paragraph"  as the words are indicies within the indicies of the paragraph matrix
			# We have sentences as the index of paragraph because each sentence has a difference length 
				if test == PMat2[sentences][words]: # Our test for equality
						occurrence += 1 # If the word appears we will increment the occurence by 1
						if occurrence > 1: # Lines 54-57 are for formatting of the final list. 
							citation += ", %d" %sentences # If occurence is greater than 1 then the citation is not the first so a comma should be placed before adding a new citation
						else:
							citation += "%d" %sentences # If occurence is not greater than one then this is the first citation so no comma need be placed in front
		entry = "%s {%d: %s}" %(removePunctFrom(test), occurrence, citation) # Formating of the final list, here we will have the word we are looking for, the total amount of times it appears and in which sententence it appears
		glossary.append(entry) # Labeled as such for ease of reading. We will add an entry to the glossary of words we have
		if column == len(PMat2[row])-1: # If true we have tested every word in the sentence and added its entry to the glossary
			if row == len(PMat2)-2:
				done = True # Will exit the code since we have tested the last word in the last sentence.
			else:	
				index(PMat2, glossary, row+1, 0) # We will then move to the next sentence for testing	
		else: # If the condition in Line 60 is false we have not finished every word in the sentence
			index(PMat2, glossary, row, column+1) # Continues interating throught the same sentence
	return glossary # Returns the output list
''' Final Main Code To Concordanate The File ''' 	
def concordanate(iT): # iT = Input Text
	''' To create a Matrix of the sentences of the Input Text File '''
	Paragraph = createPMat(iT) # This call will create a matrix using the input file
	Concordance = [] # The Final List of all words along with total occurences followed by citations of each occurence
	''' Concordination of each word in the File into a List'''
	Concordance = index(Paragraph, Concordance) # Here we assign the value of Concordance to the returned value from the dictionate
	''' Remove Duplicate Values In The List '''
	Concordance = removeDupes(Concordance)
	return Concordance
''' Call Of The Main Function '''
textOut = concordanate(textIN) # The actual function call, textOut will be assigned the returned value of the concordanate function
''' Loop To Write Each Value To A Text File '''
for x in xrange(len(textOut)): # Going the length of the textOut list
	writeout.write(textOut[x] + "\n") # Transcribe each index to the text file
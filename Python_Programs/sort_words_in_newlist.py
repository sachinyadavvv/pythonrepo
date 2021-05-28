# sort palindrome words
def palindrome(string):
	if(string == string[::-1]):
		return True
	else:
		return False

def printSortedPalindromes(sentence):
	
	newlist = []
	
	lis = list(sentence.split())
	
	for i in lis:
		
		if(palindrome(i)):
			
			newlist.append(i)

	newlist.sort()

	j = 0
	
	for i in range(len(lis)):
		
		if(palindrome(lis[i])):
			lis[i] = newlist[j]
			
			j = j + 1

	for i in lis:
		print(i, end =" ")



sentence = "please refer to the madam to know the level"

printSortedPalindromes(sentence)

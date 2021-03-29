import math
def revword (word):
	newword = ""
	for letter in word:
		newword = letter + newword
	return newword.lower()

def countword ():
	file = open('text.txt')
	word = file.readline().strip().lower()
	count = 0
	for line in file:
		for switchword in line.split():
			if revword(switchword) == word:
				count = count + 1
	return count + 1
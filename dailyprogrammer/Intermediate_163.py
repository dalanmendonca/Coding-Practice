import random

def loadWords(filename="words.txt"):
	#lines = tuple(open(filename, 'r'))
	lines = [line.strip() for line in open(filename)]
	return(lines)

def createOptions(wordArray):
	print "Choose a difficulty level (1-5):"
	difficulty = int(raw_input())
	if difficulty not in range(5):
		print "fuck off"
	else: wordLength = difficulty+4
	masterlist = []
	for w in wordArray:
		if (len(w) == wordLength):
			masterlist.append(w)

	options = random.sample(masterlist, 9)
	return options

def challenge(options = ["retina","roadie","potato","antler","ignore","tailor","orient","entire","dosage"], attempts = 4):
	"""Given the options, this function allows the player to guess the word.
	It informs the player about the number of correct letters in the correct position."""
	secret_word = random.choice(options)
	print "Your options are:"
	for o in options:
		print o

	while(attempts>0):
		print "Guess the word.", attempts,"attempts left"
		guess = raw_input()
		if(len(guess)!= len(secret_word)):
			print "Length mismatch"
		if (guess.upper() == secret_word.upper()):
			print "YOU WIN"
			break
		else:
			score = 0
			for a in range(len(secret_word)):
				score = score+(secret_word[a]==guess[a])
			print "Score:",score,"/",len(secret_word)
		attempts = attempts - 1

wordArray = loadWords()
options = createOptions(wordArray)
challenge(options)

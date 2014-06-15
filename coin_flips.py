#Program to simulate n flips of a unbiased coin
#Also logs each result 
import random


def coin_flips(n):
	global log
	log = ""
	results = {'heads':0, 'tails':0}
	sides = ['heads','tails']
	while(n>0):
		toss=random.choice(sides)
		if(toss=='heads'):
			results["heads"] = results["heads"] + 1
			log = log + "H"
			n = n-1
		else: 
			results["tails"] = results["tails"] + 1
			log = log + "T"
			n = n-1

	return results

print coin_flips(1000)
print log




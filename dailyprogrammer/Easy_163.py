import random
import math

def getresults( rolls ):
	"Given number of rolls of a die, returns percentage frequency of occurence of each number via a dictionary"
	results = {1:0,2:0,3:0,4:0,5:0,6:0}
	counter = 1
	while counter<=rolls:
		x = int(math.ceil(random.random()*6))
		#print x
		counter = counter + 1
		results[x] = results[x] + 1  

	for x in results:
		results[x] = (float(results[x])/rolls)*100
	return results

iterations_array = [10, 100, 1000, 10000, 100000, 1000000]

for a in iterations_array:
	test = getresults(a)
	print repr(a).ljust(7), "%2.2f" % test[1], "%2.2f" % test[2],"%2.2f" % test[3],"%2.2f" % test[4],"%2.2f" % test[5],"%2.2f" % test[6]












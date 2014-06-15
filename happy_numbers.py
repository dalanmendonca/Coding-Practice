SQUARE = dict([(c, int(c)**2) for c in "0123456789"])
def is_happy(n):
	s = set()
	while (n > 1) and (n not in s):
		s.add(n)
		n = sum(SQUARE[d] for d in str(n))
	return n == 1

print "1", is_happy(1)
print "7", is_happy(7)
print "9", is_happy(9)
print "32", is_happy(32)
print "56", is_happy(56)
print "921", is_happy(921)

"""
References:
1. Copied blatanly from http://en.wikipedia.org/wiki/Happy_number 
"""





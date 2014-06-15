#Takes a number and outputs it's english name

numero = str(raw_input(["Enter a number"]))
unit_dict = {'0':'zero','1':'one', '2':'two','3':'three','4':'four', '5':'five','6':'six','7':'seven', '8':'eight','9':'nine'}
tens_dict = {'0':'zero','1':'ten', '2':'twenty','3':'thirty','4':'forty', '5':'fifty','6':'sixty','7':'seventy', '8':'eighty','9':'ninety'}
suffixes = [" ","thousand","million","billion","trillion"]

def chunkify(snumber):
	print "creating chunks"
	snumber = snumber[::-1]
	step = 3
	zap = [snumber[i:i+step] for i in range(0, len(snumber), step)]
	print "printing zap"
	print zap
	crap = []
	for x in zap:
		 crap.append(x[::-1])

	return crap 

def namify(numero_chunks):
	print "Giving names to chunks"
	name_chunks = []
	for x in numero_chunks:
		chunk_len = len(x)
		if chunk_len==1:
			name = unit_dict[x[0]]
		elif chunk_len==2:
			name = tens_dict[x[0]] + unit_dict[x[1]]
		else: name = unit_dict[x[0]] + " hundred and " + tens_dict[x[1]] + unit_dict[x[2]]

		name_chunks.append(name)
	#print "printing named chunks which are returneth"
	#print name_chunks
	return name_chunks

numero_chunks = chunkify(numero)
#print "Chunks"
#print numero_chunks

namified_chunks = namify(numero_chunks)
#print "namified chunks"
#print namified_chunks

i=0
final = []
for x in namified_chunks:
	part = x + " " +suffixes[i] + " "
	final.append(part)
	i = i + 1

#Almost there, gotta handle the teens
print ''.join(reversed(final))




#Count steps in Collatz conjecture

def collatz_loops(numero):
	iterations = 0
	while(1):
		if(numero%2 == 0):
			numero = numero/2
		else:
			numero = 3*numero+1
		iterations = iterations + 1
		if(numero==1):
			break
	return iterations

numero = int(raw_input(["Enter a number"]))
iterations = collatz_loops(numero)

print numero," needed ",iterations," iterations"


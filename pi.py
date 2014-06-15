#Program to calculate π upto n digits

def pi_digits():
    "Generator for digits of pi"
    q,r,t,k,n,l = 1,0,1,1,3,3
    while True:
        if 4*q+r-t < n*t:
            yield n
            q,r,t,k,n,l = (10*q,10*(r-n*t),t,k,(10*(3*q+r))/t-10*n,l)
        else:
            q,r,t,k,n,l = (q*k,(2*q+r)*l,t*l,k+1,(q*(7*k+2)+r*l)/(t*l),l+2)

dig = int(raw_input(["Enter number of digits"]))
digits = pi_digits()
pi_result = []

for i in range(dig): 
	pi_result.append(str(digits.next()))

#Making it pretty

pi_result = pi_result[:1] + ['.'] + pi_result[1:]
pi_result = "".join(pi_result)
print pi_result


"""
References: 
1. Digit extraction algorithms for digits of pi: http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf
2. Different approaches nth digits of pi: https://pythonadventures.wordpress.com/tag/pi/ 
3. Reference implementation: http://stackoverflow.com/questions/9004789/1000-digits-of-pi-in-python
"""
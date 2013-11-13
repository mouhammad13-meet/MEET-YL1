def divisors(n) :
	for a in range(int(n)):
		if n % (a+1) == 0 :
			print n

if __name__=="__main__":
	x = int(raw_input("give me a number"))
	divisors(x)


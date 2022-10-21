# Python3 implementation of the approach

def fact(n):

	res = 1
	for i in range(2, n + 1):
		res = res * i
	return res

def Count_number(N):
	return (N * fact(N))

N = 2

print(Count_number(N))

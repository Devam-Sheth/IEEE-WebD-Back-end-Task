import itertools

def findsubsets(s, n):
	return list(itertools.combinations(s, n))

s=[5,12,29,89,65,81,123]

i=len(s)
while i>=0:
	print(findsubsets(s, i))
	i-=1
	
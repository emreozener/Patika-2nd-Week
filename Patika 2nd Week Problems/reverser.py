def reverser(x):

	for i in x:
		if type(i) == list:
			print(i)
			x[x.index(i)] = i[::-1]

	return x[::-1]
def rec(x):

	def fl_1(y): #flattens given list once
		for i in y:
			if type(i) == list:
				b = y.index(i)
				y[b:b+1] = i
			else:
				continue

	while list in [type(i) for i in x]:
		fl_1(x)

	return x
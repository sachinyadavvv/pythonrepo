#Replace list elements
def replaceOrdinal(lst):
	return [[i for j in range(len(lst[i]))]
	for i in range(len(lst))]
	
lst = [[1, 2, 3], [ 4, 5, 6], [ 7, 8, 9, 10]]
print(replaceOrdinal(lst))

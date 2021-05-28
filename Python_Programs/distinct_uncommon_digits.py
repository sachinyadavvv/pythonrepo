# distinct uncommon digits
def disticntUncommonDigits(A, B):

	A = str(A)

	B = str(B)

	lis1 = list(map(int, A))
	
	lis2 = list(map(int, B))

	lis1 = set(lis1)

	lis2 = set(lis2)

	lis = lis1.symmetric_difference(lis2)

	lis = list(lis)
lis.sort(reverse = True)

	for i in lis:
		print(i, end =" ")
A = 378212
B = 78124590

disticntUncommonDigits(A, B)

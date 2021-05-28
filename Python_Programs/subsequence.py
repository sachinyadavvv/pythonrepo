#subsequence
st = []

def find(inp, out) :
	if len(inp)== 0 :
		if len(out) != 0 :
			st.append(out)
		return

	find(inp[1:], out[:])

	if len(out)== 0:
		find(inp[1:], inp[:1])
	elif inp[0] > out[-1] :
		out.append(inp[0])
		find(inp[1:], out[:])

ls1 = [1, 3, 2]
ls2 = []

find(ls1, ls2)

for i in st:
	print(*i)

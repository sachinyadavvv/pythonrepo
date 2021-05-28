# diagonalelement
test_list1 = [1, 6, 8, 5, 3]
test_list2 = [8, 10, 3, 4, 5]

print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

res = []
for idx in range(0, len(test_list1) - 1):
	res.append(test_list1[idx] + test_list2[idx + 1])

print ("List after diagonal addition : " + str(res))

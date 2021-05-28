# listOfTuples
test_list = [('a', 2), ('c', 3), ('d', 4)]

sort_order = [4, 2, 3]

print ("The original list is : " + str(test_list))

print ("The sort order list is : " + str(sort_order))

res = [i for j in sort_order
	for i in filter(lambda k: k[1] == j, test_list)]

print ("The list after appropriate sorting : " + str(res))

# listArray
IntList = [10, 20, 30]
print("List of numbers: ")

print(IntList)

StrList = ["hello", "For", "hello"]
print("List of Strings: ")

print(StrList)
Non_homogeneous_list = [10, "hello", 20.890,\
						"for", 30, "hello"]
print("List of non-homogeneous elements: ")
print(Non_homogeneous_list)

print("Size of the Non-homogeneous list: ",\
			len(Non_homogeneous_list))

NewList = ["hello", "for", "hello"]
print("Original List: ", NewList)
NewList.append("the")

print("After adding an element the"\
					"list becomes: ")
print(NewList)
NewList.insert(3, "is")

print("After adding an element at"\
		"index 3 the list becomes: ")
print(NewList)
NewList.extend(["best", "CS", "website"])
print("After adding 3 elements at the"\
			"end, the list becomes: ")
print(NewList)
NewList.remove("the")

print("After removing an element"\
			"the list becomes: ")
print(NewList)
NewList.pop(3)

print("After removing an element "\
	"from index 3 the list becomes: ")
print(NewList)

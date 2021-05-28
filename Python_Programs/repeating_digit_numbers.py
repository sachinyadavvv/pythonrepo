# repeating digits number
test_list = [4252, 6578, 3421, 6545, 6676]

print("The original list is : " + str(test_list))

res = [sub for sub in test_list if len(set(str(sub))) == len(str(sub))]

print("List after removing repeating digit numbers : " + str(res))

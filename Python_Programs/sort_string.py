# sort string
from string import punctuation

def get_pnc_count(strng):
	
	return len([ele for ele in strng if ele in punctuation])

test_list = ["gfg@%^", "is", "Best!", "fo@#r", "@#$ge24eks!"]

print("The original list is : " + str(test_list))

test_list.sort(key = get_pnc_count)
print("Sorted Strings list : " + str(test_list))

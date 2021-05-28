#nested dictionary
from collections import OrderedDict
from operator import getitem

test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
			'Akshat' : {'roll' : 54, 'marks' : 12},
			'Akash' : { 'roll' : 12, 'marks' : 15}}

print("The original dictionary : " + str(test_dict))

res = OrderedDict(sorted(test_dict.items(),
	key = lambda x: getitem(x[1], 'marks')))
print("The sorted dictionary by marks is : " + str(res))

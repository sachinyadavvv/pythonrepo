# nested list

def sum_nestedlist( l ):

	total = 0
	
	for j in range(len(l)):
	
		if type(l[j]) == list :
		
			sum_nestedlist(l[j])
		else:
		
			total += l[j]
			
	return total
			
print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))

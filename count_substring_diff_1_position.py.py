# function to count same pairs
def pair_count(d):
	return sum((i*(i-1))//2 for i in d.values())


# function to return total number of strings which satisfy required conditions.
def Difference(array,m):
	# dictionary changed will store strings with wild cards
	# dictionary same will store strings that are equal.
	changed,same={},{}
	#iterating for all strings in the given array.
	for s in array:
		# if we found the string then increment by 1 else it will get default value 0.
		same[s]=same.get(s,0)+1
		# iteraing on a single string
		for i in range(m):
			# adding special symbol to the string
			t=s[:i]+'#'+s[i+1:]
			# incrementing the string if founded else it will get default value 0.
			changed[t]=changed.get(t,0)+1
	# return counted pairs - equal pairs
	return pair_count(changed)-pair_count(same)*m

# driver code
if __name__=="__main__":
	n,m=3,3
	array=["abc","abd","bbd"]
	print(Difference(array,m))

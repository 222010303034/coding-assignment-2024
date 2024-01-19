def inter(arr1, arr2):
	set1 = set(arr1)
	result = []
	for num in arr2:
		if num in set1:
			result.append(num)
			set1.remove(num)

	return result
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
intersection = inter(arr1, arr2)
for num in intersection:
	print(num, end=" ")

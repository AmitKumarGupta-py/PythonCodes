def second_largest(arr):
	first, second = float('-inf'), float('-inf')
	for n in arr:
		if n > first:
			first, second = n, first
		elif n > second and n != first:
			second = n
	return second if second != float('-inf') else None
print(second_largest([10, 20, 4, 45, 99]))
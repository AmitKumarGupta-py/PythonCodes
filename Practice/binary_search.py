def binary(s, target):
	s = sorted(s)
	print(s)
	low, high = 0, len(s) - 1
	while low <= high:
		mid = (low + high) // 2
		if s[mid] < target:
			low = mid + 1
		elif s[mid] > target:
			high = mid - 1
		else:
			return mid
	return -1
print(binary([1,2,3,2,3,5,6,3,8,9,0,11], 6))
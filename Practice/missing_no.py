

def miss_num(arr, n):
	expected_sum = (n * (n+1)) // 2
	actual_sum = sum(arr)
	return expected_sum - actual_sum
print(miss_num([1,2,4,5,6], 6))
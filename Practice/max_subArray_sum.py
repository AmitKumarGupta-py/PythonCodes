def max_subarray_sum(arr):
	max_sum = current_sum = arr[0]
	for num in arr[1:]:
		current_sum = max(num, current_sum + num)
		max_sum = max(max_sum, current_sum)
	return max_sum
print(max_subarray_sum([-2,1, -3, 4, -1, 2, 1, -5, 4]))



def is_perfect_square(x):
	return int(x**0.5)**2 == x
print(is_perfect_square(16))
print(is_perfect_square(15))

def sub_array_sum(arr):
	max_sum = current_sum = a[0]
	
	for num in arr[1:]:
		current_sum = max(num, current_sum + num)
		max_sum = max(max_num, current_sum)
	return max_sum

arr = [1, -2, -4, 5, 3, -6, 2, -8, 1, 0, 3, 9, -7]
print(max_subarray_sum(arr))

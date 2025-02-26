def find_duplicates(arr):
	seen = set()
	duplicate = set()
	for num in arr:
		if num in seen:
			duplicate.add(num)
		else:
			seen.add(num)
	return list(duplicate)

min = min(find_duplicates([1,2,3,4,2,3,5,6,5,7,8,9,0]))

max = max(find_duplicates([1,2,3,4,2,3,5,6,5,7,8,9,0]))

count = len(find_duplicates([1,2,3,4,2,3,5,6,5,7,8,9,0]))

sum = sum(find_duplicates([1,2,3,4,2,3,5,6,5,7,8,9,0]))

print(f"min {min} max {max} count {count} sum {sum}")

# print(find_duplicates([1,2,3,4,2,3,5,6,5,7,8,9,0]))
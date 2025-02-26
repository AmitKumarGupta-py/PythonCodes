list1 = [1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 4, 5, 6, 5, 7, 6, 7, 8, 9, 8, 9, 10, 6, 7, 8, 9, 10]

list2 = list(set(list1))

dict = {num: list1.count(num) for num in set(list1)}

print(dict)

min_value = min(dict.values())
result = [key for key, value in dict.items() if value == min_value]

	
print(min(result))

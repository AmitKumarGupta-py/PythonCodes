def count_vowel(s):
	return sum(1 for char in s if char.lower() in 'aeiou')
print(count_vowel("Hello, World!"))
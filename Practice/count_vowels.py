def count_vowels(s):
    s_lower = s.lower()
    print("Lowercase string:", s_lower)  # Debug: show lowercase string
    vowels_found = [char for char in s_lower if char in "aeiou"]
    print("Vowels found:", vowels_found)  # Debug: list the vowels found
    return len(vowels_found)

print(count_vowels("Life is beautiful!"))



def vowelcount(s):
	return sum(1 for i in s.lower() if i in "aeiou")
print(vowelcount("Hi hello"))
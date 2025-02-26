def palindrome(s):
	return s.lower() == s.lower()[::-1]
print(palindrome("Radar"))


def longest_word(sent):
	words = {k:len(k) for k in sent.split() }
	print(words)
	print(max(words.values()))
		
print(longest_word("The quick fox jumped over a lazy dog"))
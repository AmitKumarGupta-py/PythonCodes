def stringT(inputS):
	if not all(c in 'AGCT' for c in inputS):
		return "Invalid input"
    
	countA = inputS.count('A')
	countT = inputS.count('T')

    
	if countA < countT:
        	return "Valid input"
	else:
		return "Invalid input"

inputS = input("Enter a string containing only A, G, C, and T: ")
result = stringT(inputS)
print(result)

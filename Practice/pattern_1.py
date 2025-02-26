n = 5
for i in range(n):
	print(" ",end="")
	for j in range(i+1):
		print("*", end="")
	print(" ")

for i in range(n):
	print(" ", end="")
	for j in range(i+1, n):
		print("*", end="")

	print(" ")	
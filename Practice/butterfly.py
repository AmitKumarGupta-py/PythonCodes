n = 5
for i in range(1,n+1):
	left = "*" * i
	space = " " * 2*(n-i)
	print(left, space, left)
for i in range(n, 0, -1):
	left =  "*" * i
	space = " " * 2*(n-i)
	print(left, space, left)


print("============================")

for i in range(n, 0, -1):
	left = "*" * i
	space = " " * 2*(n-i)
	print(left, space)

print("===============================")

for i in range(1, n+1):
	left =  "*" * i
	space = " " * 2*(n-i)
	print(left, space)

print("===============================")

for i in range(n, 0, -1):
	space = " " * (n-i)
	left = "*" * i
	print(space, left)

print("===============================")

for i in range(1, n+1):
	space = " " * (n-i)
	left = "*" * i
	print(space, left)